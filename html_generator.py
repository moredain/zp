
#coding: utf8

import sys
import os



def todohtml(shtatx):
    temphtml = open("bootstrap_mod/index.html", "r")
    temphtmlstr = temphtml.read()
    temphtml.close()
    print(type(temphtmlstr))

    for i in shtatx:
        temphtmllist = temphtmlstr.replace("###",'hren1' )
        repl =shtatx[i]
        temphtmllist = temphtmlstr.replace("###", repl)
        print(temphtmllist)

shtat = ['hren1','hren2','hren3','hren4','hren5','hren6','hren7','hren8','hren9','hren10','hren11','hren12','hren13',
         'hren14','hren15','hren16','hren17',]

todohtml(shtat)
