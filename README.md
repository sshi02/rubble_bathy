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
`--xslope` := (int) beginning x coordinate of slope relative to mglob, requires above arguments

structure arguments    
`-r` := (float) rightward slope relative to a dx of 1 (m), required  
`-l` := (float) leftward slope relative to a dx of 1 (m), required  
`-x` := (int) toe coordinate relative to mglob, required  
`-w` := (float) crest width (m), required  
`-h` := (float) crest height (m), required  
`--todep` := (float) forced depth of toe (m), optional  
`--trunctail` := forced tructation of structure depth, at toe depth, optional  

optional arguments  
`--dx` := (float) dx [default 1 (m)]  
`-o` := output directory of script  
`--frictionfile` := to-modify input friction file (i.e friction.txt). This is an optional argument, and requires friction to be supplied  
`--friction` := friction coefficient for structure in friction file. This is an optional argument, but does not require a friction file to be supplied (it will produce a friction file by itself if added to arguments)  
`--debug` := script outputs a test.txt file for modified depth  

### usage
example usage - data case  
*input depth data file, inserting a structure with a rightward slope of 0.05, 
leftward slope of 0.10, crest height of 5 (m), and crest width of 3 (m), with the toe starting at 10 (m)*  
`> python3 rubblebathy.py -i depth.txt -o new_depth/ -r 0.05 -l 0.10 -h 5 -w 3 -x 10`

example usage - flat/slope case  
*input sloped bathymetry in a grid of 25 [m] x 3 [n], inserting a structure with a rightward slope of 0.10, leftward slope of 0.15, crest height of 3 (m) and crest width of 2 (m), with the toe starting at 16 (m). The flat water depth is 8 (m), the slope of the bathymetry is 0.05 and the start of the slope is at 20 (m). Note that dx is 0.5, so xslope and toe coordinate arguments need to be carefully handled at input.*  
`> python3 rubblebathy.py --dx 0.5 --flat 8 --slope 0.05 --xslope 8 --mglob 50 --nglob 3 -r 0.10 -l 0.15 -h 3 -w 2 -x 10`
