#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
        Command line for the HBNB shell
    """
    intro = 'Welcome to the HBNB shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        # raise ExitCmdException()
        sys.exit(1)

    def do_EOF(self, arg):
        """Exit with Ctrl-D"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
