"""
Main Entry Point for Student Grade Management System

This script initializes the application, loads data, and starts the GUI.
"""

import customtkinter as ctk
from src.storage import load_students, load_courses, load_grades, save_students, save_courses, save_grades
from src.student import Student
from src.course import Course
from src.grade import Grade
from src.login_window import LoginWindow
from src.dashboard_window import DashboardWindow
from src.student_management_window import StudentManagementWindow
from src.course_management_window import CourseManagementWindow
from src.grade_entry_window import GradeEntryWindow
from src.gpa_display_window import GPADisplayWindow
from src.charts_window import ChartsWindow
from src.pdf_export_dialog import PDFExportDialog

class App:
    """
    Main application class handling GUI and data management.
    """

    def __init__(self):
        # Set appearance mode and color theme
        ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

        self.root = ctk.CTk()
        self.root.title("Student Grade Management System")
        self.root.geometry("800x600")
        self.root.withdraw()  # Hide main window initially

        # Load data
        self.students = load_students()
        self.courses = load_courses()
        self.grades = load_grades()

        # Show login on start
        self.show_login()

    def save_data(self):
        """Saves all data to CSV files."""
        save_students(self.students)
        save_courses(self.courses)
        save_grades(self.grades)

    def show_login(self):
        """Shows the login window."""
        LoginWindow(self.root, self)

    def show_dashboard(self):
        """Shows the dashboard window."""
        DashboardWindow(self.root, self)

    def show_student_management(self):
        """Shows the student management window."""
        StudentManagementWindow(self.root, self)

    def show_course_management(self):
        """Shows the course management window."""
        CourseManagementWindow(self.root, self)

    def show_grade_entry(self):
        """Shows the grade entry window."""
        GradeEntryWindow(self.root, self)

    def show_gpa_display(self):
        """Shows the GPA display window."""
        GPADisplayWindow(self.root, self)

    def show_charts(self):
        """Shows the charts window."""
        ChartsWindow(self.root, self)

    def show_pdf_export(self):
        """Shows the PDF export dialog."""
        PDFExportDialog(self.root, self)

    def run(self):
        """Starts the main event loop."""
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()