import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import *
from tkinter import messagebox
from mysql.connector import Error

db = mysql.connector.connect(host ="localhost", user = 'root', password = 'root', db ="login_details")

def submitact():
	
	user = Username.get()
	passw = password.get()

	logintodb(user, passw)

def logintodb(user, passw):
    
    user1=tuple([user])
    
	
	# If password is enetered by the
	# user
    cur = db.cursor()
    cur.execute("SELECT username FROM login")
    a=0
    for row in cur:
        if user in row:
            a=1
    cur.close()
    
    b=1
    if a==1:
        cur = db.cursor()
        cur.execute("select password from login where username = %s",user1)
        
        for row in cur:
            if passw in row:
                b=0
                #print("Login Sucesfully!")
                login(user, passw)
                
                
        
        cur.close()
        if b!=0:
            messagebox.showerror('Login Error', 'Incorrect Password')
    else:
        messagebox.showerror('Login Error', 'Incorrect Username')
    Username.delete(0,END)
    password.delete(0,END)
    
def login(user, passw):
    if user=="admin":
        root.destroy()
        adminlogin()
    else:
        root.destroy()
        studentlogin()
        
    
def loginpage():
    global Username, password, root
    root = tk.Tk()
    root.geometry("300x200")
    root.title("Login Page")
    Canvas1 = Canvas(root)

    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)


    # Defining the first row
    lblfrstrow = tk.Label(root, text ="Username -",bg='black',fg='white' )
    lblfrstrow.place(x = 70, y = 40)

    Username = tk.Entry(root, width = 35)
    Username.place(x = 150, y = 40, width = 100)

    lblsecrow = tk.Label(root, text ="Password -",bg='black',fg='white')
    lblsecrow.place(x = 70, y = 70)

    password = tk.Entry(root, width = 35, show='*')
    password.place(x = 150, y = 70, width = 100)

    submitbtn = tk.Button(root, text ="Login",
    					bg ='white',fg='black', command = submitact)
    submitbtn.place(x = 125, y = 125, width = 55)

    root.mainloop()
# =============================================================================
# # Admin_Login
# =============================================================================
def adminlogin():
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.maxsize(width=400,height=400)
    root.canvas = Canvas(width=800, height=500, bg='black')
    root.canvas.pack()
    root.geometry("600x500")




    
    headingFrame1 = Frame(root,bg="yellow",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Admin Login", bg='black', fg='white', font=(("Courier new",20,'bold')))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=lambda:[root.destroy(),addBook()])
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=lambda:[root.destroy(),delete()])
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=lambda:[root.destroy(),Search().mainloop()])
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        
    btn4 = Button(root,text="Quit",bg='black', fg='white', command = root.destroy)
    btn4.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    #     
    btn5 = Button(root,text="Logout",bg='black', fg='white', command = lambda:[root.destroy(),loginpage()])
    btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    # =============================================================================
    root.mainloop()

bookTable = "books_detail"
def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    insertBooks = "insert into "+bookTable+" values ('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    bookInfo1.delete(0,END)
    bookInfo2.delete(0,END)
    bookInfo3.delete(0,END)
    bookInfo4.delete(0,END)
    
def addBook(): 
    
    global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    con = mysql.connector.connect( host="localhost",user="root",password="root",db="library")
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books_detail" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="ADD BOOK",bg='white', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="BACK",bg='white', fg='black', command=lambda:[root.destroy(),adminlogin()])
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()




con = mysql.connector.connect(host="localhost",user="root",password="root",database="library")
cur = con.cursor()


def deleteBook():
    
    bid = bookInfo1.get()
    
    deleteSql = "delete from "+bookTable+" where book_id = '"+bid+"'"
    

    try:
        cur.execute(deleteSql)
        con.commit()
        

        messagebox.showinfo('Success',"Book Record Deleted Successfully")

    except:
        messagebox.showinfo('Error',"Please check Book ID")
    
    #print(bid)

    bookInfo1.delete(0, END)
    #studentroot.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root)
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.1,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.25,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="DELETE",bg='white', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="BACK",bg='white', fg='black', command=lambda:[root.destroy(),adminlogin()])
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    
    
class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Book")
        self.maxsize(800,500)
        self.minsize(800,500)
        self.canvas = Canvas(width=800, height=500, bg='black')
        self.canvas.pack()
       
        headingFrame1 = Frame(self,bg="yellow",bd=5)
        headingFrame1.place(x=290,y=20,w=240,h=46)
        l1=Label(headingFrame1,text="Search Library",bg='black',fg='white', font=("Courier new",20,'bold')).place(x=0,y=0)
        l = Label(self, text="Search By",bg='black',fg='white', font=("Courier new", 15, 'bold')).place(x=60, y=96)
        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))
            self.en.delete(0, END)
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')

            elif g.get() == 'All':
                try:
                    self.conn = mysql.connector.connect(host='localhost',database='library',user='root',password='root')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books_detail")
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Name is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
            
            elif g.get() == 'Book Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',database='library',user='root',password='root')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books_detail where tilte LIKE %s",['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Name is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
           
            elif g.get() == 'Author Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books_detail where author LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Author Name not found")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
            
            elif g.get() == 'Book Id':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='root')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books_detail where book_id LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Id is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
            
            elif g.get() == 'Availability':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='root')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books_detail where status='avail'")
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Id is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
       
        b=Button(self,text="FIND",width=15,bg='white',font=("Courier new",10,'bold'),command=ge).place(x=550,y=100)
        b1=Button(self,text="BACK",width=15,bg='white',font=("Courier new",10,'bold'),command=lambda:[self.destroy(),adminlogin()]).place(x=550,y=148)
        c=ttk.Combobox(self,textvariable=g,values=["All","Book Name","Author Name","Book Id","Availability"],width=40,state="readonly").place(x = 180, y = 100)
        en = Entry(self,textvariable=f,width=43).place(x=180,y=155)
        la = Label(self, text="Enter",bg='black',fg='white', font=("Courier new", 15, 'bold')).place(x=100, y=150)
    

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Book Name', 'Book Author', 'Availability'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Book ID', anchor='center')
        self.listTree.column("#0", width=120, anchor='center')
        self.listTree.heading("Book Name", text='Book Name')
        self.listTree.column("Book Name", width=200, anchor='center')
        self.listTree.heading("Book Author", text='Book Author')
        self.listTree.column("Book Author", width=200, anchor='center')
        self.listTree.heading("Availability", text='Availability')
        self.listTree.column("Availability", width=200, anchor='center')
        self.listTree.bind('&lt;Button-1&gt;', handle)
        self.listTree.place(x=40, y=200)
        self.vsb.place(x=763,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))
        
# =============================================================================
# Student_Login
# =============================================================================

def studentlogin():
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.maxsize(width=400,height=400)
    root.canvas = Canvas(width=800, height=500, bg='black')
    root.canvas.pack()
    root.geometry("600x500")


    headingFrame1 = Frame(root,bg="yellow",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Student Login", bg='black', fg='white', font=(("Courier new",20,'bold')))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=lambda:[root.destroy(),Search1().mainloop()])
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    
    btn4 = Button(root,text="Quit",bg='black', fg='white', command = root.destroy)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
    btn5 = Button(root,text="Logout",bg='black', fg='white', command = lambda:[root.destroy(),loginpage()])
    btn5.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    root.mainloop()
    
class Search1(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Book")
        self.maxsize(800,500)
        self.minsize(800,500)
        self.canvas = Canvas(width=800, height=500, bg='black')
        self.canvas.pack()
        #self.iconbitmap(r'libico.ico')
        headingFrame1 = Frame(self,bg="yellow",bd=5)
        headingFrame1.place(x=290,y=20,w=240,h=46)
        l1=Label(headingFrame1,text="Search Library",bg='black',fg='white', font=("Courier new",20,'bold')).place(x=0,y=0)
        l = Label(self, text="Search By",bg='black',fg='white', font=("Courier new", 15, 'bold')).place(x=60, y=96)
        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))
            
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')

            elif g.get() == 'All':
                try:
                    self.conn = mysql.connector.connect(host='localhost',database='library',user='root',password='root')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books_detail")
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Name is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
            elif g.get() == 'Book Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',database='library',user='root',password='root')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books_detail where tilte LIKE %s",['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Name is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
            elif g.get() == 'Author Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',database='library',user='root',password='root')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books_detail where author LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Author Name not found")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
            elif g.get() == 'Book Id':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='root')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books_detail where book_id LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Id is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
                    
            elif g.get() == 'Availability':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='root')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books_detail where status='avail'")
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Id is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
                    
                    
        b=Button(self,text="FIND",width=15,bg='white',font=("Courier new",10,'bold'),command=ge).place(x=550,y=100)
        b1=Button(self,text="BACK",width=15,bg='white',font=("Courier new",10,'bold'),command=lambda:[self.destroy(),studentlogin()]).place(x=550,y=148)
        c=ttk.Combobox(self,textvariable=g,values=["All","Book Name","Author Name","Book Id","Availability"],width=40,state="readonly").place(x = 180, y = 100)
        en = Entry(self,textvariable=f,width=43).place(x=180,y=155)
        la = Label(self, text="Enter",bg='black',fg='white', font=("Courier new", 15, 'bold')).place(x=100, y=150)
    

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Book Name', 'Book Author', 'Availability'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Book ID', anchor='center')
        self.listTree.column("#0", width=120, anchor='center')
        self.listTree.heading("Book Name", text='Book Name')
        self.listTree.column("Book Name", width=200, anchor='center')
        self.listTree.heading("Book Author", text='Book Author')
        self.listTree.column("Book Author", width=200, anchor='center')
        self.listTree.heading("Availability", text='Availability')
        self.listTree.column("Availability", width=200, anchor='center')
        self.listTree.bind('&lt;Button-1&gt;', handle)
        self.listTree.place(x=40, y=200)
        self.vsb.place(x=763,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))
        
# =============================================================================
# 
# =============================================================================
loginpage()