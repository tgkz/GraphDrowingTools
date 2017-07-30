#!/usr/bin/python
# Write a pie chart
# Written by Tsugikazu Shibata Copyright(c) 2017

import numpy as np
import matplotlib.pyplot as plt
import sys

def printusage():
    print "Usage: ", sys.argv[0], "[-t 'title string'] filename" 
    exit(1)
    
def lowfilter(domain, percent):
    # select data over LOWLIMIT, lower data will be gathered as Others
    data=[]
    label=[]
    LOWLIMIT=1.0     # less than this number becomes "OTHERS"
    didx = 0
    totalothers=0.0
    nothers=0
    for v in percent:
        if float(v) < LOWLIMIT:
            totalothers=totalothers+float(v)
            nothers= nothers + 1
        else:
            label.append(domain[didx])
            data.append(percent[didx])
            print domain[didx], ' ', v
            didx = didx + 1

    if nothers > 1:  # we found lower data add "Others item"
        label.append("Others")
        data.append(str(totalothers))
        print nothers, 'items were gathered as Others, Total percents were', totalothers
        
    return label, data


domains=[]
percent=[]

if len(sys.argv) == 1:
    printusage()
    exit(1)
filename=sys.argv[1]

title=''
if sys.argv[1] == "-t":
    if len(sys.argv) != 4:
        printusage()
    title=sys.argv[2]
    filename=sys.argv[3]

name=filename.split('.')
outfilename=name[0]+'.png'

with open(filename,"r") as f:
    data = f.readlines()
# we guess datafile is consits of "domain ncommiter ncommits percent"
# we will pick domain and percent

for line in data:
    l =  line.split()
    if l[0] != "#": # line start from "#" is comment 
        domains.append(l[0])
        percent.append(l[3])

(label, data)=lowfilter(domains, percent)

# set window title
fig=plt.figure(0)
figuretitle='PieChart_'+outfilename
fig.canvas.set_window_title(figuretitle)

# write a pie chart
plt.pie(data, counterclock=False, labels=label, startangle=90,autopct="%1.1f%%")
plt.axis('equal')
# put a title 
plt.title(title)

#plt.savefig(outfilename, dpi=300, format='png')
plt.show()

