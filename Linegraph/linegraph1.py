# Write a Linegraph 
# linegraph file 
import matplotlib.pyplot as plt
from datetime import datetime as dt 
import matplotlib.dates as mdates
import sys

vers=[]
date=[]
lines=[]

if len(sys.argv) == 1:
    print "Usage: ", sys.argv[0], ": filename" 
    exit(1)

filename=sys.argv[1]
name=filename.split('.')
outfilename=name[0]+'.png'

with open(filename,"r") as f:
    data = f.readlines()

title = 'title is not described in 1st line of file'
for line in data:
    l =  line.split()
    if l[0] == "#":
        title=line.lstrip('# ')
    else:
        vers.append(l[0])
        d = dt.strptime(l[1], "%Y-%m-%d")
        date.append(d)
        lines.append(int(l[2]))
    

plt.plot_date(date, lines, fmt="r-", marker=".", markeredgewidth=0)
plt.plot_date(date, lines, fmt="r-", marker="D", markevery=5 )
for v in range(0, len(lines)):
    if (v % 5) == 0:
        plt.annotate(vers[v], (mdates.date2num(date[v]), lines[v]), 
             xytext=(-20,5), textcoords='offset points' )

plt.title(title)
plt.grid(True)

plt.ylabel("MLines")
locs,labels = plt.yticks()
plt.yticks(locs, map(lambda x: "%g" % x, locs*1e-6))

plt.savefig(outfilename, dpi=300, format='png')
plt.show()

