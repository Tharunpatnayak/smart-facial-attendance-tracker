from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox,Toplevel
import mysql.connector
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
from developer import Developer

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"C:\5EERFPimg\lback1.png")  # Raw string (correct)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Login Icon
        img1 = Image.open(r"C:\5EERFPimg\loic.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        # Get Started Text
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #======Icon images=======
        img2 = Image.open(r"C:\5EERFPimg\loic.png")
        img2 = img2.resize((25,25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(self.root, image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=325, width=25, height=25)

        img3 = Image.open(r"C:\5EERFPimg\Lock_red-512.png")
        img3 = img3.resize((25,25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(self.root, image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=394, width=25, height=25)

        #Login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
  #register button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman", 10, "bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forget passbtn
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman", 10, "bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)    
    
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="tharun",  # Ideally, fetch from a secure source
                database="mydata"
            )
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                is_admin = messagebox.askyesno("Access Confirmation", "Access only for admin. Proceed?")
                if is_admin:
                    self.new_window = Toplevel(self.root)  # Ensure self.root is the main window
                    self.app = Face_Recognition_System(self.new_window)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        finally:
            conn.close()
            #==============reset password=========================
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter The Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter The Newpassword",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="tharun",database="mydata")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset , please login new password",parent=self.root2)
                self.root2.destroy()
            
    

            #===============================forgot password window==================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="tharun",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row is None:
                messagebox.showerror("My Error","Please Enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman", 20, "bold"), fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)
                self.combo_securiy_Q=ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_securiy_Q["values"]=("Select", "Your Birth Place", "Your age")
                self.combo_securiy_Q.place(x=50,y=110,width=250)
                self.combo_securiy_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=100,y=290)



       



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        #===variables==========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()




        #=====bg img=====
        self.bg=ImageTk.PhotoImage(file=r"C:\5EERFPimg\regi1.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #=====left img=====
        self.bg1=ImageTk.PhotoImage(file=r"C:\5EERFPimg\r2.png")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        #=====main frame=========
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #=====label and entry===========
        #-------------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        #-------------------row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #-------------------row3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        self.combo_securiy_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15, "bold"), state="readonly")
        self.combo_securiy_Q["values"]=("Select", "Your Birth Place", "Your age")
        self.combo_securiy_Q.place(x=50,y=270,width=250)
        self.combo_securiy_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #-----------row4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        #=============checkbutton=============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50,y=380)
#=============buttons====
        img=Image.open(r"C:\5EERFPimg\register.png")
        img=img.resize((200,55), Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame, image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2", font=("times new roman", 15, "bold"), fg="white")
        b1.place(x=10,y=420, width=200)
        
        img1=Image.open(r"C:\5EERFPimg\login.png")
        img1=img1.resize((200,45), Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white")
        b1.place(x=330,y=420,width=200)

        #==============function declaration=======

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="tharun",database="mydata")
            my_cursor=conn.cursor()
            query="select * from register where email=%s"
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()

        



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")

        self.root.title("Face Recognition System")
       #first image
        img_path = r"C:\5EERFPimg\i1.jpg"  
       
        img = Image.open(img_path)
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
       

   #second image

        img_path1 = r"C:\5EERFPimg\Facial recognition.png"  

        img1 = Image.open(img_path1)
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)


    #third image

        img_path2 = r"C:\5EERFPimg\i3.jpg"  

             
        img2 = Image.open(img_path2)
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

           
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)
    #bg img
        img_path3 = r"C:\5EERFPimg\bg.png"  
        img3 = Image.open(img_path3)
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

           
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

     #===========time=========================
        def time():
            string=strftime('%H:%M:%S')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='dark green')
        lbl.place(x=0,y=0,width=140,height=50)
        time()


    #STUDENT BUTTON
        img_path4 = r"C:\5EERFPimg\student.jpg"  
        img4 = Image.open(img_path4)
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)


        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2") 
        b1_1.place(x=200,y=300,width=220,height=40)



        #detect face BUTTON
        img_path5 = r"C:\5EERFPimg\facedetector.png"  
        img5 = Image.open(img_path5)
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=600,y=100,width=220,height=220)


        b1_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_data) 
        b1_1.place(x=600,y=300,width=220,height=40)


        #attendance BUTTON
        img_path6 = r"C:\5EERFPimg\attendance.png"  
        img6 = Image.open(img_path6)
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=1000,y=100,width=220,height=220)


        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data) 
        b1_1.place(x=1000,y=300,width=220,height=40)



        #train data BUTTON
        img_path7 = r"C:\5EERFPimg\traindata.png"  
        img7 = Image.open(img_path7)
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)


        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data) 
        b1_1.place(x=200,y=600,width=220,height=40)

       

       #photos BUTTON
        img_path8 = r"C:\5EERFPimg\photos.png"  
        img8 = Image.open(img_path8)
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=600,y=400,width=220,height=220)


        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img) 
        b1_1.place(x=600,y=600,width=220,height=40)




        #developer BUTTON
        img_path9 = r"C:\5EERFPimg\developer.png"  
        img9 = Image.open(img_path9)
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.developer_data)
        b1.place(x=1000,y=400,width=220,height=220)


        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data) 
        b1_1.place(x=1000,y=600,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    #============function buttons===============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)







if __name__ == "__main__":
    main()
