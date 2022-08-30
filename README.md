# rubblebathy.py
rubblebathy.py is a preprocessing script, whihc takes in command line arguments or JSON file input (TODO). Current implementation is for 1-D cases. The output of the script is a depth.txt file and an optional fricition file for FUNWAVE-TVD

### arguments
Usage requires a batch of arguments from several categories. Generally, it will compose of bathymetry/depth arguments, structure arguments, and optional flags.

depth/friction data file arguments  
`--json` := JSON file input, ignore all other args  
`-i` := to-modify input depth file (i.e depth.txt). If a depth file is supplied, flat/slope depth args will be ignored  

new flat/slope depth arguments  
`--nglob`, `--mglob` := (int) nglob and mglob respectively  
`--flat` := (float) flat depth, requires mglob, nglob arguments  
`--slope` := (float) seaward slope, requires xslope argument and above arguments  
`--xslope` := (int) beginning x coordinate of slope, requires above arguments

structure arguments    
`-r` := (float) rightward slope, required  
`-l` := (float) leftward slope, required  
`-x` := (int) toe coordinate, required  
`-w` := (float) crest width, required  
`-h` := (float) crest height, required  
`--todep` := (float) forced depth of toe, optional  
`--trunctail` := forced tructation of structure depth, at toe depth, optional  

optional arguments  
(TODO) '--dx' := (float) dx  
`-o` := output directory of script  
`--frictionfile` := to-modify input friction file (i.e friction.txt). This is an optional argument, and requires friction to be supplied  
`--friction` := friction coefficient for structure in friction file. This is an optional argument, but does not require a friction file to be supplied (it will produce a friction file by itself if added to arguments)  
`--debug` := script outputs a test.txt file for modified depth  
