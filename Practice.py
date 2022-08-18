from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning")
root.iconbitmap("Calculator.ico")

img1 = ImageTk.PhotoImage(Image.open("1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("4.jpg"))

img_list = [img1, img2, img3, img4]

img_label = Label(image=img1)
img_label.grid(row=0, column=0, columnspan=2)

global j
j=3

def forward():
    global i
    i=0
    img_label.grid_forget()
    if i<=3:
        i=i+1
        new_img = Label(image=img_list[i])
        new_img.grid(row=0, column=0, columnspan=2)
    else:
        i=0
   
        

def backward():
    img_label.grid_forget()
    index1 = img_label.index()
    label = Label(root, text=index1)
    if j>=0:
        j=j-1
        new_img1 = Label(image=img_list[j])
        new_img1.grid(row=0, column=0, columnspan=2)
    else:
        j=3

back_butt = Button(root, text="<<", command=backward)
forward_butt = Button(root, text=">>", command=forward)
back_butt.grid(row=1, column=0)
forward_butt.grid(row=1, column=1)


root.mainloop()
