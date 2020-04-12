from tkinter import *
from twscraper import *
from scraper import *
from youtube import *

WINDOW_SIZE=800

def click(e, pg, flag):
    entry=e.get()
    pgcount=int(pg.get()) or 1
    if not entry.strip():
        #print("Empty String")
        msg=Tk()
        msg.title("Errors")
        msg.bind('<Escape>', lambda event: msg.destroy())
    else:
        #print(entry)
        if (flag==0):
            if '#' not in entry:
                entry="#"+entry
    
    if flag==0:        
        setup(entry, pgcount)
        msg=Tk()
        msg.title("Operation Completed")
        box = Button(msg,text = "OK", bg="snow", command=(lambda: msg.destroy()), bd=3, font=('Franklin Gothic',12, 'bold'))
    elif flag==1:
        start(entry, pgcount)
        
def trigger(e):
    entry=e.get()
    if not entry.strip():
        #print("Empty String")
        msg=Tk()
        msg.title("Errors")
        msg.bind('<Escape>', lambda event: msg.destroy())
    #else:
        #print(entry)
            
    driver(entry)
        
class Menu(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.canvas = Canvas(
            height=800, width=800,
            bg='#00022D')
        
        self.canvas.pack()
        self.bind('<x>', lambda event: self.destroy())
        self.title_screen()
        self.buttoncreate()
        
    def call_result(label_result, n1):  
        keyword1 = (n1.get())   
        labelResult.config(text="Result = %d" % keyword1)  
        return
    
    def title_screen(self):
        # placeholder title screen
            self.canvas.delete('all') #just in case 
            #self.img = PhotoImage(file="mhp.png")   
            #self.canvas.create_image(WINDOW_SIZE/2,WINDOW_SIZE/2, anchor=CENTER, image=self.img)    
            #self.canvas.image = self.img  
            self.canvas.create_rectangle(
                int(WINDOW_SIZE/20), int(WINDOW_SIZE/20),
                int(WINDOW_SIZE*19/20), int(WINDOW_SIZE*19/20),
                width=int(WINDOW_SIZE/50),
                outline='snow')
            
            '''self.canvas.create_text(
                WINDOW_SIZE/2,
                WINDOW_SIZE/5.5,
                text='State Intelligence Dept.', fill='white',
                font=('Franklin Gothic', int(-WINDOW_SIZE/14), 'bold'))'''
            
            self.canvas.create_text(
                WINDOW_SIZE/2,
                WINDOW_SIZE/1.2,
                text='Social Media Analysis Tool', fill='white',
                font=('Franklin Gothic', int(-WINDOW_SIZE/16), 'bold'))
            
            self.canvas.create_text(
                WINDOW_SIZE/1.15,
                WINDOW_SIZE/1.02,
                text='Copy: \u00A9DPS 2020', fill='white',
                font=('Franklin Gothic', int(-WINDOW_SIZE/64), 'bold'))
            
            self.canvas.create_text(
                WINDOW_SIZE/12,
                WINDOW_SIZE/1.02,
                text='Version: 0.03.01', fill='white',
                font=('Franklin Gothic', int(-WINDOW_SIZE/64), 'bold'))
    
    def ytform(self):
        win=Tk()
        win.title("Keyword Form")
        win.geometry("250x150")
        win.configure(bg='#00022D')
        win.bind('<Escape>', lambda event: win.destroy())
        keywords = Label(win, text = "Keyword(s)", fg="snow", bg='#00022D', font=('Franklin Gothic', 12, 'bold')).grid(row = 0, column = 0)  
        keyword = Entry(win)
        keyword.grid(row = 0, column = 1) 
        win.bind("<Return>", (lambda: trigger(keyword)))
        submit = Button(win,text = "Submit", bg="snow", command=(lambda: [trigger(keyword), win.destroy()]), bd=3, font=('Franklin Gothic',12, 'bold') ).grid(row = 2, column = 1)
    
    def fbform(self):
        win=Tk()
        win.title("Page Form")
        win.geometry("250x120")
        win.configure(bg='#00022D')
        win.bind('<Escape>', lambda event: win.destroy())
        namepages = Label(win, text = "FB Page", fg="snow", bg='#00022D', font=('Franklin Gothic', 12, 'bold')).grid(row = 0, column = 0)  
        pgname = Entry(win)
        pgname.grid(row = 0, column = 1) 
        pages = Label(win, text = "No. of Pages", fg="snow", bg='#00022D', font=('Franklin Gothic', 12, 'bold')).grid(row = 2, column = 0) 
        pgcount = Entry(win)
        pgcount.grid(row = 2, column = 1)
        win.bind("<Return>", (lambda x: click(pgname, pgcount, 1)))
        flag=1
        submit = Button(win,text = "Submit", bg="snow", command=(lambda: click(pgname, pgcount, flag)), bd=3, font=('Franklin Gothic',12, 'bold') ).grid(row = 3, column = 1)
        
    def twform(self):
        win=Tk()
        win.title("Hashtag Form")
        win.geometry("250x120")
        win.configure(bg='#00022D')
        win.bind('<Escape>', lambda event: win.destroy())
        keywords = Label(win, text = "Keyword(s)", fg="snow", bg='#00022D', font=('Franklin Gothic', 12, 'bold')).grid(row = 0, column = 0)  
        hashes = Entry(win)
        hashes.grid(row = 0, column = 1)
        pages = Label(win, text = "No. of Pages", fg="snow", bg='#00022D', font=('Franklin Gothic', 12, 'bold')).grid(row = 2, column = 0)  
        pgcount = Entry(win)
        pgcount.grid(row = 2, column = 1)
        win.bind("<Return>", (lambda x: click(hashes, pgcount, 0)))
        flag=0
        confirm = Button(win,text = "Confirm", bg="snow", command=(lambda: click(hashes, pgcount, flag)), bd=3, font=('Franklin Gothic',12, 'bold') ).grid(row = 3, column = 1)
        
    def buttoncreate(self):    
        self.button2 = Button(text = "Youtube(Alpha)", bg="white", fg = "midnight blue", bd=3, command=self.ytform, height=2, width=21, font=('Franklin Gothic',int(-WINDOW_SIZE/40), 'bold'))  
        self.button2.pack( side = LEFT )  
        self.button3 = Button(text = "Facebook(Alpha)", bg="white", fg = "midnight blue", bd=3, command=self.fbform, height=2, width=21, font=('Franklin Gothic',int(-WINDOW_SIZE/40), 'bold'))  
        self.button3.pack( side = RIGHT )  
        self.button1 = Button(text = "Twitter", bg="white", fg = "midnight blue", bd=3, command=self.twform, height=2, width=23, font=('Franklin Gothic',int(-WINDOW_SIZE/40), 'bold'))  
        self.button1.pack( side =TOP)
            
            
def main_menu():
    root=Menu()
    root.resizable(0,0)
    root.title("SMA Tool")
    root.configure(bg='#00022D')
    root.mainloop()    
    
main_menu()