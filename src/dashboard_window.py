"""
Dashboard Window Module

This module defines the DashboardWindow class for the main application hub.
"""

import customtkinter as ctk

class DashboardWindow:
    """
    Main dashboard window with navigation buttons.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("Dashboard - Student Grade Management System")
        self.window.geometry("800x600")

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Main container
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True)

        # Sidebar
        sidebar_frame = ctk.CTkFrame(main_frame, width=200, corner_radius=0)
        sidebar_frame.pack(side="left", fill="y")

        # Sidebar title
        sidebar_title = ctk.CTkLabel(sidebar_frame, text="Navigation",
                                    font=ctk.CTkFont(size=16, weight="bold"))
        sidebar_title.pack(pady=(20, 10))

        # Navigation buttons in sidebar
        self.student_btn = ctk.CTkButton(sidebar_frame, text="Manage Students",
                                        command=self.app.show_student_management, height=40)
        self.student_btn.pack(pady=5, padx=10, fill="x")

        self.course_btn = ctk.CTkButton(sidebar_frame, text="Manage Courses",
                                       command=self.app.show_course_management, height=40)
        self.course_btn.pack(pady=5, padx=10, fill="x")

        self.grade_btn = ctk.CTkButton(sidebar_frame, text="Enter Grades",
                                      command=self.app.show_grade_entry, height=40)
        self.grade_btn.pack(pady=5, padx=10, fill="x")

        self.gpa_btn = ctk.CTkButton(sidebar_frame, text="View GPA/CGPA",
                                    command=self.app.show_gpa_display, height=40)
        self.gpa_btn.pack(pady=5, padx=10, fill="x")

        self.charts_btn = ctk.CTkButton(sidebar_frame, text="View Charts",
                                       command=self.app.show_charts, height=40)
        self.charts_btn.pack(pady=5, padx=10, fill="x")

        self.pdf_btn = ctk.CTkButton(sidebar_frame, text="Export PDF",
                                    command=self.app.show_pdf_export, height=40)
        self.pdf_btn.pack(pady=5, padx=10, fill="x")

        # Logout button in sidebar
        self.logout_btn = ctk.CTkButton(sidebar_frame, text="Logout",
                                       command=self.logout, fg_color="red", hover_color="darkred", height=40)
        self.logout_btn.pack(pady=(20, 10), padx=10, fill="x")

        # Main content area
        content_frame = ctk.CTkFrame(main_frame, corner_radius=0)
        content_frame.pack(side="right", fill="both", expand=True)

        # Title in content
        self.title_label = ctk.CTkLabel(content_frame, text="Student Grade Management System",
                                       font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        # Subtitle
        self.subtitle_label = ctk.CTkLabel(content_frame, text="Dashboard",
                                          font=ctk.CTkFont(size=16))
        self.subtitle_label.pack(pady=(0, 20))

        # Status info
        self.status_label = ctk.CTkLabel(self.window,
                                        text=f"Students: {len(self.app.students)} | Courses: {len(self.app.courses)} | Grades: {len(self.app.grades)}")
        self.status_label.pack(pady=(0, 10))

    def logout(self):
        """Logs out and returns to login."""
        self.window.destroy()
        self.app.show_login()
