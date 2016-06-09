
#coding: utf8

import sys
import os



def todohtml(shtatx):
    temphtml = open("bootstrap_mod/index.html", "r")
    temphtmlstr = temphtml.read()
    lenstr = len(temphtmlstr)
    print(lenstr)
    temphtml.close()
    j = 0
    print(type(j))
    replx = shtatx[int(j)]
    print("replx = " + replx)
    str ="###"

    temphtmllist = temphtmlstr.find(str, 0,lenstr)
    print(temphtmllist)



shtat = ['hren1','hren2','hren3','hren4','hren5','hren6','hren7','hren8','hren9','hren10','hren11','hren12','hren13',
         'hren14','hren15','hren16','hren17',]
shtatcopy =list.copy(shtat)
print(shtatcopy)

todohtml(shtat)
