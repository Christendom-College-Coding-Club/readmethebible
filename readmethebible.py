import pyttsx3

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

def get_chapters(bible, book, first, last):
    
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
                    print("found ",first_number)
                
            if state == reading_chapter:
                first_number = get_first_number(line)
                if int(first_number) > last:
                    print("found ",first_number)
                    break
                else:
                    numberless_line = ''.join([i for i in line if not i.isdigit() and not i == ':'])
                    if numberless_line:
                        to_read += numberless_line
                        to_read += " "
    
    return to_read

def read_to_me(book,start,end,to_read,speed):  
    try:
        engine = pyttsx3.init()
        
        engine.setProperty('rate', speed)
        engine.setProperty('volume', 1)
        
        try:
            print("saving to file, will close when done")
            print("to read: ",to_read)
            engine.save_to_file(to_read,f"{book}{start}-{end}.mp3")
        except Exception as e:
            print(e)
            print("error saving to file. exiting...")
        
        engine.runAndWait()
        print("save completed")
    except Exception as e:
        print(e)
        print("Error initializing pyttsx3. Exiting...")

def read_me_the_bible(bible,book,first,last,speed):
    print("gathering selection...")
    to_read = get_chapters(bible,book,first,last)
    print("read successful")
    read_to_me(book,first,last,to_read,speed)

print("Ctrl+c to Exit")
book = input("Book: ").strip()
book = book.lower().capitalize()
first = int(input("First Chapter: "))
last = int(input("Last Chapter: "))
print("150-200 is a good speed")
speed = int(input("Speed: "))
read_me_the_bible("bible.txt",book,first,last,speed)
