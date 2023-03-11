from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from tkinter import messagebox

def back2login():
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    same=True
    n=0.25
    # Adding a background image
    # =============================================================================
    # background_image =Image.open("E:\Library Management System\lib.jpg")
    # [imageSizeWidth, imageSizeHeight] = background_image.size
    # newImageSizeWidth = int(imageSizeWidth*n)
    # if same:
    #     newImageSizeHeight = int(imageSizeHeight*n) 
    # else:
    #     newImageSizeHeight = int(imageSizeHeight/n) 
    #     
    # background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(background_image)
    # Canvas1 = Canvas(root)
    # Canvas1.create_image(300,340,image = img)      
    # Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    # Canvas1.pack(expand=True,fill=BOTH)
    # =============================================================================

    bg = PhotoImage( file = "E:\Library Management System\lib.png")

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Admin Login", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=lambda:[root.destroy(),addBook()])
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=lambda:[root.destroy(),delete()])
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=NONE)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        
    # =============================================================================
    # btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = NONE)
    # btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    #     
    # btn5 = Button(root,text="Return Book",bg='black', fg='white', command = NONE)
    # btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    # =============================================================================
    root.mainloop()