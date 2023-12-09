#!/usr/bin/python3
"""This is the module for the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json



class HBNBCommand(cmd.Cmd):
    """This is the command interpreter for the AirBnb clone Project"""

    prompt = "(hbnb) "
    def emptyline(self):
        """Do nothing on an empty line."""
        pass
    def do_create(self, arg):
        """This creates a new instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
              print("** class doesn't exist **" )
        else:
            b = storage.classes([args])
            b.save()
            print(b.id)

    def do_show(self, arg):
        """this prints the string representation of instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                     print(storage.all()[key])


    def do_destroy(self, arg):
        """This Deletes an instance based on the class name and id"""

        if arg == "" or arg is None:
            print("** class name missing")
        else:
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """This  Prints all string representation of all instances based or not on the class name."""
        if arg != "":
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)


    def do_update(self, arg):
        """This Updates an instance based on the class name and id by adding or updating attribute"""
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

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
