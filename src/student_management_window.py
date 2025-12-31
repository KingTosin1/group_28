"""
Student Management Window Module

This module defines the StudentManagementWindow class for managing students.
"""

import customtkinter as ctk
from tkinter import messagebox
from src.student import Student

class StudentManagementWindow:
    """
    Window for adding, editing, and deleting students.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("Student Management")
        self.window.geometry("800x1200")
        self.window.resizable(True, True)

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Scrollable frame for entire content
        self.main_scrollable = ctk.CTkScrollableFrame(self.window)
        self.main_scrollable.pack(fill="both", expand=True, padx=10, pady=10)

        # Title
        self.title_label = ctk.CTkLabel(self.main_scrollable, text="Student Management",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Search frame
        search_frame = ctk.CTkFrame(self.main_scrollable, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=(0, 10))
        search_label = ctk.CTkLabel(search_frame, text="Search:")
        search_label.pack(side="left", padx=(0, 10))
        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search students...")
        self.search_entry.pack(side="left", fill="x", expand=True)
        self.search_entry.bind('<KeyRelease>', self.search_students)

        # Scrollable frame for students
        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_scrollable)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Add button
        self.add_btn = ctk.CTkButton(self.main_scrollable, text="Add New Student", command=self.show_add_form, height=40)
        self.add_btn.pack(pady=(0, 20), padx=20, fill="x")

        # Form frame (hidden initially)
        self.form_frame = ctk.CTkFrame(self.main_scrollable)

        self.form_title = ctk.CTkLabel(self.form_frame, text="", font=ctk.CTkFont(size=16, weight="bold"))
        self.form_title.pack(pady=(10, 5))

        # Form fields
        fields_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        fields_frame.pack(fill="x", padx=20, pady=10)

        self.id_label = ctk.CTkLabel(fields_frame, text="Student ID:")
        self.id_label.pack(anchor="w", pady=(10, 0))
        self.id_entry = ctk.CTkEntry(fields_frame)
        self.id_entry.pack(fill="x", pady=(0, 10))

        self.name_label = ctk.CTkLabel(fields_frame, text="Name:")
        self.name_label.pack(anchor="w", pady=(10, 0))
        self.name_entry = ctk.CTkEntry(fields_frame)
        self.name_entry.pack(fill="x", pady=(0, 10))

        self.email_label = ctk.CTkLabel(fields_frame, text="Email:")
        self.email_label.pack(anchor="w", pady=(10, 0))
        self.email_entry = ctk.CTkEntry(fields_frame)
        self.email_entry.pack(fill="x", pady=(0, 10))

        # Buttons
        button_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=(0, 10))

        self.save_btn = ctk.CTkButton(button_frame, text="Save", command=self.save_student, height=35)
        self.save_btn.pack(side="left", padx=(0, 10))

        self.cancel_btn = ctk.CTkButton(button_frame, text="Cancel", command=self.cancel_edit,
                                       fg_color="gray", hover_color="darkgray", height=35)
        self.cancel_btn.pack(side="left")

        # Load students
        self.load_students()

        # Editing state
        self.editing_student = None

    def load_students(self):
        """Loads students into card-style layout."""
        # Clear existing cards
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for student in self.app.students:
            self.create_student_card(student)

    def create_student_card(self, student):
        """Creates a card for a student."""
        card = ctk.CTkFrame(self.scrollable_frame, corner_radius=10)
        card.pack(fill="x", padx=10, pady=5)

        # Student info
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(fill="x", padx=10, pady=10)

        id_label = ctk.CTkLabel(info_frame, text=f"ID: {student.student_id}",
                               font=ctk.CTkFont(weight="bold"))
        id_label.pack(anchor="w")

        name_label = ctk.CTkLabel(info_frame, text=f"Name: {student.name}")
        name_label.pack(anchor="w")

        email_label = ctk.CTkLabel(info_frame, text=f"Email: {student.email}")
        email_label.pack(anchor="w")

        # Buttons
        button_frame = ctk.CTkFrame(card, fg_color="transparent")
        button_frame.pack(fill="x", padx=10, pady=(0, 10))

        edit_btn = ctk.CTkButton(button_frame, text="Edit", width=80,
                                command=lambda s=student: self.show_edit_form(s))
        edit_btn.pack(side="left", padx=(0, 5))

        delete_btn = ctk.CTkButton(button_frame, text="Delete", width=80, fg_color="red", hover_color="darkred",
                                  command=lambda s=student: self.delete_student(s))
        delete_btn.pack(side="left")

    def show_add_form(self):
        """Shows the form for adding a new student."""
        self.editing_student = None
        self.form_title.configure(text="Add New Student")
        self.id_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.form_frame.pack(fill="x", padx=20, pady=(0, 20))

    def show_edit_form(self, student):
        """Shows the form for editing a student."""
        self.editing_student = student
        self.form_title.configure(text="Edit Student")
        self.id_entry.delete(0, "end")
        self.id_entry.insert(0, student.student_id)
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, student.name)
        self.email_entry.delete(0, "end")
        self.email_entry.insert(0, student.email)
        self.form_frame.pack(fill="x", padx=20, pady=(0, 20))

    def save_student(self):
        """Saves the student data."""
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()

        if not student_id or not name or not email:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            if self.editing_student:
                # Update existing
                self.editing_student.student_id = student_id
                self.editing_student.name = name
                self.editing_student.email = email
                self.editing_student.validate()
            else:
                # Add new
                student = Student(student_id, name, email)
                student.validate()
                self.app.students.append(student)
            self.app.save_data()
            self.load_students()
            self.cancel_edit()
            messagebox.showinfo("Success", "Student saved successfully!")
            # Scroll to top to show updated list
            try:
                self.main_scrollable._parent_canvas.yview_moveto(0)
            except:
                pass
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def cancel_edit(self):
        """Cancels editing and hides the form."""
        self.form_frame.pack_forget()
        self.editing_student = None

    def delete_student(self, student):
        """Deletes the selected student."""
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete {student.name}?"):
            self.app.students.remove(student)
            self.app.save_data()
            self.load_students()
            messagebox.showinfo("Success", "Student deleted successfully!")

    def search_students(self, event):
        """Filters students based on search query."""
        query = self.search_entry.get().lower()
        # Clear existing cards
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for student in self.app.students:
            if query in student.name.lower() or query in student.student_id.lower():
                self.create_student_card(student)
