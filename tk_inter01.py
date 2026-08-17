import tkinter as tk
from tkinter import DoubleVar, Label, Menu, StringVar, Text, font 
from tkinter import ttk
#from profiling.tracing import label #from tkinter import * can also be use 

win = tk.Tk() #win = Tk() can also be used
win.title("My Window") # Set the title of the window
#win.iconbitmap("icon.ico") # Set the icon of the window(leaf,left most) the image should be in .ico format
win.attributes("-alpha", 1) # Set the transparency of the window in btw[0,1]
win.config(bg="lightblue") # Set the background color of the window
            # we can also use color code instead

win.geometry("400x300") # Set the size of the window
                        # win.geometry("400x300+100+100") # Set the size and position of the window
''' width=300, height=200

    sys_width=win.winfo_screenwidth()
    sys_height=win.winfo_screenheight()
    
    c_x=int(sys_width/2-width/2)
    c_y=int(sys_height/2-height/2)
        
    win.geometry(f"{width}x{height}+{c_x}+{c_y}")'''   #by this we can make the UI at the center of the screen
win.minsize(100,100) #min size of window
#win.maxsize(800,800) #max size of window
win.resizable(True, True) # Set whether the window can be resized (width, height)
                          # win.resizable(False, False) # Set whether the window can be resized (width, height)                        
lab= tk.Label (win,text="Hello World",font=("Arial", 30),bg="lightgreen",fg="black") # Create a label widget
lab.pack() # Pack the label widget
           # lab.place(x=100,y=100) # Place the label widget at a specific position
'''           
#lab.pack(ipadx=10,ipady=10,side="bottom") # Pack the listbox widget with internal padding
#lab2= tk.Label (win,text="whats up?",font=("Arial", 20),bg="lightgreen",fg="black")
#lab2.grid(row=2,column=0,x=100,y=100)  # Place the label widget in a grid layout
#lab2.place(x=100,y=100) # Place the label widget at a specific position
#lab.place(height=100,width=100) # Set the size of the label widget(box)
'''

var= tk.StringVar(win,value="www.linkedin.com/in/sujal-chand-333b3a427") # Create a StringVar to hold the text of the label
print(var.get()) # Get the value of the StringVar
var.set("wow") # Set the value of the StringVar
var1=tk.IntVar(win,value=10.000001,name="var1") # Create a IntVar to hold the text of the label
            # getvar() and setvar() method were only in use when the name is given to the variable
print(var1.get()) # Get the value of the IntVar
var2=tk.BooleanVar(win,value=True) # Create a BooleanVar to hold the text of the label 
print(var2.get()) # Get the value of the BooleanVar
var3=tk.DoubleVar(win,value=10.000005) # Create a DoubleVar to hold the text of the label
print(var3.get()) # Get the value of the DoubleVar

#lb1=tk.Label(win,textvariable=var,text="arrey",font=("Arial", 30),bg="lightgreen",fg="black") # Create a label widget with textvariable
#lb1.place(x=200,y=1500) # Place the label widget at a specific position

lb2=tk.Label(win,textvariable=var1,text="arrey",font=("Arial", 30),cursor="hand2",relief="sunken",justify=tk.LEFT) # Create/chsnge cursor when mouse is over the widget 
                                                                                                                   # Create/change the shape of the box
                                                                                                                   # Create/change the alignment of the text in the box
lb2.place(x=200,y=150) # Place the label widget at a specific position

'''
entry=input("enter anything : ") # Get input from the user
var=tk.StringVar()
lb3=tk.Label(win,text="Hey",font=("Arial", 30),textvariable=var2,underline=0) # Create a label widget with textvariable
                                                                              # Create/change the underline of the text in the box
var.set(entry) # Set the value of the StringVar
lb3.place(x=200,y=200) # Place the label widget at a specific position
'''

"""
photo=PhotoImage(file="demo.png") # Create a PhotoImage object
lb4=tk.Label(win,image=photo,bg="lightblue") # Create a label widget with image
lb.place(x=200,y=250) # Place the label widget at a specific position
"""

lb5=tk.LabelFrame(win,text="Hii! This is Orange",font=("Arial", 15),bg="orange",fg="black",labelanchor="nw") # Create a label widget with textvariable
lb5.place(x=0,y=0,height=100,width=625) # Place the label widget at a specific position and set the size of the label widget(box)

def on_click():
    bt1.config(text="Button clicked!") # Change the text of the label widget when the button is clicked
bt1=tk.Button(win,text="ON",font=30,fg="green",bg="lightgray",cursor="hand2",command=on_click) # Create a button widget
                                                                             #bt1.config(command=on_click) # Bind the click event to the function
bt1.place(x=200,y=350) # Place the button widget at a specific position

# Checkbutton widget
check_button=tk.Checkbutton(win,text="Check me!",font=30,fg="green",bg="lightgray",cursor="hand2") # Create a checkbutton widget
check_button.place(x=200,y=400) # Place the checkbutton widget at a specifict

# Radiobutton widget
radio_button1=tk.Radiobutton(win,text="Option 1",font=30,fg="green",bg="lightgray",cursor="hand2",value="1") # Create a radiobutton widget
radio_button1.place(x=200,y=450) # Place the radiobutton widget at a specific position
radio_button2=tk.Radiobutton(win,text="Option 2",font=30,fg="green",bg="lightgray",cursor="hand2",value="2") # Create a radiobutton widget
radio_button2.place(x=200,y=500) # Place the radiobutton widget at a specific position
'''
def ok():
    lb.config(text="You selected: " + var.get())  # Change the text of the label widget when the button is clicked
list_1=("Python","Java","C++","C#","JavaScript")  # Create a list of options
var=tk.StringVar()
for i in list_1:
    radio_button3=tk.Radiobutton(win,text=i,font=30,fg="green",bg="lightgray",cursor="hand2",value=i,variable=var,command=ok)  # Create a radiobutton widget
    radio_button3.pack(fill="x")  # Place the radiobutton widget
lb=Label(win,text="You selected: ",font=30,fg="green",bg="lightgray")  # Create a label widget
lb.pack()  # Place the label widget 
bt01=tk.Button(win,text="OK",font=30,fg="green",bg="lightgray",cursor="hand2",command=ok)  # Create a button widget
bt01.pack()  # Place the button widget   
'''

# Menu button widget
menu_button1=tk.Menubutton(win,text="file",font=30,fg="green",bg="lightgray",cursor="hand2") # Create a menubutton widget
menu_button1.pack() # Place the menubutton widget
menu_button1.menu=tk.Menu(menu_button1,tearoff=0) # Create a menu for the menubutton widget,tearoff help us to make the wedge stuck in one place
menu_button1["menu"]=menu_button1.menu
menu_button1.menu.add_command(label="New",command=lambda:print("New file")) # Add a command to the menu
menu_button1.menu.add_command(label="Open",command=lambda:print("Open file")) # Add a command to the menu
menu_button1.menu.add_command(label="Save",command=lambda:print("Save file")) # Add a command to the menu
menu_button1.pack() # Place the menubutton widget

Main_maenu=Menu(win) # Create a main menu
#File menu
f_menu=Menu(Main_maenu,tearoff=0) # Create a file menu
f_menu.add_command(label="New FIle")
f_menu.add_command(label="Open FIle")
f_menu.add_command(label="Save FIle")
win.config(menu=Main_maenu) # Set the main menu of the window
Main_maenu.add_cascade(label="File",menu=f_menu) # Add the file menu to the main menu with help of add_cascade method
#Edit menu
f_menu1=Menu(Main_maenu,tearoff=0) # Create a file menu
f_menu1.add_command(label="Cut")
f_menu1.add_command(label="Copy")
f_menu1.add_command(label="Paste")
f_menu1.add_separator() # Add a separator to the menu
#Sub_Menu
sub_menu=Menu(f_menu1,tearoff=0) # Create a sub menu
sub_menu.add_command(label="Sub Menu 1")
sub_menu.add_command(label="Sub Menu 2")
f_menu1.add_cascade(label="Sub Menu",menu=sub_menu) # Add the sub menu to the edit menu
f_menu1.add_separator() # Add a separator
f_menu1.add_command(label="Delete")
f_menu1.add_command(label="Select All")
f_menu1.add_command(label="Undo")
win.config(menu=Main_maenu) # Set the main menu of the window
Main_maenu.add_cascade(label="Edit",menu=f_menu1) # Add the edit menu to the main menu

# Entry Box Widget
def on_enter():
    label4.config(text=var.get()) # Change the text of the label widget when the button is clicked

label3=Label(win,text="Email",font="Arial 15",bg="lightblue",fg="black") # Create a label widget
label3.place(x=0,y=100) # Place the label widget at a specific position
var=StringVar()
entry1=tk.Entry(win,textvariable=var,font="Arial 15",bg="lightgray",fg="black",show="*")  # Create an entry widget
entry1.place(x=0,y=130) # Place the entry widget at a specific position

button1=tk.Button(win,text="Submit",font="Arial 15",bg="lightgray",fg="black",cursor="hand2",command=on_enter) # Create a button widget
button1.place(x=0,y=180,width=225,height=30) # Place the button widget at a specific position

label4=Label(win,text="",font="Arial 15",bg="lightblue",fg="black") # Create a label widget
label4.place(x=0,y=250) # Place the label widget at a specific position

# Text Box Widget
def text_box_action():
    label6.config(text=text_1.get("1.0", "end-1c")) # Change the text of the label widget when the button is clicked
text_1=Text(win,font="Arial 15",bg="lightgray",fg="black") # Create a text widget
text_1.place(x=1240,y=0,width=225,height=200) # Place
label6=Label(win,text="Text Box",font="Arial 15",bg="lightblue",fg="black") # Create a label widget
label6.place(x=1240,y=300) # Place the label widget at a specific position
button2=tk.Button(win,text="Submit",font="Arial 15",bg="lightgray",fg="black",cursor="hand2",command=text_box_action) # Create a button widget
button2.place(x=1240,y=450,width=225,height=30) # Place the button widget at a specific position

# Seperator Widget
label7=Label(win,text="Python",font="30",bg="lightblue",fg="black") # Create a label widget
label7.pack()
separator1=ttk.Separator(win,orient="horizontal") # Create a separator widget
separator1.pack(fill="x") # Place the separator widget at a specific position
label8=Label(win,text="Java",font="30",bg="lightblue",fg="black") # Create a label widget 
label8.pack()

# Spinbox Widget
spin_box1=ttk.Spinbox(win,from_=0,to=10,textvariable=var,style="Custom.TSpinbox") # Create a spinbox widget
spin_box1.place(x=1240,y=480,width=225,height=30) # Place the spinbox widget at a specific position

# Scale Widget
def scale_action(p):
    p=str(var3.get()) # Get the value of the scale widget
    label9.config(text=p) # Change the text of the label widget when the button is clicked
var3=DoubleVar()
scale1=ttk.Scale(win,from_=0,to=100,orient="vertical",variable=var3,command=scale_action) # Create a scale widget
scale1.place(x=1240,y=520,width=30,height=200) # Place the scale widget at a specific position
label9=Label(win,text="Scale Value: " + str(var3.get()),font="30",bg="lightblue",fg="black") # Create a label widget
label9.place(x=1300,y=560) # Place the label widget at a specific position

# Scrollbar Widget
text2=Text(win,font="30",bg="lightgray",fg="black") # Create a text widget
text2.place(x=0,y=400,width=180,height=200) # Place the text widget at a specific position
scroll_bar1=ttk.Scrollbar(win,orient="vertical",command=text2.yview) # Create a scrollbar widget
scroll_bar1.place(x=180,y=400,width=25,height=200) # Place the scrollbar widget at a specific position
text2.config(yscrollcommand=scroll_bar1.set) # Link the scrollbar to the text widget

# Combobox Widget
list_2=["Python","Java","C++","C#","JavaScript"] # Create a list of options
var4=StringVar()
combo_box1=ttk.Combobox(win,values=list_2,textvariable=var4) # Create a combobox widget
combo_box1.place(x=250,y=120,width=225,height=30) # Place the combobox widget at a specific position
combo_box1.set("Select a language") # Set the default value of the combobox widget

# NoteBook Widget
notebook1=ttk.Notebook(win) # Create a notebook widget
notebook1.place(x=500,y=150,width=400,height=100) # Place the notebook widget at a specific position 
frame1=ttk.Frame(notebook1) # Create a frame widget
frame1.pack(fill="both",expand=True) # Place the frame widget at a specific position
label_farme1=Label(frame1,text="enter your name: ",font="30",bg="lightblue",fg="black") # Create a label widget
label_farme1.pack() # Place the label widget at a specific position
entry_frame1=ttk.Entry(frame1) # Create an entry widget
entry_frame1.pack() # Place the entry widget at a specific position
frame2=ttk.Frame(notebook1) # Create a frame widget 
frame2.pack(fill="both",expand=True) # Place the frame widget at a specific position
label_farme2=Label(frame2,text="This is Frame 2",font="30",bg="lightblue",fg="black") # Create a label widget
label_farme2.pack() # Place the label widget at a specific position
notebook1.add(frame1,text="Frame 1") # Add the frame widget to the notebook widget
notebook1.add(frame2,text="Frame 2") # Add the frame widget to the notebook widget

# Message Box Widget
from tkinter.messagebox import showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def test():
    showinfo("Information", "I said! This is an information message box") # Show an information message box
    showwarning("Warning", "This is a warning ") # Show a warning message box
    showerror("Error", "This is an error") # Show an error message box
    askquestion("Question", "are you sure?") # Show a question message box
    askokcancel("OK/Cancel", "Do you want to continue?") # Show an OK/Cancel message box
    askyesno("Yes/No", "Do you want to continue?") # Show a Yes/No message box

button3=tk.Button(win,text="Information Message Box",font="40",bg="lightgray",fg="black",cursor="hand2",command=test) # Create a button widget
button3.place(x=900,y=000,width=270,height=40) # Place the button widget at a specific position

# Frame Widget
style=ttk.Style() # Create a style object
frame01=ttk.Frame(win) # Create a frame widget
style.configure("Gray.TFrame", background="lightgray")
frame01 = ttk.Frame(win, style="Gray.TFrame")
frame01.place(x=900,y=50,width=270,height=200) # Place this
label10=Label(win,text="Scale Value: ",font="30",fg="black") # Create a label widget
label10.place(x=900,y=50)
# If a label coordinates stands outside the given frame then it will not apear on the window

# Toplevel (new window)
def new_window01():
    tp=tk.Toplevel(win) # create new window inside a window
    tp.title("New window 01")
    tp.config(bg="lightgrey")
    label11=Label(tp,text="Welcome to new window")
    label11.place(x=0,y=0)
    tp.mainloop()
button4=tk.Button(win,text="New Window",font="30",command=new_window01) # create a button to open new window
button4.place(x=0,y=230)

# Canvas
canvas_1=tk.Canvas(win,bg="lightgreen") # creating canvas in win
canvas_1.place(x=0,y=270,height=30,width=30)
 #           x0 y0 x1  y1
coordinates01=0,0,100,100
coordinates02=100,0,0,100
line01=canvas_1.create_line(coordinates01,fill="Blue") # creating a line with given coordinates
line02=canvas_1.create_line(coordinates02,fill="Blue")
# corrdinates of lines are according to the canvas not according to window.

canvas_2=tk.Canvas(win,bg="lightgreen") # creating canvas in win
canvas_2.place(x=35,y=270,height=50,width=50)
 #           x0 y0 x1  y1
coordinates03=70,70,100,100
arc01=canvas_2.create_arc(coordinates03,fill="Red",start=0,extent=90) # creating a ace of 90 degree with givwen coordinates

canvas_3=tk.Canvas(win,bg="lightgreen")
canvas_3.place(x=90,y=270,height=50,width=50) # can create circle,oval,ellips according to the coordinates
coordinates03=20,20,50,50
oval_01=canvas_3.create_oval(20,20,50,50,fill="Red")
                        #   (coordinates03,fill="Red") 

# Hierarchical Treeview
tree01 = ttk.Treeview(win)

tree01.insert("", tk.END, text="Python", iid=0)
tree01.insert("", tk.END, text="Java", iid=1)
tree01.insert("", tk.END, text="Web", iid=2)

tree01.insert("", tk.END, text="ML", iid=3)
tree01.insert("", tk.END, text="DS", iid=4)

tree01.insert("", tk.END, text="HTML", iid=5)
tree01.insert("", tk.END, text="CSS", iid=6)

tree01.move(3,0,0) # move 4th item(ML) as subset of 1st item(python)
tree01.move(4,0,1)

tree01.move(5,2,0)
tree01.move(6,2,1)

tree01.place(x=150,y=220,height=180,width=100)

# bind (alternative of command)
def pty(event):
    print("Hello Python")
    print(event)
button5=tk.Button(win,text="Bind Button") # create a button through which binf function will occur
button5.bind('<Leave>',pty) # Leave function occur when we pass the cursor through it
button5.place(x=250,y=220,height=30,width=70)
# other operation\function like enter,button,motion,presskey,releasekey ect ect.
def ptyy(event):
    print("Helllo Java")
button5.bind('<Button-1>',ptyy)
def ptyyy(event):
    print("Hello C++")
button5.bind('<Button-1>',ptyyy,add="+") # through"+" we can use to function simulataneously with one operation

# Unbind 
# same syntax as bind function with exect opposite usage

win.mainloop() # Start the main loop of the window
