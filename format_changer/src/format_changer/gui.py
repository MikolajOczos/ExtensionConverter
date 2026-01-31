import tkinter as tk
from tkinter import filedialog, messagebox
from docx2pdf import convert
from pdf2docx import *
import os
import shutil
import time


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Converter")
        self.root.geometry("800x500")
        self.file_path = None
        
        
        tk.Label(root, text=" Drag & Drop", font=("Arial", 16, "bold")).pack(pady=20)
        
        
        self.drop_box = tk.Label(
            root,
            text="Drag file here or click to browse",
            font=("Arial", 12),
            bg="lightgray",
            width=40,
            height=8,
            relief="solid",
            borderwidth=2
        )
        self.drop_box.pack(pady=20)
        self.drop_box.bind("<Button-1>", self.browse_file)
        
        
        self.convert_btn = tk.Button(
            root,
            text="Convert",
            command= self.convert_file,
            font=("Arial", 12),
            state="disabled"
        )
        self.convert_btn.pack(pady=10)
        
        
        self.status = tk.Label(root, text="No file selected", fg="gray")
        self.status.pack()
    
    def browse_file(self, event=None):
        file_path = filedialog.askopenfilename(
            title="Select a document",
            filetypes=[("Word files", "*.docx"), ("Pdf files", "*.pdf"), ("All files", "*.*")]
        )
        if file_path:
            self.set_file(file_path)
    def set_file(self, file_path):
        self.file_path = file_path
        self.filename = os.path.basename(file_path)
        self.drop_box.config(
            text=f" {self.filename}Click to change",
            bg="lightgreen"
        )
        self.convert_btn.config(state="normal")
        self.status.config(text=f"Selected: {self.filename}", fg="green")
    
    def convert_file(self):
        try:
                self.status.config(text="Converting...", fg="blue")
                self.root.update()  
                self.status.config(text="Created")
                if self.filename.endswith(".docx"):
                    messagebox.showinfo("Success", f"PDF created successfully!")
                    self.converted_file = convert(self.file_path)
                elif self.filename.endswith(".pdf"):
                    output_docx = os.path.splitext(self.file_path)[0] + ".docx"
                    cv = Converter(self.file_path)
                    self.converted_file = cv.convert(output_docx)
                    messagebox.showinfo("Success", f"WORD created successfully!")           
        except Exception as e:
            self.status.config(text=f"Error: {str(e)}", fg="red")
            messagebox.showerror("Error", str(e))

    def show_converted_file(self):
        if self.converted_file:
            self.downloadspace = tk.Label(
                root,
                text= "Download your document here",
                fg="blue",
                cursor="hand2", 
                font=("Arial", 10, "underline")
            )               
root = tk.Tk()
app = GUI(root)
root.mainloop()