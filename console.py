#!/usr/bin/python3
"""
    Command prompt module
    Contains the entry point of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
        Defining HBNBCommand class that contains the entry point
        of the command interpreter
    """
    prompt = "(hbnb)"

    def do_quit(self, *args):
        """Quit command to exit the program
        """
        return (True)

    def do_EOF(self, *args):
        """ EOF command to exit the program
        """
        return (True)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
