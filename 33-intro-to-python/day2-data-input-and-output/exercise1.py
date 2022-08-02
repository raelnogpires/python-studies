# create a program that receive a name
# and prints the name vertically in inverted stairs.
# example:
# RAEL
# RAE
# RA
# R

def invertedNameStairCase(name):
    nameLen = len(name)
    for i in range(nameLen, 0, -1):
        print(name[:i])


invertedNameStairCase("RAEL")
