import readmethebible
import os

def shortSelectionWorks():
    filename = "Genesis1-1.mp3"
    log = ""
    internalLog = [""]
    shortSelection = readmethebible.get_chapters("bible.txt","Genesis",1,1)
    readmethebible.read_to_me("Genesis",1,1,shortSelection,200,internalLog)
    size = os.path.getsize(filename)
    if size > 1000000:
        os.remove(filename)
        return True
    else:
        log += "internalLog: " + internalLog[0] + "\n"
        log += "size: " + str(size) + "\n"
        log += "shortSelectionWorks failed\n"
        os.remove(filename)
        print(log)
        return False


def longSelectionWorks():
    filename = "Genesis1-50.mp3"
    log = ""
    internalLog = [""]
    longSelection = readmethebible.get_chapters("bible.txt","Genesis",1,50)
    readmethebible.read_to_me("Genesis",1,50,longSelection,200,internalLog)
    size = os.path.getsize(filename)
    if size > 1000000:
        os.remove(filename)
        return True
    else:
        log += "internalLog: " + internalLog[0] + "\n"
        log += "size: " + str(size) + "\n"
        log += "longSelectionWorks failed\n"
        os.remove(filename)
        print(log)
        return False

print("\n\n")
if shortSelectionWorks():
    print("shortSelectionWorks passed", end="\n\n")
if longSelectionWorks():
    print("longSelectionWorks passed", end="\n\n")
