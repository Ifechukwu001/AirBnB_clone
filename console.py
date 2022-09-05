#!/usr/bin/python3
""" Module that is the entry point to the command interpreter.
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class

    """
    prompt = "(hbnb) "
    __classes = {"BaseModel": BaseModel, "User": User, "State": State,
                 "City": City, "Amenity": Amenity, "Place": Place,
                 "Review": Review}

    def do_create(self, args):
        """ Creates a new instance of BaseModel and its subclasses

        """
        cmd_args = args.split()
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_inst = HBNBCommand.__classes[cmd_args[0]]()
            models.storage.save()
            print(new_inst.id)

    def do_show(self, args):
        """ Prints the string representation of an instance

        """
        cmd_args = args.split()
        if HBNBCommand.valid(cmd_args):
            class_name = cmd_args[0]
            instance_id = cmd_args[1]
            instances = models.storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key not in instances:
                print("** no instance found **")
            else:
                instance = instances[key]
                print(instance)

    def do_destroy(self, args):
        """ Deletes an instance based on the classname and id

        """
        cmd_args = args.split()
        if HBNBCommand.valid(cmd_args):
            class_name = cmd_args[0]
            instance_id = cmd_args[1]
            instances = models.storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key not in instances:
                print("** no instance found **")
            else:
                del instances[key]
                models.storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances
            based on or not on the class name

        """
        cmd_args = args.split()
        if len(cmd_args) == 0:
            instances = models.storage.all()
            instance_list = []
            for instance in instances.values():
                instance_list.append(str(instance))
            print(instance_list)
        elif len(cmd_args) > 0:
            class_name = cmd_args[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                instances = models.storage.all()
                instance_list = []
                for key, instance in instances.items():
                    if key.startswith(class_name):
                        instance_list.append(str(instance))
                print(instance_list)

    def do_update(self, args):
        """ Updates an instance based on class name and id

        """
        cmd_args = args.split()
        if HBNBCommand.valid(cmd_args):
            class_name = cmd_args[0]
            instance_id = cmd_args[1]
            instances = models.storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key not in instances:
                print("** no instance found **")
                return None
            if len(cmd_args) < 3:
                print("** attribute name missing **")
                return None
            if len(cmd_args) < 4 and not cmd_args[2].startswith("{"):
                print("** value missing **")
                return None
            if cmd_args[2].startswith("{"):
                dict_start = args.index("{")
                dict_end = args.index("}")
                att_dict = eval(args[dict_start:dict_end + 1])
                instance = instances[key]
                for attr_name, value in att_dict.items():
                    instance.__dict__[attr_name] = value
                instance.save()
            else:
                attr_name = cmd_args[2]
                value_start = args.find("\"") + 1
                if value_start > 0:
                    value_end = args.find("\"", value_start) + 1
                    value = args[value_start - 1:value_end]
                    print(value)
                else:
                    value = cmd_args[3]
                    print(value)
                instance = instances[key]
                instance.__dict__[attr_name] = eval(value)
                instance.save()

    def do_count(self, args):
        """ Counts the number of instances of a class

        """
        cmd_args = args.split()
        class_name = cmd_args[0]
        instances = models.storage.all()
        count = 0
        for instance in instances.values():
            if instance.__class__.__name__ == class_name:
                count += 1
        print(count)

    def do_quit(self, args):
        """ Quit command to exit the program

        """
        models.storage.save()
        return True

    def do_EOF(self, args):
        """ Exits the console

        """
        print()
        models.storage.save()
        return True

    def precmd(self, line):
        """ Works on command line before execution

        """
        new_line = line.split(".")
        if len(new_line) == 2:
            class_name, cmd_function = new_line
            command, arguments = cmd_function.split("(")
            arguments = arguments.strip(")").split(",")
            instance_id = attributes = ""
            if arguments:
                instance_id = arguments.pop(0).strip("\"")
                attributes = ",".join(arguments)
                if not attributes.startswith(" {"):
                    attributes = attributes.replace("\"", "", 2)
                    attributes = attributes.replace(",", "")
            line = "{} {} {} {}".format(command, class_name,
                                        instance_id, attributes)
        return line

    def emptyline(self):
        """ Does nothing if empty line is passed

        """
        pass

    @classmethod
    def valid(cls, cmd_args):
        """ Validates a command line

        """
        if len(cmd_args) == 0:
            print("** class name missing **")
            return False
        elif cmd_args[0] not in cls.__classes:
            print("** class doesn't exist **")
            return False
        elif len(cmd_args) < 2:
            print("** instance id missing **")
            return False
        else:
            return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
