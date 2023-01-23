import tkinter as tk
import time
from datetime import datetime
from tkcalendar import *
import numpy as np
import tracemalloc
import os,psutil

root = tk.Tk()
root.geometry('500x600')
root.title('Study App')
#root.resizable(0,0)
scheduledata = [["5/22/20", "Math Homework"],["5/25/20", "English Test"],["5/1/20", "Kewarganegaraan speech"],["5/16/20", "Data Science Project"]]

list = [["math",100,90,30,20],["english",50,50,60,70],["science",70,30], ["sport",40]]
#def myClick():
   # x = tk.Label(, text= "thanks")
 #   x.pack()
 

def home_page():
    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame, text = "Home Page \nPage:1",font=('Bold',15))
    lb.pack()
    lb1 = tk.Label(home_frame, text = "Welcome to the home page \nClick the button on the left\nto go to different pages",font=('Bold',15))
    lb1.pack()
    home_frame.pack(pady= 20)

def C1(e):
    global word
    global scheduletexts
    scheduletexts = ""
    word = e.get().split()
    if len(word) == 2:
        scheduletexts += word[1]
    if len(word) >2:
        for x in range(1, len(word)):
            scheduletexts+= " "
            scheduletexts+= word[x]
    print (scheduletexts)
    print(word)

def menu_page():
    quote = """"""
    menu_frame = tk.Frame(main_frame)
    lb = tk.Label(menu_frame, text = "Menu Page \nPage:2",font=('Bold',15))
    lb.pack()

    e = tk.Entry(menu_frame, width =50)
    e.pack()
    myButton = tk.Button(menu_frame, text="Click Me!", command= lambda:[text.delete("1.0","end"), C1(e), add_data(word[0], scheduletexts, quote, text)])
    myButton.pack()
    global text
    text = tk.Text(menu_frame, width = 40, height = 6, font = ("Times New Roman",12))
    text.pack()
    text.insert(tk.INSERT,"Table of Scores\n")
    create_data(quote)
    menu_frame.pack(pady= 20)

def add_data(data, number, quote, text):
    if data == "delete":
        print("yesss")
        print(list)
        for x in range (len(list)):
            if list[x][0] == number:
                list[x].pop()
                break

        quote += "Table of Scores\n"
        for x in list:
            for y in x:
                quote +=str(y)+" | "
            quote+= "\n"

        text.insert(tk.INSERT,quote)

        return
    global deff
    deff = True
    text.delete("1.0","end")
    for x in range (len(list)):
        for y in range(len(list[x])):
            if list[x][0] == data:
                deff = False
                print("step 1")
                list[x].append(number)
                break


    if deff == True:
        list.append([data, number])
        deff = False

    print(list)
    quote += "Table of Scores\n"
    for x in list:
        for y in x:
            quote +=str(y)+" | "
        quote+= "\n"

    text.insert(tk.INSERT,quote)

def create_data(quote):
    #print(list)
    for x in list:
        for y in x:
            quote +=str(y)+" | "
        quote+= "\n"

    text.insert(tk.INSERT,quote)

def create_schedule(scheduletext, texts):
    print(scheduledata)
    for x in range(len(scheduledata)):
        scheduletext+=( scheduledata[x][0]+": " )
        for y in range(1, len(scheduledata[x])):
            if y >1:
                scheduletext += ("," + scheduledata[x][y])
            if y == 1:
                scheduletext += scheduledata[x][y]
        scheduletext += "\n"

    texts.insert(tk.INSERT, scheduletext)

def contact_page():
    scheduletext = ""
    contact_frame = tk.Frame(main_frame)
    lb = tk.Label(contact_frame, text = "Schedule Page \nPage:3",font=('Bold',15))
    lb.pack()
    contact_frame.pack(pady= 20)
    e = tk.Entry(contact_frame, width =20)
    e.pack()
    myButton = tk.Button(contact_frame, text="Enter Schedule",command= lambda:[texts.delete("1.0","end"), C1(e),add_date(word[0],scheduletexts), create_schedule(scheduletext, texts)])
    myButton.pack()

    texts = tk.Text(contact_frame, width = 30, height = 6, font = ("Times New Roman",12))
    texts.pack()
    create_schedule(scheduletext, texts)

    my_button2 = tk.Button (contact_frame, text = "Get Date",command=lambda: grab_date(my_label, my_label1, cal,scheduledata))
    my_button2.pack()
    
    cal = Calendar(contact_frame, selectmode = "day", year= 2020, month = 5, day = 22)
    cal.pack()

    my_label = tk.Label(contact_frame, text ="")
    my_label.pack(pady=5)
    my_label1 = tk.Label(contact_frame, text ="")
    my_label1.pack()
    

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    my_labeltime.config(text = "Time: " + hour + ":" + minute + ":"+ second)
    my_labeltime.after(1000,clock)

def about_page():
    about_frame = tk.Frame(main_frame)
    lb = tk.Label(about_frame, text = "About Page \nPage:4\n\n",font=('Bold',15))
    lb.pack()

    rules = tk.Label(about_frame, text = "Menu Page\n"+
    "To add Scores:\nType Lesson + Score\nTo delete Scores:\nType Delete + Lesson\n\n"+
    "Schedule Page\nSchedule List are shown on the box\nTo add Schedules:\n"+
    "Type Schedules + task\nTo delete Schedules:\nType Delete + Schedules\n"+
    "To find what is on the calendar:\nPick a number on the calendar\nPress Get Date", font=('Bold',15) )
    rules.pack()
    about_frame.pack(pady= 20)

def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    menu_indicate.config(bg='#c3c3c3')
    contact_indicate.config(bg='#c3c3c3')
    about_indicate.config(bg='#c3c3c3')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()

def grab_date(my_label, my_label1, cal,scheduledata):
    indicator = False
    text = ""
    my_label.config(text = "Today's Date Is " + cal.get_date())
    print (cal.get_date())
    for x in range(len(scheduledata)):
        if scheduledata[x][0] == cal.get_date():
            for y in range(1, len(scheduledata[x])):
                text += scheduledata[x][y]
                text += "\n"
                indicator = True

        my_label1.config(text = "Today's schedule is "+"\n"+ text)
    if indicator == False:
        my_label1.config(text = "There is no schedule today")


def add_date(date, schedule):
    if (date == "delete"):
        start = time.time()
        print ("yes its delete")
        for x in range(len(scheduledata)):
            if (scheduledata[x][0]==schedule):
                scheduledata.pop(x)
                print(scheduledata)
                end = time.time()
                process = psutil.Process(os.getpid())
                print("The time of execution of above program is :", (end-start) * 10**3, "ms")
                print("Memory usage to run the program :", (process.memory_info().rss) / (1024 * 1024))
                return
            #else: return
    #scheduledata.append([date, schedule])
    """if (date == "delete"):
        ans = findAns(scheduledata, schedule)
        if (ans[0] == -1):
            return
        scheduledata.pop(ans[0])
        return"""

    for x in range (len(scheduledata)):
        if scheduledata[x][0] == date:
            print("step 1")
            scheduledata[x].append(schedule)
            return
    
    scheduledata.append([date, schedule])

def findAns(arr, target):
    #binary search
    row = 0
    col = len(arr[row]) - 1
    while (row < len(arr) and col >= 0):
        if (arr[row][col] == target):
            return [row, col]

    # Target lies in further row
        if (arr[row][col] < target):
            row += 1

    # Target lies in previous column
        else:
            col -= 1

    return [-1, -1]

now = datetime.now()
my_labeltime11 = tk.Label(root, text = "Date: " + str(now.month) + "/"+str(now.day) + "/"+str(now.year), font = ("Helvetica BOLD", 15))
my_labeltime11.pack(side="top", anchor="ne")

my_labeltime = tk.Label(root, text= "", font = ("Helvetica BOLD", 15))
my_labeltime.pack(side="top", anchor="ne")
clock()

options_frame = tk.Frame(root, bg= '#c3c3c3')

home_btn = tk.Button(options_frame, text = 'Home', font = ('Bold',15),
                    fg = '#158aff', bd=0, bg = "#c3c3c3",command =lambda:indicate(home_indicate,home_page))

home_btn.place(x=10, y=50)

home_indicate = tk.Label(options_frame, text = '', bg = '#c3c3c3')
home_indicate.place(x=3, y=50, width = 5, height= 40)

menu_btn = tk.Button(options_frame, text = 'Menu', font = ('Bold',15),
                    fg = '#158aff', bd=0, bg = "#c3c3c3",command =lambda:indicate(menu_indicate, menu_page))

menu_btn.place(x=10, y=100)

menu_indicate = tk.Label(options_frame, text = '', bg = '#c3c3c3')
menu_indicate.place(x=3, y=100, width = 5, height= 40)

contact_btn = tk.Button(options_frame, text = 'Schedule', font = ('Bold',15),
                    fg = '#158aff', bd=0, bg = "#c3c3c3",command =lambda:indicate(contact_indicate,contact_page))

contact_btn.place(x=10, y=150)

contact_indicate = tk.Label(options_frame, text = '', bg = '#c3c3c3')
contact_indicate.place(x=3, y=150, width = 5, height= 40)

about_btn = tk.Button(options_frame, text = 'About', font = ('Bold',15),
                    fg = '#158aff', bd=0, bg = "#c3c3c3",command =lambda:indicate(about_indicate, about_page))

about_btn.place(x=10, y=200)

about_indicate = tk.Label(options_frame, text = '', bg = '#c3c3c3')
about_indicate.place(x=3, y=200, width = 5, height= 40)

options_frame.pack(side = tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=700)

main_frame = tk.Frame(root, highlightbackground = 'black', highlightthickness = 2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=700, width = 500)
home_page()

root.mainloop()