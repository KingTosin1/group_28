"""
Course Management Window Module

This module defines the CourseManagementWindow class for CRUD operations on courses.
"""

import customtkinter as ctk
from tkinter import messagebox, ttk
from src.course import Course

class CourseManagementWindow:
    """
    Window for managing courses (add, edit, delete, view).
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("Course Management")
        self.window.geometry("800x800")
        self.window.resizable(True, True)

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Scrollable frame for entire content
        self.main_scrollable = ctk.CTkScrollableFrame(self.window)
        self.main_scrollable.pack(fill="both", expand=True, padx=10, pady=10)

        # Title
        self.title_label = ctk.CTkLabel(self.main_scrollable, text="Course Management",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Search frame
        search_frame = ctk.CTkFrame(self.main_scrollable, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=(0, 10))
        search_label = ctk.CTkLabel(search_frame, text="Search:")
        search_label.pack(side="left", padx=(0, 10))
        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search courses...")
        self.search_entry.pack(side="left", fill="x", expand=True)
        self.search_entry.bind('<KeyRelease>', self.search_courses)

        # Scrollable frame for courses
        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_scrollable)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Add button
        self.add_btn = ctk.CTkButton(self.main_scrollable, text="Add New Course", command=self.show_add_form, height=40)
        self.add_btn.pack(pady=(0, 20), padx=20, fill="x")

        # Form frame (hidden initially)
        self.form_frame = ctk.CTkFrame(self.main_scrollable)

        self.form_title = ctk.CTkLabel(self.form_frame, text="", font=ctk.CTkFont(size=16, weight="bold"))
        self.form_title.pack(pady=(10, 5))

        # Form fields
        fields_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        fields_frame.pack(fill="x", padx=20, pady=10)

        self.code_label = ctk.CTkLabel(fields_frame, text="Course Code:")
        self.code_label.pack(anchor="w", pady=(10, 0))
        self.code_entry = ctk.CTkEntry(fields_frame)
        self.code_entry.pack(fill="x", pady=(0, 10))

        self.name_label = ctk.CTkLabel(fields_frame, text="Name:")
        self.name_label.pack(anchor="w", pady=(10, 0))
        self.name_entry = ctk.CTkEntry(fields_frame)
        self.name_entry.pack(fill="x", pady=(0, 10))

        self.credits_label = ctk.CTkLabel(fields_frame, text="Credit Units:")
        self.credits_label.pack(anchor="w", pady=(10, 0))
        self.credits_entry = ctk.CTkEntry(fields_frame)
        self.credits_entry.pack(fill="x", pady=(0, 10))

        self.semester_label = ctk.CTkLabel(fields_frame, text="Semester:")
        self.semester_label.pack(anchor="w", pady=(10, 0))
        self.semester_entry = ctk.CTkEntry(fields_frame)
        self.semester_entry.pack(fill="x", pady=(0, 10))

        # Buttons
        button_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=(0, 10))

        self.save_btn = ctk.CTkButton(button_frame, text="Save", command=self.save_course, height=35)
        self.save_btn.pack(side="left", padx=(0, 10))

        self.cancel_btn = ctk.CTkButton(button_frame, text="Cancel", command=self.cancel_edit,
                                       fg_color="gray", hover_color="darkgray", height=35)
        self.cancel_btn.pack(side="left")

        # Load courses
        self.load_courses()

        # Editing state
        self.editing_course = None

    def load_courses(self):
        """Loads courses into card-style layout."""
        # Clear existing cards
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for course in self.app.courses:
            self.create_course_card(course)

    def create_course_card(self, course):
        """Creates a card for a course."""
        card = ctk.CTkFrame(self.scrollable_frame, corner_radius=10)
        card.pack(fill="x", padx=10, pady=5)

        # Course info
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(fill="x", padx=10, pady=10)

        code_label = ctk.CTkLabel(info_frame, text=f"Code: {course.code}",
                                 font=ctk.CTkFont(weight="bold"))
        code_label.pack(anchor="w")

        name_label = ctk.CTkLabel(info_frame, text=f"Name: {course.name}")
        name_label.pack(anchor="w")

        credits_label = ctk.CTkLabel(info_frame, text=f"Credits: {course.credit_units}")
        credits_label.pack(anchor="w")

        semester_label = ctk.CTkLabel(info_frame, text=f"Semester: {course.semester}")
        semester_label.pack(anchor="w")

        # Buttons
        button_frame = ctk.CTkFrame(card, fg_color="transparent")
        button_frame.pack(fill="x", padx=10, pady=(0, 10))

        edit_btn = ctk.CTkButton(button_frame, text="Edit", width=80,
                                command=lambda c=course: self.show_edit_form(c))
        edit_btn.pack(side="left", padx=(0, 5))

        delete_btn = ctk.CTkButton(button_frame, text="Delete", width=80, fg_color="red", hover_color="darkred",
                                  command=lambda c=course: self.delete_course(c))
        delete_btn.pack(side="left")

    def show_add_form(self):
        """Shows the form for adding a new course."""
        self.editing_course = None
        self.form_title.configure(text="Add New Course")
        self.code_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.credits_entry.delete(0, "end")
        self.semester_entry.delete(0, "end")
        self.form_frame.pack(fill="x", padx=20, pady=(0, 20))

    def show_edit_form(self, course):
        """Shows the form for editing a course."""
        self.editing_course = course
        self.form_title.configure(text="Edit Course")
        self.code_entry.delete(0, "end")
        self.code_entry.insert(0, course.code)
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, course.name)
        self.credits_entry.delete(0, "end")
        self.credits_entry.insert(0, str(course.credit_units))
        self.semester_entry.delete(0, "end")
        self.semester_entry.insert(0, course.semester)
        self.form_frame.pack(fill="x", padx=20, pady=(0, 20))

    def save_course(self):
        """Saves the course data."""
        code = self.code_entry.get().strip()
        name = self.name_entry.get().strip()
        credits_str = self.credits_entry.get().strip()
        semester = self.semester_entry.get().strip()

        if not code or not name or not credits_str or not semester:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            credits = int(credits_str)
            course = Course(code, name, credits, semester)
            if self.editing_course:
                # Update existing
                for i, c in enumerate(self.app.courses):
                    if c.code == self.editing_course.code:
                        self.app.courses[i] = course
                        break
            else:
                # Check for duplicate code
                if any(c.code == code for c in self.app.courses):
                    messagebox.showerror("Error", "Course code already exists.")
                    return
                self.app.courses.append(course)
            self.app.save_data()
            self.load_courses()
            self.cancel_edit()
            messagebox.showinfo("Success", "Course saved successfully!")
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
        self.editing_course = None

    def delete_course(self, course):
        """Deletes the selected course."""
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete {course.name}?"):
            self.app.courses.remove(course)
            self.app.grades = [g for g in self.app.grades if g.course_code != course.code]  # Remove grades too
            self.app.save_data()
            self.load_courses()
            messagebox.showinfo("Success", "Course deleted successfully!")

    def search_courses(self, event):
        """Filters courses based on search query."""
        query = self.search_entry.get().lower()
        # Clear existing cards
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for course in self.app.courses:
            if query in course.name.lower() or query in course.code.lower():
                self.create_course_card(course)
