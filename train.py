
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        top_img_path = r"C:\Face Recognition Software\5EERFPimg\t1.png"
        if os.path.exists(top_img_path):
            img_top = Image.open(top_img_path).resize((1530, 325), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            Label(self.root, image=self.photoimg_top).place(x=0, y=55, width=1530, height=325)

        Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
               font=("times new roman", 30, "bold"), bg="red", fg="white").place(x=0, y=380, width=1530, height=60)

        bottom_img_path = r"C:\Face Recognition Software\5EERFPimg\t2.png"
        if os.path.exists(bottom_img_path):
            img_bottom = Image.open(bottom_img_path).resize((1530, 325), Image.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            Label(self.root, image=self.photoimg_bottom).place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        try:
            data_dir = "data"
            if not os.path.exists(data_dir):
                messagebox.showerror("Error", "Data directory not found!", parent=self.root)
                return

            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png'))]

            if not path:
                messagebox.showerror("Error", "No images found in data directory!", parent=self.root)
                return

            faces, ids = [], []

            for image in path:
                img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)  # Load as grayscale
                if img is None:
                    continue
                # Ensure image is resized to 200x200 (consistent with dataset generation)
                img_resized = cv2.resize(img, (200, 200), interpolation=cv2.INTER_LINEAR)
                try:
                    id = int(os.path.split(image)[1].split('.')[1])  # Extract student ID
                except (IndexError, ValueError):
                    messagebox.showerror("Error", f"Invalid filename format for {image}. Expected format: user.ID.img_id.jpg", parent=self.root)
                    return

                faces.append(img_resized)
                ids.append(id)
                cv2.imshow("Training", img_resized)
                cv2.waitKey(100)
                if cv2.waitKey(1) & 0xFF == 13:  # Press Enter to exit
                    break

            ids = np.array(ids)

            # Train classifier with LBPHFaceRecognizer
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training dataset completed!", parent=self.root)

            # Clear the current layout and create a new frame
            for widget in self.root.winfo_children():
                widget.destroy()
            self.create_new_frame()

        except Exception as e:
            cv2.destroyAllWindows()
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)

    def create_new_frame(self):
        title_lbl = Label(self.root, text="TRAINING COMPLETED", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        success_msg = Label(self.root, text="The dataset has been successfully trained!\nYou can now proceed with face recognition.",
                           font=("times new roman", 20, "bold"), bg="white", fg="black")
        success_msg.place(x=500, y=200, width=530, height=100)

        Button(self.root, text="BACK", command=self.reset_to_initial, cursor="hand2",
               font=("times new roman", 20, "bold"), bg="blue", fg="white").place(x=650, y=350, width=200, height=50)

    def reset_to_initial(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()