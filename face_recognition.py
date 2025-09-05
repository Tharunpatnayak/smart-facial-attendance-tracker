from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import time
from datetime import datetime
import cv2
import numpy as np
from mtcnn import MTCNN
import os

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.attendance_marked = {}  # Dictionary to track marked attendance with timestamps
        self.face_tracking = {}  # Dictionary to track faces during verification

        # Load existing attendance from CSV
        try:
            with open("attendance_report/tharun.csv", "r", newline="\n") as f:
                lines = f.readlines()
                header_found = False
                start_index = 0
                if lines and lines[0].strip().startswith("StudentId,Roll,Name"):
                    header_found = True
                    start_index = 1
                for line in lines[start_index:]:
                    if line.strip():
                        try:
                            parts = line.strip().split(",")
                            if len(parts) >= 7:  # Ensure enough columns
                                student_id, _, _, _, time_str, date_str, _ = parts[:7]
                                # Parse time and date (format: HH:MM:SS, DD/MM/YYYY)
                                try:
                                    dt = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M:%S")
                                    timestamp = dt.timestamp()
                                    if student_id not in self.attendance_marked:
                                        self.attendance_marked[student_id] = []
                                    self.attendance_marked[student_id].append(timestamp)
                                    print(f"[init] Loaded timestamp for {student_id}: {timestamp} ({date_str} {time_str})")
                                except ValueError as e:
                                    print(f"[init] Invalid datetime in CSV: {line.strip()}, Error: {e}")
                            else:
                                print(f"[init] Malformed CSV line (too few columns): {line.strip()}")
                        except Exception as e:
                            print(f"[init] Error parsing CSV line: {line.strip()}, Error: {e}")
                if not header_found:
                    print("[init] No header found in CSV, treated all lines as data")
            print(f"[init] Loaded attendance IDs: {list(self.attendance_marked.keys())}")
        except FileNotFoundError:
            print("[init] No existing attendance file found")

        # UI Elements
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Face Recognition Software\5EERFPimg\f1.png")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(r"C:\Face Recognition Software\5EERFPimg\f2.png")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=880, height=700)

        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=("times new roman", 18, "bold"),
                      bg="darkgreen", fg="white", command=self.face_recog)
        b1_1.place(x=365, y=620, width=200, height=40)

    def mark_attendance(self, student_id, roll, name, dep):
        current_time = time()
        # Initialize timestamp list if student_id is new
        if student_id not in self.attendance_marked:
            self.attendance_marked[student_id] = []

        # Check if attendance was marked within last 4 hours
        timestamps = self.attendance_marked[student_id]
        if timestamps:
            last_marked = max(timestamps)
            time_diff = current_time - last_marked
            if time_diff < 14400:  # 4 hours = 14400 seconds
                print(f"[mark_attendance] Attendance already marked for {student_id} within 4 hours (last: {last_marked}, now: {current_time}, diff: {time_diff}s)")
                return
            else:
                print(f"[mark_attendance] 4 hours elapsed for {student_id} (last: {last_marked}, now: {current_time}, diff: {time_diff}s)")
        else:
            print(f"[mark_attendance] No previous timestamps for {student_id}, allowing marking")

        # Update in-memory tracking first
        self.attendance_marked[student_id].append(current_time)

        # Read existing CSV data
        try:
            with open("attendance_report/tharun.csv", "r", newline="\n") as f:
                myDataList = f.readlines()
        except FileNotFoundError:
            myDataList = []

        # Create new attendance entry
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")
        new_entry = f"{student_id},{roll},{name},{dep},{dtString},{d1},Present"

        # Append new entry to data list
        myDataList.append(new_entry + "\n")

        # Parse and sort entries by student_id, excluding header
        parsed_entries = []
        for line in myDataList:
            if line.strip() and not line.startswith("StudentId,Roll,Name"):
                parsed_entries.append(line.strip().split(","))

        # Sort by student_id (index 0)
        parsed_entries.sort(key=lambda x: x[0])

        # Write sorted entries back to CSV with header
        try:
            with open("attendance_report/tharun.csv", "w", newline="\n") as f:
                f.write("StudentId,Roll,Name,Department,Time,Date,Attendance Status\n")
                for entry in parsed_entries:
                    f.write(",".join(entry) + "\n")
        except Exception as e:
            print(f"[mark_attendance] Error writing to CSV: {e}")
            # Roll back in-memory update if CSV write fails
            self.attendance_marked[student_id].pop()
            return

        print(f"[mark_attendance] Attendance marked for {name} (ID: {student_id}), Timestamps: {self.attendance_marked[student_id]}")

    def face_recog(self):
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        detector = MTCNN()
        video_cap = cv2.VideoCapture(1)  # Adjust index if needed
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Could not open Camo Studio camera. Check index or connection.")
            return
        video_cap.set(3, 1280)
        video_cap.set(4, 720)

        valid_ids = set()
        data_dir = "data"
        for file in os.listdir(data_dir):
            if file.endswith('.jpg'):
                student_id = file.split('.')[1]
                valid_ids.add(student_id)
        print(f"[face_recog] Valid Trained IDs: {valid_ids}")

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="tharun", database="face_recognizer")
            my_cursor = conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", f"Database connection failed: {str(e)}")
            return

        try:
            while True:
                ret, frame = video_cap.read()
                if not ret:
                    messagebox.showerror("Error", "Failed to capture frame from Camo Studio.")
                    break

                faces = detector.detect_faces(frame)
                for face in faces:
                    x, y, w, h = face['box']
                    confidence = face['confidence']

                    if confidence > 0.95 and w >= 100 and h >= 100:
                        face_region = frame[y:y+h, x:x+w]
                        gray_face = cv2.cvtColor(face_region, cv2.COLOR_BGR2GRAY)
                        gray_face = cv2.resize(gray_face, (200, 200), interpolation=cv2.INTER_LINEAR)

                        id, raw_confidence = clf.predict(gray_face)
                        confidence_score = int(100 * (1 - raw_confidence / 300))
                        print(f"[face_recog] Predicted ID: {id}, Confidence: {confidence_score}")

                        if confidence_score > 85 and str(id) in valid_ids:
                            try:
                                my_cursor.execute("SELECT Student_id, Name, Roll, Dep FROM student WHERE Student_id = %s", (str(id),))
                                result = my_cursor.fetchone()
                                print(f"[face_recog] DB Result: {result}")
                            except Exception as e:
                                result = None
                                cv2.putText(frame, f"DB Error: {str(e)}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                            if result:
                                student_id, name, roll, dep = result
                                print(f"[face_recog] Identified: {student_id}, {name}")

                                # Check attendance first
                                current_time = time()
                                if student_id in self.attendance_marked and self.attendance_marked[student_id]:
                                    last_marked = max(self.attendance_marked[student_id])
                                    if current_time - last_marked < 14400:  # 4 hours
                                        print(f"[face_recog] Attendance already marked for {student_id} within 4 hours - Skipping")
                                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 3)  # Yellow box
                                        cv2.putText(frame, "Already Attendance Marked", (x, y - 105), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
                                        cv2.putText(frame, f"ID: {student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                        cv2.putText(frame, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                        cv2.putText(frame, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                        cv2.putText(frame, f"Dept: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                        continue

                                # Proceed to verification
                                print(f"[face_recog] Attendance not marked or 4 hours elapsed for {student_id} - Starting verification")
                                if student_id not in self.face_tracking:
                                    self.face_tracking[student_id] = {
                                        "start_time": current_time,
                                        "count": 1,
                                        "confidence_history": [confidence_score]
                                    }
                                    print(f"[face_recog] Tracking started for {student_id}")
                                else:
                                    tracking = self.face_tracking[student_id]
                                    tracking["count"] += 1
                                    tracking["confidence_history"].append(confidence_score)
                                    if len(tracking["confidence_history"]) > 30:
                                        tracking["confidence_history"].pop(0)
                                    avg_confidence = sum(tracking["confidence_history"]) / len(tracking["confidence_history"])
                                    print(f"[face_recog] Tracking {student_id} - Avg Confidence: {avg_confidence:.2f}, Count: {tracking['count']}")

                                    if avg_confidence > 85:
                                        elapsed_time = time() - tracking["start_time"]
                                        if elapsed_time >= 10:  # Verification time 10 seconds
                                            print(f"[face_recog] Verification complete for {student_id}")
                                            self.mark_attendance(student_id, roll, name, dep)
                                            # Display "Attendance Marked" for 3 seconds
                                            mark_time = time()
                                            while time() - mark_time < 3:
                                                ret, frame = video_cap.read()
                                                if not ret:
                                                    break
                                                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                                                cv2.putText(frame, "Attendance Marked", (x, y - 105), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                                                cv2.putText(frame, f"ID: {student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                                cv2.putText(frame, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                                cv2.putText(frame, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                                cv2.putText(frame, f"Dept: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                                cv2.imshow("Welcome to Face Recognition (Camo Studio)", frame)
                                                cv2.waitKey(1)
                                            del self.face_tracking[student_id]
                                            continue
                                        else:
                                            remaining_time = int(10 - elapsed_time)
                                            cv2.putText(frame, f"Verifying: {remaining_time}s", (x, y - 105), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)

                                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                                    cv2.putText(frame, f"ID: {student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                    cv2.putText(frame, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                    cv2.putText(frame, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                                    cv2.putText(frame, f"Dept: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                            else:
                                print(f"[face_recog] No DB match for ID {id}")
                                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                                cv2.putText(frame, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
                        else:
                            print(f"[face_recog] Rejected: Confidence {confidence_score} too low or ID {id} invalid")
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                            cv2.putText(frame, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
                    else:
                        print(f"[face_recog] Skipped face: Low MTCNN confidence {confidence} or size w={w}, h={h}")
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(frame, "Invalid Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                cv2.imshow("Welcome to Face Recognition (Camo Studio)", frame)
                if cv2.waitKey(1) == 13:  # Enter key to exit
                    break
        finally:
            video_cap.release()
            cv2.destroyAllWindows()
            conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()