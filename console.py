#!/usr/bin/python3
"""command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Exit our command interpreter"""
        return True

    def do_EOF(self, args):
        """Exit our command interpreter"""
        return True

    def emptyline(self):
        """empty line + ENTER"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
