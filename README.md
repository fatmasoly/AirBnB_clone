README.md
Project Description
This project is an implementation of a command-line interpreter
designed for managing instances of various classes defined in
the models module. It provides a convenient way to create, view,
update, and delete instances of different types such as Users,
Places, Reviews, Cities, States, Amenities, and more, mimicking
the functionality of Airbnb-like applications.

Command Interpreter
How to Start It
To start the command interpreter, execute the console.py script
located in the project directory. This can be done by running
the following command in your terminal:

    ./console.py
How to Use It
Once the interpreter is started, you can use various commands to
interact with the objects. Here are some of the supported commands:

    quit: Exits the command interpreter.
EOF: Exits the command interpreter(same as quit).
create ClassName: Creates a new instance of the specified class.
show ClassName ID: Displays the details of a
specific instance by class name and ID.
destroy ClassName ID: Deletes a specific
instance by class name and ID.
all ClassName: Displays all instances of a specific class.
update ClassName ID AttributeName Value:
    Updates an attribute of a specific instance.
count ClassName: Counts the number of
instances of a specified class.
Examples
Creating a New User
(hbnb) create User
Showing Details of a User with ID 123
(hbnb) show User  123
Deleting a User with ID 123
(hbnb) destroy User  123
Updating a User's First Name to John
(hbnb) update User  123 first_name "John"
Counting the Number of Users
(hbnb) count User
These are just a few examples of the commands supported by
the command interpreter. You can explore more commands
by typing help within the interpreter.
