#!/usr/bin/python3
gbl_name = "Mark Munyao Mutua"

def change_name():
    global gbl_name
    gbl_name = "Sammy"

change_name()
print(gbl_name)
