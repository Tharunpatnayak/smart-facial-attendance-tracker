from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
from mtcnn import MTCNN




class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")

        self.root.title("Face Recognition System")
        
        
        #===========================variables=======================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        #first image
        img_path = r"C:\5EERFPimg\s1.png"  
       
        img = Image.open(img_path)
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
       

   #second image

        img_path1 = r"C:\5EERFPimg\s2.png"  

        img1 = Image.open(img_path1)
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)


    #third image

        img_path2 = r"C:\5EERFPimg\s3.png"  

             
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


        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730 ,height=580)

        img_path_left = r"C:\5EERFPimg\sleft.png"

             
        img_left = Image.open(img_path_left)
        img_left = img_left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)
        
        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=125,width=720 ,height=125)
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold",),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer Science and Enginnering","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","B-Tech","M-Tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2021-2022","2022-2023","2023-2024","2024-2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
         #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        #class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720 ,height=300)
        #student id
        studentID_label=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        #student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=18)
        div_combo["values"]=("Select Division","A","B","C","D","E","F","G","H","I","J")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date of birth
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher name
        address_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")#textvariable=self.var_radio1
        radiobtn2.grid(row=6,column=1)
        
        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1) 
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2) 
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",command=self.update_photo_sample,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
               
         #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
        
        img_path_right = r"C:\5EERFPimg\sright.png"

             
        img_right = Image.open(img_path_right)
        img_right = img_right.resize((720, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)
        
        
        
        #********search system********************
                # Inside the __init__ method, update the search_frame section
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        self.search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 13, "bold"))
        self.search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", command=self.search_data, width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="show All", command=self.show_all_data, width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)
        #=======table frame======
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710 ,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Rollno")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #===========function declaration===================
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="tharun",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),                           
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        


    #====fetch data=============================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="tharun",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #========get cursor========================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
#update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="tharun",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_std_id.get()
                                                                                                                                                                        ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="tharun",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#==============Generate data set or take photo samples=============================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return
        try:
            # Database Connection
            conn = mysql.connector.connect(host="localhost", username="root", password="tharun", database="face_recognizer")
            my_cursor = conn.cursor()
            
            student_id = self.var_std_id.get()
            
            # Check if student exists
            my_cursor.execute("SELECT * FROM student WHERE Student_id = %s", (student_id,))
            existing_student = my_cursor.fetchone()
            
            if existing_student:
                my_cursor.execute("""
                    UPDATE student 
                    SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, 
                        Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, 
                        Teacher=%s, PhotoSample=%s 
                    WHERE Student_id=%s
                """, (
                    self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                    self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                    self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                    self.var_teacher.get(), "Yes", student_id
                ))
            else:
                my_cursor.execute("""
                    INSERT INTO student (
                        Student_id, Dep, Course, Year, Semester, Name, Division, 
                        Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    student_id, self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                    self.var_semester.get(), self.var_std_name.get(), self.var_div.get(),
                    self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(),
                    self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), "Yes"
                ))

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # Face Detection Using MTCNN with Camo Studio
            detector = MTCNN()
            # Try different indices (0, 1, 2) to find Camo Studio's virtual webcam
            cap = cv2.VideoCapture(1)  # Adjust index if needed (1 or 2 might work for Camo Studio)
            if not cap.isOpened():
                messagebox.showerror("Error", "Could not open Camo Studio camera. Check index or connection.", parent=self.root)
                return
            cap.set(3, 1280)
            cap.set(4, 720)
            img_id = 0
            dataset_path = "data/"
            if not os.path.exists(dataset_path):
                os.makedirs(dataset_path)

            while True:
                ret, frame = cap.read()
                if not ret:
                    messagebox.showerror("Error", "Failed to capture frame from Camo Studio.", parent=self.root)
                    break

                faces = detector.detect_faces(frame)
                if len(faces) == 1:  # Ensure only one face is detected
                    face = faces[0]
                    x, y, w, h = face['box']
                    confidence = face['confidence']

                    if confidence > 0.95 and w >= 100 and h >= 100:
                        y = max(y - 20, 0)
                        h = min(h + 40, frame.shape[0] - y)
                        face_cropped = frame[y:y+h, x:x+w]
                        if face_cropped.size == 0:
                            continue

                        # Resize to 200x200 (consistent with recognition and training)
                        face_resized = cv2.resize(face_cropped, (200, 200))
                        face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                        img_id += 1
                        file_name_path = f"{dataset_path}user.{student_id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face_gray, [cv2.IMWRITE_JPEG_QUALITY, 95])
                        cv2.putText(frame, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    cv2.imshow("Captured Face (Camo Studio)", frame)
                    if cv2.waitKey(1) == 13 or img_id == 100:  # Enter key or 100 samples
                        break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", f"Dataset Generated for Student ID: {student_id}!", parent=self.root)
            self.root.focus_force()

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def update_photo_sample(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please enter a Student ID", parent=self.root)
            return

        try:
            # Database Connection
            conn = mysql.connector.connect(host="localhost", username="root", password="tharun", database="face_recognizer")
            my_cursor = conn.cursor()

            student_id = self.var_std_id.get()

            # Check if student exists
            my_cursor.execute("SELECT * FROM student WHERE Student_id = %s", (student_id,))
            existing_student = my_cursor.fetchone()

            if not existing_student:
                messagebox.showerror("Error", f"No student found with ID {student_id}", parent=self.root)
                conn.close()
                return

            # Update student details if changed
            my_cursor.execute("""
                UPDATE student 
                SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, 
                    Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, 
                    Teacher=%s, PhotoSample=%s 
                WHERE Student_id=%s
            """, (
                self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                self.var_teacher.get(), "Yes", student_id
            ))

            conn.commit()
            self.fetch_data()
            conn.close()

            # Face Detection Using MTCNN with Camo Studio
            detector = MTCNN()
            cap = cv2.VideoCapture(1)  # Adjust index if needed (1 or 2 might work for Camo Studio)
            if not cap.isOpened():
                messagebox.showerror("Error", "Could not open Camo Studio camera. Check index or connection.", parent=self.root)
                return
            cap.set(3, 1280)
            cap.set(4, 720)
            img_id = 0
            dataset_path = "data/"
            if not os.path.exists(dataset_path):
                os.makedirs(dataset_path)

            # Delete existing photos for this student to avoid duplication
            existing_files = [f for f in os.listdir(dataset_path) if f.startswith(f"user.{student_id}.")]
            for file in existing_files:
                os.remove(os.path.join(dataset_path, file))

            while True:
                ret, frame = cap.read()
                if not ret:
                    messagebox.showerror("Error", "Failed to capture frame from Camo Studio.", parent=self.root)
                    break

                faces = detector.detect_faces(frame)
                if len(faces) == 1:  # Ensure only one face is detected
                    face = faces[0]
                    x, y, w, h = face['box']
                    confidence = face['confidence']

                    if confidence > 0.95 and w >= 100 and h >= 100:
                        y = max(y - 20, 0)
                        h = min(h + 40, frame.shape[0] - y)
                        face_cropped = frame[y:y+h, x:x+w]
                        if face_cropped.size == 0:
                            continue

                        # Resize to 200x200
                        face_resized = cv2.resize(face_cropped, (200, 200))
                        face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                        img_id += 1
                        file_name_path = f"{dataset_path}user.{student_id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face_gray, [cv2.IMWRITE_JPEG_QUALITY, 95])
                        cv2.putText(frame, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    cv2.imshow("Captured Face (Camo Studio)", frame)
                    if cv2.waitKey(1) == 13 or img_id == 100:  # Enter key or 100 samples
                        break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", f"Photo Sample Updated for Student ID: {student_id}!", parent=self.root)
            self.root.focus_force()

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


            
#search system --search by
    def search_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="tharun", database="face_recognizer")
            my_cursor = conn.cursor()

            search_by = self.search_combo.get()
            search_text = self.search_entry.get().strip()  # Remove leading/trailing whitespace

            if not search_text:
                messagebox.showerror("Error", "Please enter a search value", parent=self.root)
                return

            if search_by == "Roll_No":
                my_cursor.execute("SELECT * FROM student WHERE roll = %s", (search_text,))
            elif search_by == "Phone_No":
                my_cursor.execute("SELECT * FROM student WHERE phone = %s", (search_text,))
            else:
                messagebox.showerror("Error", "Please select a search criterion", parent=self.root)
                return

            rows = my_cursor.fetchall()
            print(f"Query executed: SELECT * FROM student WHERE {search_by.lower()} = '{search_text}'")  # Debug print
            print(f"Rows returned: {rows}")  # Debug print
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No matching records found", parent=self.root)
                self.fetch_data()

            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def show_all_data(self):
        self.fetch_data()







                














if __name__ == "__main__":
    root = Tk()
    obj =Student(root)
    root.mainloop()

