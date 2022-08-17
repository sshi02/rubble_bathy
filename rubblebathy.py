import numpy as np
import sys, getopt, json

class RubbleBathy:
    def __init__(self, filename) -> None:
        with open(filename) as file:
            self.bathy = np.loadtxt(file)

    def save(self, filename):
        np.savetxt(filename, self.bathy, fmt='%.6E')

    def addrubble(self, seaslope, leeslope, x_i, h, w):
        pass


def main(argv):
    # init vars
    inputfile = None
    outdir = None
    frictionfile = None
    jsonfile = None
    flatdepth = None
    slope = None
    xslope = None
    cslope = None       # seaward slope
    lslope = None       # leeward slope
    toe = None          # structure toe
    h = None            # crest height
    w = None            # crest width
    n = None            # nglob
    m = None            # mglob
    bathy = None        # bathy array

    # parse argv[]
    try:
        opts, _ = getopt.getopt(argv, 'i:o:f:c:l:x:h:w:', 
        ['json=', 'flat=', 'slope=', 'xslope=', 'nglob=', 'mglob='])
    except getopt.GetoptError:
        print("Error: invalid usage")
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in '-i':
            inputfile = arg
        elif opt in '-o':
            outdir = arg
        elif opt in '--json':
            jsonfile = arg
        elif opt in '--flat':
            flatdepth = float(arg)
        elif opt in '--slope':
            slope = float(arg)
        elif opt in '--xslope':
            xslope = int(arg)
        elif opt in '-f':
            frictionfile = arg
        elif opt in '-c':
            cslope = float(arg)
        elif opt in 'l':
            lslope = float(arg)
        elif opt in '-x':
            toe = int(arg)
        elif opt in '-w':
            w = float(arg)
        elif opt in '-h':
            h = float(arg)
        elif opt in '--mglob':
            m = int(arg)
        elif opt in '--nglob':
            n = int(arg)

    # parse .json
    if not jsonfile == None:
        ## import json warning
        if not (cslope == None and lslope == None and toe == None \
                and w == None and h == None):
            print("warning: importing JSON, ignoring arguments")

        ## parse json
        with open(jsonfile) as file:
            x = json.loads(file)
            for key in x:
                pass            # TODO
    
    # establish bathymetry
    ## data
    if not inputfile == None:
        with open(inputfile) as file:
            bathy = np.loadtxt(file)
            m, n = bathy.shape
    elif not flatdepth == None:
        if n == None or m == None:
            print("Error: mglob, nglob arguments not found")
            sys.exit()
        bathy = np.full((n, m), flatdepth)
        if not (slope == None or xslope == None):
            bathy[:,xslope:] = np.tile(np.linspace(flatdepth,
                                                flatdepth - slope * (m - xslope), 
                                            num=(m - xslope)), (n, 1))
    else:
        print("Error: invalid or missing bathy arguments")
        sys.exit()

    np.savetxt('test.txt', bathy, fmt='%.6E')

if __name__ == '__main__':
    main(sys.argv[1:])