#!/usr/bin/python3
"""This script implements a command-line
interpreter for managing instances of
the classes defined in the models module."""

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
    """
    Defines a Class for the command interpreter,
    providing a command-line interface
    for managing instances of the classes
    defined in the models module.

    Attributes:
        prompt (str): The command prompt displayed to the user.

    """

    prompt = "(hbnb) "

    def precmd(self, line):
        """
        Preprocess the command line input before it is executed.

        Args:
            line (str): The raw command line input.

        Returns:
            str: The preprocessed command line input.
        """
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

    def default(self, line):
        """Handle any unrecognized command entered by the user."""
        self.precmd(line)

    def do_quit(self, line):
        """Exit the program upon receiving the quit command."""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_EOF(self, line):
        """Handle the end-of-file signal,
        printing a newline character."""
        print()
        return True

    def do_create(self, line):
        """
        Create a new instance of a specified class.

        Args:
            line (str): The name of the class to instantiate.

        Raises:
            KeyError: If the class does not exist in storage.
        """
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
        """
        Display the string representation of a specified instance.

        Args:
            line (str): The class name and instance id, separated by space.

        Raises:
            KeyError: If the class or instance does not exist in storage.
        """
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
        """
        Destroy a specified instance based on class name and id.

        Args:
            line (str): The class name and instance id, separated by space.

        Raises:
            KeyError: If the class or instance does not exist in storage.
        """
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
        """
        Print all string representations of instances,
        optionally filtered by class.

        Args:
            line (str, optional): The class name to filter instances by.
        """
        if line is not None or line != "":
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_list = [str(obj)
                            for key, obj in storage.all().items()
                            if type(obj).__name__ == args[0]]
                print(new_list)
        else:
            insta_list = [str(obj)
                          for key, obj in storage.all().items()]
            print(insta_list)

    def do_count(self, line):
        """
        Count the number of instances of a specified class.

        Args:
            line (str): The class name to count instances of.

        Raises:
            KeyError: If the class does not exist in storage.
        """
        args = line.split(' ')
        if args[0] is None:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            count_list = [k for k in storage.all()
                          if k.startswith(args[0] + '.')]
            print(len(count_list))

    def do_update(self, line):
        """
        Update the attributes of a specified instance.

        Args:
            line (str): The class name, instance id, attribute
            name, and new value, separated by spaces.

        Raises:
            KeyError: If the class or instance does not exist in storage.
            ValueError: If the value cannot be cast to
            the attribute's data type.
        """
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

    def fix_dict(self, cls_name, unq_id, str_dict):
        """Helper method for update() with a dictionary."""
        try:
            data = json.loads(str_dict)
        except json.JSONDecodeError:
            print("** Invalid JSON format **")
            return

        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if unq_id is None:
            print("** instance id missing **")
            return
        key = f"{cls_name}.{unq_id}"

        if key not in storage.all():
            print("** no instance found **")
            return
        attributes = storage.get_attr()[cls_name]
        instance = storage.all()[key]

        for attribute, value in data.items():
            if attribute in attributes:
                value = attributes[attribute](value)
            setattr(instance, attribute, value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
