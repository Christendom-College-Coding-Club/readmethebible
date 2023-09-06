import pyttsx3
import sys

def get_first_number(line):
    first_number = ""
    if ':' not in line:
        return -1

    for i in range(len(line)):
        if line[i].isdigit():
            first_number += line[i]
        if line[i] == ':':
            break
    return -1 if first_number == "" else first_number

def get_chapters(bible, book, first, last, log = ""):
    
    looking_for_book = 1
    looking_for_chapter = 2
    reading_chapter = 3
    
    state = looking_for_book
    
    to_read = ""
    
    with open(bible, "r") as file:
        for line in file:
            line = line.strip()
    
            if state == looking_for_book:
                if book in line and get_first_number(line) == -1:
                    state = looking_for_chapter
    
            elif state == looking_for_chapter:
                first_number = get_first_number(line)
                if int(first_number) == first:
                    state = reading_chapter
                    log += "found chapter " + str(first) + "\n"
                
            if state == reading_chapter:
                first_number = get_first_number(line)
                if int(first_number) > last:
                    log += "finished reading chapter " + str(first) + "\n"
                    break
                else:
                    numberless_line = ''.join([i for i in line if not i.isdigit() and not i == ':'])
                    if numberless_line:
                        to_read += numberless_line
                        to_read += " "

    log += to_read + "\n"
    
    return to_read

def read_to_me(book,start,end,to_read,speed,log = [""]):  
    try:
        engine = pyttsx3.init()
        
        engine.setProperty('rate', speed)
        engine.setProperty('volume', 1)
        
        try:
            log[0] += "saving to file, will close when done" + "\n"
            engine.save_to_file(to_read,f"{book}{start}-{end}.mp3")
        except Exception as e:
            log[0] += str(e) + "\n"
            log[0] += "error saving to file. exiting..." + "\n"
        
        engine.runAndWait()
        log[0] += "save completed" + "\n"
    except Exception as e:
        log[0] += str(e) + "\n"
        log[0] += "error initializing engine. exiting..." + "\n"

def read_me_the_bible(bible,book,first,last,speed):
    print("gathering selection...")
    to_read = get_chapters(bible,book,first,last)
    print("read successful")
    read_to_me(book,first,last,to_read,speed)

if __name__ == "__main__":
    if len(sys.argv) == 5:
        book = sys.argv[1].strip().lower().capitalize()
        first = int(sys.argv[2])
        last = int(sys.argv[3])
        speed = int(sys.argv[4])
    elif len(sys.argv) == 1:
        print("Ctrl+c to Exit")
        book = input("Book: ").strip()
        book = book.lower().capitalize()
        first = int(input("First Chapter: "))
        last = int(input("Last Chapter: "))
        print("150-200 is a good speed")
        speed = int(input("Speed: "))
    else:
        print("Usage: readmethebible or readmethebible <book> <first chapter> <last chapter> <speed>")
        print("Example: python3 bible_reader.py Genesis 1 50 150")
        print("Example: python3 bible_reader.py")
        sys.exit(1)
    
    read_me_the_bible("bible.txt",book,first,last,speed)
