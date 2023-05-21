#!/usr/bin/python3
import cmd
from models.base_model  import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City 
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        Command line for the HBNB shell
    """
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User, "Amenity": Amenity,
        "Place": Place, "City": City, "Review": Review,
        "State": State
        }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit with Ctrl-D"""
        print()
        return True

    def do_create(self, arg):
        """Creates an Instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        line = parse(arg)
        if line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if line[1]:
                name = "{}.{}".format(line[0], line[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id;
            Save changes to JSON file
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        line = parse(arg)
        if line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if line[1]:
                name = "{}.{}".format(line[0], line[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        line = parse(arg)
        new_obj = []
        if len(arg) == 0:
            for obj in storage.all().values():
                if line[0] == obj.__class__.__name__:
                    new_obj.append(obj.__str__())
            print(new_obj)
        elif line[0] in HBNBCommand.classes:
            for key, ob in storage.all().items():
                if line[0] in key:
                    new_obj.append(ob)
            print(new_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id 
            by adding or updating attribute .
        """
        line = parse(arg)
        print(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return 
        elif len(line) == 2:
            print("** attribute name missing **")
            return
        elif len(line) == 3:
            print("** value missing **")
            return
        else:
            if line[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            key = "{}.{}".format(line[0], line[1])
            if key not in storage.all().keys():
                print("** no instance found **")
                return
            else:
                cast = type(eval(line[3]))
                arg3 = line[3].strip('\"')
                setattr(storage.all()[key], line[2], cast(arg3))
                storage.save()

    def do_count(self, line):
        """Display count of instances specified"""
        if line in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")


    def default(self, line):
        """Accepts class name followed by arguement"""
        args = line.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg)
            elif command == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)
            elif command == 'update':
                args = args[1].split(',')
                id_arg = args[0].strip("'")
                id_arg = id_arg.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))
        

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(arg.split())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
