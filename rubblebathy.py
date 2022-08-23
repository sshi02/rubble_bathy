import numpy as np
import sys, getopt, json

def main(argv):
    # init vars
    inputfile = None
    outdir = None
    frictionfile = None
    jsonfile = None
    flatdepth = None
    slope = None
    xslope = None
    rslope = None       # rightward slope
    lslope = None       # leftward slope
    toe = None          # structure toe
    h = None            # crest height
    w = None            # crest width
    n = None            # nglob
    m = None            # mglob
    bathy = None        # bathy array
    toedep = None       # depth at toe of structure
    dx = 1              # dx, default 1 (m)
    smoothing = True    # smoothing, default True
    friction = None     # friction coef
    farray = None       # friction array

    ## operational args
    printfric = False
    debug = False

    # parse argv[]
    try:
        opts, _ = getopt.getopt(argv, 'i:o:r:l:x:h:w:', 
        ['json=', 'flat=', 'slope=', 'xslope=', 'nglob=', 
            'mglob=', 'toedep=', 'dx=', 'smoothing', 'frictionfile=', 'friction=',
            'debug'])
    except getopt.GetoptError:
        print("Error: invalid usage")
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in '-i':
            inputfile = arg
        elif opt in '-o':               # TODO: full implementation
            outdir = arg
        elif opt in '--json':
            jsonfile = arg
        elif opt in '--flat':
            flatdepth = float(arg)
        elif opt in '--slope':
            slope = float(arg)
        elif opt == '--xslope':
            xslope = int(arg)
        elif opt == '--frictionfile':
            frictionfile = arg
        elif opt in '--friction':
            friction = float(arg)
        elif opt in '-r':
            rslope = float(arg)
        elif opt in '-l':
            lslope = float(arg)
        elif opt in '-x':
            toe = int(arg)
        elif opt in '-w':
            w = float(arg)
        elif opt in '-h':
            h = float(arg)
        elif opt in '--toedep':
            toedep = float(arg)
        elif opt in '--mglob':
            m = int(arg)
        elif opt in '--nglob':
            n = int(arg)
        # elif opt in '--dx':           # NOT SURE IF NEEDED...
        #     dx = float(arg)
        elif opt in '--debug':
            debug = True

    # parse .json
    if not jsonfile == None:
        ## import json warning
        if not (rslope == None and lslope == None and toe == None \
                and w == None and h == None):
            print("warning: importing JSON, ignoring arguments")

        ## parse json
        with open(jsonfile) as file:
            x = json.loads(file)
            for key in x:
                if key == 'inputfiledepth':
                    inputfile = x[key]
                if key == 'outputdir':
                    outdir = x[key]
                ### TODO: Parse JSON as such above
    
    # establish bathymetry
    ## data
    if not inputfile == None:
        with open(inputfile) as file:
            bathy = np.loadtxt(file)#.reshape((n, m))
            n, m = bathy.shape
    ## flat/slope case
    elif not flatdepth == None:
        if n == None or m == None:
            print("Error: mglob, nglob arguments not found")
            sys.exit()
        bathy = np.full((n, m), flatdepth)
        np.savetxt('test.txt', bathy, fmt='%.6E')
        if not (slope == None or xslope == None):
            bathy[:,xslope:] = np.tile(np.linspace(flatdepth,
                                        flatdepth - slope * (m - xslope), 
                                        num=(m - xslope)), (n, 1))
    else:
        print("Error: invalid or missing bathy arguments")
        sys.exit()

    # establish friction
    if not frictionfile == None:
        try:
            farray = np.full((n, m), float(frictionfile))
        except:
            with open(inputfile) as file:
                farray = np.loadtxt(file)
        if friction == None:
            print('Error: friction coefficient not supplied')
            sys.exit()
        printfric = True
    

    # insert structure
    ## check for input toe depth
    if toedep == None:
        toedep = 0
        for y in bathy[:, toe]:
            toedep += y
        toedep = toedep / bathy[:, toe].size
    ## add structure on depth
    for y in range(n):
        for x in range(toe, toe + int(h / rslope + w + h / lslope)):
            if x < toe + h / lslope:
                if bathy[y, x] > toedep - lslope * (x - toe + 1):
                    bathy[y, x] = toedep - lslope * (x - toe + 1)
            elif x < toe + h / lslope + w - 2:
                if bathy[y, x] > toedep - h:
                    bathy[y, x] = toedep - h
            elif x < toe + h / rslope + w + h / lslope - 2:
                if bathy[y, x] > toedep - rslope * \
                        (h / rslope + w + h / lslope - x + toe - 2):
                    bathy[y, x] = toedep - rslope * \
                     (h / rslope + w + h / lslope - x + toe - 2)
            if printfric:
                farray[y, x - 1] = friction
                
    ## smoothing

    if debug:
        np.savetxt('test.txt', bathy, fmt='%.6E')
    np.savetxt('depth.txt', bathy, fmt='%.6E')
    if printfric:
        np.savetxt('friction.txt', farray, fmt='%.6E')

# main() arg call
if __name__ == '__main__':
    main(sys.argv[1:])