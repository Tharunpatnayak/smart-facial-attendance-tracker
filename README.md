# Smart Facial Attendance Tracker  

## 📌 Project Overview  
The **Smart Facial Attendance Tracker** is a real-time, AI-powered system designed to automate attendance marking using **facial recognition technology**.  
It replaces traditional methods such as manual roll calls, RFID cards, or fingerprint scanners with a **secure, contactless, and efficient solution**.  
The system captures and analyzes facial features, matches them with stored profiles, and automatically marks attendance in real time.  

---

## ✨ Features  
- 👤 **User Registration** – Enroll students/employees with facial data and details.  
- 🎥 **Real-time Face Detection & Recognition** – Detects and recognizes faces using **MTCNN** and **LBPH** algorithms.  
- 🕒 **Automated Attendance Logging** – Stores attendance with timestamps in a **MySQL database**.  
- 📊 **Reports & Analytics** – Generates CSV-based attendance reports.  
- 🔑 **Secure Login System** – Admin/user authentication with password reset options.  
- 📷 **Dataset Creation & Training** – Capture, preprocess, and train datasets for higher accuracy.  
- 🖥️ **User-Friendly GUI** – Built using **Tkinter** for smooth interaction.  

---

## 🛠️ Technology Stack  
**Languages & Frameworks:**  
- Python (Core Development, Face Recognition)  
- Tkinter (GUI)  
- HTML, CSS (Login/Registration Pages)  

**Libraries & Tools:**  
- OpenCV  
- MTCNN (Multi-task Cascaded Convolutional Networks)  
- LBPH (Local Binary Patterns Histogram)  
- NumPy, Pillow  
- Flask (optional backend integration)  
- Camo Studio (face detection & testing)  

**Database:**  
- MySQL (Attendance & User Data Storage)  

**Development Tools:**  
- Visual Studio Code  
- MySQL Workbench   

---

## ⚙️ Installation & Setup  

1. **Clone the repository**  
```bash
git clone https://github.com/Tharunpatnayak/smart-facial-attendance-tracker.git
cd smart-facial-attendance-tracker
```
2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Setup MySQL Database
- Create a database ```bash mydata```.
- Import schema (tables for users, attendance).
- Update MySQL username & password in ```bash Face_Recognition_Software.py.```
  
5. Run the project
```bash
python Face_Recognition_Software.py
```

📂 Project Structure
```bash
📦 smart-facial-attendance-tracker
├── Face_Recognition_Software.py   # Main application
├── student.py                     # Student data management
├── train.py                       # Training model with dataset
├── face_recognition.py            # Face recognition logic
├── attendance.py                  # Attendance logging
├── developer.py                   # Developer info page
├── data/                          # Captured face datasets
├── attendance_report/             # Attendance CSV reports
├── requirements.txt               # Dependencies
└── README.md                      # Project documentation
```

🚀 Usage Flow
- Admin logs into the system.
- Register students/employees with details and face samples.
- Train the dataset.
- Start real-time facial recognition.
- Attendance is logged automatically into the database.
- Reports can be exported as CSV.


🔮 Future Scope
- Cloud integration for centralized attendance management.
- Mobile app support for remote access.
- AI improvements for mask detection and low-light accuracy.
- Multi-camera support for large classrooms/events.



