
#coding: utf8

import sys
import os



def todohtml(shtatx, username):
    temphtml = open("bootstrap_mod/index.html", "r")
    temphtmlstr = temphtml.read()

    temphtml.close()
    search = temphtmlstr.find("###")
    if search == -1:
        print("Error. String of replace don't found")
    else:
        mylistlen = len(shtatx)
        print(shtatx)
        spli = temphtmlstr.split("###")
        i = 0

        while i < mylistlen:
            spli.insert(1 + i * 2, shtatx[i])
            i = i + 1

        s=""
        fullhtml =s.join(spli)
        htmlname = "bootstrap_mod/"+username+".html"
        fullhtml_file_write = open(htmlname, "w")
        fullhtml_file_write.write(fullhtml)
        fullhtml_file_write.close()



    return  "HTML generated"

shtat = ['hren1','hren2','hren3','hren4','hren5','hren6','hren7','hren8','hren9','hren10','hren11','hren12','hren13',
         'hren14','hren15','hren16','hren17',]


todohtml(shtat,'gopnik')