import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# ---------------- Student Data ----------------
students = {}
unique_subjects = set()

# ---------------- Grade Calculation ----------------


def calculate_grade(percentage):
    if percentage >= 95:
        return 'O'
    elif percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'D'

# ---------------- Add Student ----------------


def add_student():
    name = simpledialog.askstring("Add Student", "Enter student name:")
    if not name:
        return
    roll_no = simpledialog.askstring("Add Student", "Enter roll number:")
    if not roll_no:
        return
    subjects_str = simpledialog.askstring(
        "Add Student", "Enter subjects (comma separated):")
    if not subjects_str:
        return

    subjects = [s.strip() for s in subjects_str.split(',')]
    marks = []
    for sub in subjects:
        while True:
            try:
                mark = float(simpledialog.askstring(
                    "Marks Entry", f"Enter marks for {sub}:"))
                marks.append(mark)
                break
            except:
                messagebox.showerror("Error", "Enter a valid numeric value!")

    students[roll_no] = {"name": name, "subjects": subjects, "marks": marks}
    unique_subjects.update(subjects)
    messagebox.showinfo("Success", f"Student {name} added successfully!")
    view_students()

# ---------------- Edit Student ----------------


def edit_student(roll_no):
    if roll_no not in students:
        messagebox.showerror("Error", "Student not found!")
        return
    info = students[roll_no]
    name = simpledialog.askstring(
        "Edit Student", "Enter new name:", initialvalue=info['name'])
    if not name:
        return
    subjects_str = simpledialog.askstring("Edit Student", "Enter subjects (comma separated):",
                                          initialvalue=', '.join(info['subjects']))
    if not subjects_str:
        return
    subjects = [s.strip() for s in subjects_str.split(',')]
    marks = []
    for sub in subjects:
        while True:
            try:
                mark = float(simpledialog.askstring(
                    "Marks Entry", f"Enter marks for {sub}:",
                    initialvalue=str(info['marks'][info['subjects'].index(
                        sub)] if sub in info['subjects'] else "0")
                ))
                marks.append(mark)
                break
            except:
                messagebox.showerror("Error", "Enter a valid numeric value!")

    students[roll_no] = {"name": name, "subjects": subjects, "marks": marks}
    unique_subjects.update(subjects)
    messagebox.showinfo("Success", f"Student {name} updated successfully!")
    view_students()

# ---------------- Delete Student ----------------


def delete_student(roll_no):
    if roll_no in students:
        if messagebox.askyesno("Delete Student", f"Are you sure you want to delete {students[roll_no]['name']}?"):
            del students[roll_no]
            messagebox.showinfo("Deleted", "Student deleted successfully!")
            view_students()
    else:
        messagebox.showerror("Error", "Student not found!")

# ---------------- View Students ----------------


def view_students():
    for widget in table_frame.winfo_children():
        widget.destroy()

    columns = ("Roll No", "Name", "Subjects", "Marks",
               "Percentage", "Grade", "Actions")
    tree = ttk.Treeview(table_frame, columns=columns, show='headings')

    # Scrollbars
    vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    vsb.pack(side='right', fill='y')
    hsb.pack(side='bottom', fill='x')

    # Columns setup
    col_widths = {"Roll No": 80, "Name": 120, "Subjects": 200,
                  "Marks": 120, "Percentage": 100, "Grade": 80}
    for col in columns[:-1]:
        tree.heading(col, text=col)
        tree.column(col, width=col_widths.get(col, 100), anchor='center')

    # Populate data
    for roll, info in students.items():
        total = sum(info['marks'])
        percentage = total / len(info['marks'])
        grade = calculate_grade(percentage)
        subjects_str = ', '.join(info['subjects'])
        marks_str = ', '.join(str(m) for m in info['marks'])
        tree.insert('', tk.END, values=(roll, info['name'], subjects_str,
                                        marks_str, f"{percentage:.2f}", grade))

    # Right-click menu for edit/delete
    def on_right_click(event):
        item = tree.identify_row(event.y)
        if item:
            roll_no = tree.item(item, "values")[0]
            menu = tk.Menu(root, tearoff=0)
            menu.add_command(
                label="Edit", command=lambda: edit_student(roll_no))
            menu.add_command(
                label="Delete", command=lambda: delete_student(roll_no))
            menu.post(event.x_root, event.y_root)

    tree.bind("<Button-3>", on_right_click)
    tree.pack(fill=tk.BOTH, expand=True)


# ---------------- Search Student ----------------
def search_student():
    roll_no = simpledialog.askstring("Search Student", "Enter Roll Number:")
    if roll_no in students:
        info = students[roll_no]
        total = sum(info['marks'])
        percentage = total / len(info['marks'])
        grade = calculate_grade(percentage)
        result = f"Name: {info['name']}\n"
        for sub, mark in zip(info['subjects'], info['marks']):
            result += f"{sub}: {mark}\n"
        result += f"Percentage: {percentage:.2f}% | Grade: {grade}"
        messagebox.showinfo("Student Found", result)
    else:
        messagebox.showerror("Error", "Student not found!")

# ---------------- Display Topper ----------------


def display_topper():
    if not students:
        messagebox.showinfo("Info", "No student records found.")
        return
    topper_name = max(students.values(), key=lambda x: sum(
        x['marks'])/len(x['marks']))['name']
    max_percentage = max(sum(x['marks'])/len(x['marks'])
                         for x in students.values())
    messagebox.showinfo(
        "Class Topper", f"Class Topper: {topper_name} with {max_percentage:.2f}%")

# ---------------- Show Unique Subjects ----------------


def show_unique_subjects():
    if unique_subjects:
        messagebox.showinfo(
            "Unique Subjects", f"Unique Subjects Offered:\n{', '.join(unique_subjects)}")
    else:
        messagebox.showinfo("Unique Subjects", "No subjects found!")


# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Student Report Card System")
root.geometry("900x600")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Student Report Card System", font=(
    "Helvetica", 20, "bold"), bg="#f0f0f0").pack(pady=15)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

buttons = [
    ("Add Student", add_student),
    ("Search Student", search_student),
    ("Class Topper", display_topper),
    ("Unique Subjects", show_unique_subjects),
    ("Exit", root.destroy)
]

for i, (text, cmd) in enumerate(buttons):
    tk.Button(btn_frame, text=text, width=18, command=cmd, bg="#4caf50", fg="white",
              font=("Helvetica", 10, "bold")).grid(row=0, column=i, padx=5)

# Table frame
table_frame = tk.Frame(root, bg="#f0f0f0")
table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

view_students()  # Initial table
root.mainloop()
