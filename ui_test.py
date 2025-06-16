import tkinter as tk
from tkinter import filedialog, messagebox
import data_reader as dr

# select files
def select_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

# select output folder
def select_folder(entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

# data reader script runner
def run_data_mage():
    members_file = entry_members.get()
    attendance_file = entry_attendance.get()
    output_dir = entry_output.get()
    
    if not members_file or not attendance_file or not output_dir:
        messagebox.showerror("Error", "Please select both files and the output directory.")
        return

    try:
        dr.data_mage(members_file, attendance_file, output_dir)
        messagebox.showinfo("Success", "Files processed successfully.")
        root.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        root.destroy()

def center_window(root, width=600, height=250):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

def run_gui():
    global root
    global entry_members
    global entry_attendance
    global entry_output
    
    # create the main window
    root = tk.Tk()
    root.title("Data Mage")

    # center the window
    center_window(root)

    # create and place the labels and entries for file selection
    tk.Label(root, text="Select Members File:").grid(row=0, column=0, padx=10, pady=5)
    entry_members = tk.Entry(root, width=50)
    entry_members.grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_file(entry_members)).grid(row=0, column=2, padx=10, pady=5)

    tk.Label(root, text="Select Attendance File:").grid(row=1, column=0, padx=10, pady=5)
    entry_attendance = tk.Entry(root, width=50)
    entry_attendance.grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_file(entry_attendance)).grid(row=1, column=2, padx=10, pady=5)

    tk.Label(root, text="Select Output Directory:").grid(row=2, column=0, padx=10, pady=5)
    entry_output = tk.Entry(root, width=50)
    entry_output.grid(row=2, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: select_folder(entry_output)).grid(row=2, column=2, padx=10, pady=5)

    # create and place the run button
    tk.Button(root, text="Run Attendance Script", command=run_data_mage).grid(row=3, column=1, pady=20)

    # run the application
    root.mainloop()
