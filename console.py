#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models import storage
import json


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        self.precmd(line)

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        print()
        return True

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        else:
            class_dict = storage.classes()
        if line not in class_dict:
            print("** class doesn't exist **")
        else:
            new_instance = class_dict[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        if line is None or line == "":
            print("** class name missing **")
        else:
            args = line.split(' ')
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) <= 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        if line is not None or line != "":
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_list = [str(obj) for key, obj in storage.all().items()
                    if type(obj).__name__ == args[0]]
                print(new_list)
        else:
            insta_list = [str(obj) for key, obj in storage.all().items()]
            print(insta_list)

    def precmd(self, line):
        parts = line.split('(')
        if len(parts) != 2:
            return line
        class_name, rest = parts[0].split('.')
        method = rest.strip()
        args = parts[1].rstrip(')')
        if ',' in args:
            unique_id, attr_dict = args.split(',', 1)
            unique_id = unique_id.strip().strip('"')
            attr_dict = attr_dict.strip()
        else:
            unique_id = args.strip().strip('"')
            attr_dict = None

        attr_value = ""
        if method == "update" and attr_dict:
            if attr_dict.startswith('{') and attr_dict.endswith('}'):
                self.update_dict(class_name, unique_id, attr_dict)
                return ""
            else:
                parts = attr_dict.split(',', 1)
                attr_value = parts[0].strip()
                if len(parts) == 2:
                    attr_value += ' ' + parts[1].strip()
        cmd = f"{method} {class_name} {unique_id}"
        if attr_value:
            cmd += f" {attr_value}"
        self.onecmd(cmd)
        return cmd


    def do_count(self, line):
        args = line.split(' ')
        if args[0] is None:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            count_list = [k for k in storage.all() if k.startswith(args[0] + '.')]
            print(len(count_list))

    def do_update(self, line):
        parts = line.split()
        if not parts:
            print("** class name missing **")
            return

        class_name = parts[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(parts) < 2:
            print("** instance id missing **")
            return

        instance_id = parts[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(parts) < 3:
            print("** attribute name missing **")
            return

        attribute = parts[2]
        if len(parts) < 4:
            print("** value missing **")
            return

        value = " ".join(parts[3:])
        value = value.replace('"', '')
        attributes = storage.get_attr()[class_name]
        cast = attributes.get(attribute)
        if cast:
            try:
                value = cast(value)
            except ValueError:
                print("** invalid value for attribute **")
                return

        setattr(storage.all()[key], attribute, value)
        storage.all()[key].save()





if __name__ == '__main__':
    HBNBCommand().cmdloop()
