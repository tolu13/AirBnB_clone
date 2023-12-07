### AirBnB Clone - Console

### DESCRIPTION OF THE PROJECT
>
> - this project give us the overview, how to
> - put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
> - create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
> - create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
> - create the first abstracted storage engine of the project: File storage.
> - create all unittests to validate all our classes and storage engine
> 
> 
### DESCRIPTION OF THE COMMAND INTERPRETER
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
****
### AUTHORS
***
#### @Tolu OLanrewaju
