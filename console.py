#!/usr/bin/python3
""" Module that is the entry point to the command interpreter.
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class

    """
    prompt = "(hbnb) "
    __classes = {"BaseModel": BaseModel, "User": User}

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
            elif len(cmd_args) < 3:
                print("** attribute name missing **")
            elif len(cmd_args) < 4:
                print("** value missing **")
            else:
                attr_name = cmd_args[2]
                value = cmd_args[3].strip('\"')
                instance = instances[key]
                instance.__dict__[attr_name] = value
                instance.save()

    def do_quit(self, args):
        """ Quit command to exit the program

        """
        models.storage.save()
        return True

    def precmd(self, line):
        """ Works on command line before execution

        """
        if line == "EOF":
            print()
            line = "quit"
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
