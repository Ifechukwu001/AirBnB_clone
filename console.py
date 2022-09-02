#!/usr/bin/python3
""" Module that is the entry point to the command interpreter.
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class

    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program

        """
        models.storage.save()
        return True

    def precmd(self, line):
        """ Works on command line before execution

        """
        line = line.lower()
        if line == "eof":
            print()
            line = "quit"
        return line

    def emptyline(self):
        """ Does nothing if empty line is passed

        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
