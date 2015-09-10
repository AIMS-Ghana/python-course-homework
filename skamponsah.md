AIMS-Ghana Python course work

This repository contains file on my three weeks course in python.
Project work files are 1. project_seir.py 2. shape_drawing.py
Note: run code from the terminal.

1. project_seir.py
This plots the SEIR model and plots results using the normal ODE method and also the Gillepse method on one graph
 
Code runs as this:

$ ./project_seir.py withnegativevalues.json

Error: the parameter input had negative values for whichever inputs

$ ./project_seir.py

... same as next line ...

$ ./project_seir.py -h

... useful info about usage ...

$ ./project_seir.py config.json

... rows of numerical output, including header line ...

$ ls plot.png
... finds plot you just made ...
$ ./project_seir.py config2.json target.csv target.png
$ ls target.*
... finds the csv and png you just created ...
$ ./project_seir.py config2.json -g 10 target.csv target.png
$ ls target.*
... finds the csv and png you just created, should be Gillespie runs ...



2. shape_drawing.py

This draws different shapes with different colors and sizes on one output.

Code runs as this:

$ ./shape_drawing.py garbageinput.csv

Error: ... indicate what is wrong on the first line with an error ...

$ ./shape_drawing.py

... same as next line ...

$ ./shape_drawing.py -h

... useful info about usage ...

$ ./shape_drawing.py input.csv

... real time animation of shape drawing ...

$ ./shape_drawing.py input.csv output.eps

$ ls output.eps

... finds plot you just made ...


