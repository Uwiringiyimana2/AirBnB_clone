#!/usr/bin/python3
"""

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ """

    prompt = '(hbnb) '
    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("Exit an interpreter")

    def do_EOF(self, arg):
        print()
        return True

    def help_EOF(self):
        print("Exit an interpreter")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
