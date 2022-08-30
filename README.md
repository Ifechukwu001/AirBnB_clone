#AirBnB clone - The console.

##Project Description

Team project to build a clone of AirBnB.

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project visit the Wiki.

The console willl perform the following tasks:

*create a new object.
*retrive an object from a file.
*do operations on objects.
*destroy an object.

##storage

All the classes are handled by the Storage engine in the FileStorage Class.

##Installation

To get usage of the console use the following command
```
git clone https://github.com/Ifechukwu001/AirBnB_clone.git
```

#Usage

The Console shows a prompt and wait for the BaseModel to type a command, interpretes and run the input command and display the prompt again. You can exit the console using quit command EOF or Ctrl + D.

##Interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#Non-Interactive mode
```
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
```
