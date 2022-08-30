import numpy as np
from matplotlib import pyplot as plt
import os

os.system('python3 rubblebathy.py --debug --flat 8 --mglob 50 --nglob 3 -l 0.5 -r 0.5 -x 20 -h 4 -w 5')
data = np.loadtxt("test.txt")

plt.figure()
plt.plot(range(1, 51), -data[1,])
plt.savefig("test1")

os.system('python3 rubblebathy.py --debug --flat 8 --mglob 100 --nglob 3 -l 0.5 -r 0.2 -x 20 -h 8 -w 8')
data = np.loadtxt("test.txt")

plt.figure()
plt.plot(range(100), -data[2,])
plt.savefig("test2")

os.system('python3 rubblebathy.py --debug --flat 8 --mglob 200 --nglob 3 -l 0.5 -r 0.13 -x 20 -h 8 -w 8')
data = np.loadtxt("test.txt")

plt.figure()
plt.plot(range(200), -data[2,])
plt.savefig("test3")

os.system('python3 rubblebathy.py --debug --flat 8 --slope 0.05 --xslope 10 --mglob 50 --nglob 3 -l 0.5 -r 0.2 -x 20 -h 4 -w 4')
data = np.loadtxt("test.txt")

plt.figure()
plt.plot(range(50), -data[2,])
plt.savefig("test4")

os.system('python3 rubblebathy.py --debug -i depth_levee.txt -l 0.5 -r 0.2 -x 20 -h 4 -w 4')
data = np.loadtxt("test.txt")

plt.figure()
plt.plot(range(500), -data[2,])
plt.savefig("test5")

os.system('python3 rubblebathy.py --debug --frictionfile 0.1 --friction 0.5 --flat 8 --mglob 50 --nglob 3 -l 0.5 -r 0.5 -x 20 -h 4 -w 5')
data = np.loadtxt("test.txt")

plt.figure()
plt.plot(range(1, 51), -data[1,])
plt.savefig("test6")

data = np.loadtxt("samplebath.txt")

plt.figure()
plt.plot(range(300), -data[2,])
plt.savefig("samplebathy.png")

os.system('python3 rubblebathy.py --debug -i samplebath.txt -l 0.03 -r 0.1 -x 100 -h 2 -w 30')
data = np.loadtxt("test.txt")

plt.figure()
plt.plot(range(300), -data[1,])
plt.savefig("test7")