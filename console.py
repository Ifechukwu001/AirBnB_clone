#!/usr/bin/python3
"""A file that uses the cmd module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB console command"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        """quits from the command interpreter"""
        raise SystemExit

    def do_EOF(self, args):
        """Exits the command interpreter"""
        raise SystemExit

    def emptyline(self):
        """Prints an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
