Project Description
This project is an implementation of a command-line interpreter for managing Airbnb-like objects. It includes classes for various components such as users, places, reviews, cities, states, amenities, and more. The command-line interpreter allows users to create, retrieve, update, and delete these objects using simple commands.

Command Interpreter
Starting the Interpreter
To start the command interpreter, execute the console.py script located in the project directory.

bash
Copy code
./console.py
Using the Interpreter
Once the interpreter is started, you can use various commands to interact with the objects. The supported commands include:

quit: Exit the command interpreter.
EOF: Exit the command interpreter (same as quit).
create: Create a new instance of a specified class.
show: Display details of a specific instance.
destroy: Delete a specific instance.
all: Display details of all instances or instances of a specific class.
update: Update attributes of a specific instance.
count: Count the number of instances of a specified class.
Examples
Create a new user:
bash
Copy code
(hbnb) create User
Show details of a user with ID 123:
bash
Copy code
(hbnb) show User 123
Delete a specific instance:
bash
Copy code
(hbnb) destroy User 123
Display details of all instances of a specific class:
bash
Copy code
(hbnb) all User
Update attributes of a specific instance:
bash
Copy code
(hbnb) update User 123 first_name "John"
Count the number of instances of a specified class:
bash
Copy code
(hbnb) count User
These are just a few examples of the commands supported by the command interpreter. You can explore more commands by typing help within the interpreter.