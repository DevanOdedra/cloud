import tkinter as tk

def submit_registration():
    # Get input values from the form
    name = name_entry.get()
    course = course_entry.get()
    semester = semester_entry.get()
    # ... (other fields)

    # Save the data to an Azure database or file storage
    # You can use Azure SQL Database, Azure Blob Storage, or other services.

root = tk.Tk()
root.title("Student Registration Form")

# Create form fields
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)
course_label = tk.Label(root, text="Course:")
course_entry = tk.Entry(root)
semester_label = tk.Label(root, text="Semester:")
semester_entry = tk.Entry(root)
# ... (other fields)

submit_button = tk.Button(root, text="Submit", command=submit_registration)

# Arrange form elements using grid layout
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
course_label.grid(row=1, column=0)
course_entry.grid(row=1, column=1)
semester_label.grid(row=2, column=0)
semester_entry.grid(row=2, column=1)
# ... (other fields)

submit_button.grid(row=6, columnspan=2)

root.mainloop()
