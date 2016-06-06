
#coding: utf8

import sys
import os



def todohtml(shtatx):
    temphtml = open("bootstrap_mod/index.html", "r")
    temphtmlstr = temphtml.read()
    temphtml.close()
    print(type(temphtmlstr))
#    print(temphtmlstr)
    print(shtatx[2])
    for i in shtatx:
#        temphtmllist = temphtmlstr.replace("###",'hren1' )
#        print(temphtmllist)
        i = 0
        replx =shtatx[i]
        repl = replx+str(i)
        print(repl)
        temphtmllist = temphtmlstr.replace("###", repl)
        print(temphtmllist)
        i= i+1

shtat = ['hren1','hren2','hren3','hren4','hren5','hren6','hren7','hren8','hren9','hren10','hren11','hren12','hren13',
         'hren14','hren15','hren16','hren17',]

todohtml(shtat)
