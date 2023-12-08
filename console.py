#!/usr/bin/python3
"""This is the module for the entry point of the command interpreter"""

import cmd
class HBNBCommand(cmd.Cmd):
    """This is the command interpreter for the AirBnb clone Project"""

    prompt = "(hbnb) "
    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF."""
        print()
        return True

    def help_quit(self):
        """Print help message for quit command."""
        print("Quit the program")

    def help_EOF(self):
        """Print help message for EOF command."""
        print("Exit the program on EOF")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
