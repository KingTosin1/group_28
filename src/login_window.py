"""
Login Window Module

This module defines the LoginWindow class for admin authentication.
"""

import customtkinter as ctk
from tkinter import messagebox

class LoginWindow:
    """
    Login window for admin authentication.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("Login - Student Grade Management System")
        self.window.geometry("400x500")
        self.window.resizable(False, False)

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Main frame for better styling
        main_frame = ctk.CTkFrame(self.window, corner_radius=15)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title
        self.title_label = ctk.CTkLabel(main_frame, text="Student Grade Management System",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=(30, 15))

        # Subtitle
        subtitle_label = ctk.CTkLabel(main_frame, text="Please log in to continue",
                                     font=ctk.CTkFont(size=12))
        subtitle_label.pack(pady=(0, 20))

        # Username frame
        username_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        username_frame.pack(pady=10, padx=40, fill="x")
        self.username_label = ctk.CTkLabel(username_frame, text="Username:", font=ctk.CTkFont(size=14))
        self.username_label.pack(anchor="w", pady=(10, 5))
        self.username_entry = ctk.CTkEntry(username_frame, placeholder_text="admin", height=35)
        self.username_entry.pack(fill="x", pady=(0, 10))
        self.username_entry.insert(0, "admin")

        # Password frame
        password_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        password_frame.pack(pady=10, padx=40, fill="x")
        self.password_label = ctk.CTkLabel(password_frame, text="Password:", font=ctk.CTkFont(size=14))
        self.password_label.pack(anchor="w", pady=(10, 5))
        self.password_entry = ctk.CTkEntry(password_frame, show="*", placeholder_text="password", height=35)
        self.password_entry.pack(fill="x", pady=(0, 10))
        self.password_entry.insert(0, "password")

        # Login button
        self.login_button = ctk.CTkButton(main_frame, text="Login", command=self.login, height=40, font=ctk.CTkFont(size=14, weight="bold"))
        self.login_button.pack(pady=(20, 15), padx=40, fill="x")

        # Error label
        self.error_label = ctk.CTkLabel(main_frame, text="", text_color="red", font=ctk.CTkFont(size=12))
        self.error_label.pack(pady=(0, 10))

    def login(self):
        """Handles login authentication."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.window.destroy()
            self.app.show_dashboard()
        else:
            self.error_label.configure(text="Invalid username or password.")
