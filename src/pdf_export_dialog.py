"""
PDF Export Dialog Module

This module defines the PDFExportDialog class for exporting PDF reports.
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
from src.pdf_report import generate_student_report

class PDFExportDialog:
    """
    Dialog for selecting student and exporting PDF report.
    """

    def __init__(self, root, app_instance):
        self.root = root
        self.app = app_instance
        self.window = ctk.CTkToplevel(root)
        self.window.title("Export PDF Report")
        self.window.geometry("400x250")

        # Center the window
        self.window.transient(root)
        self.window.grab_set()

        # Main frame
        main_frame = ctk.CTkFrame(self.window, corner_radius=10)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title
        title_label = ctk.CTkLabel(main_frame, text="Export PDF Report",
                                  font=ctk.CTkFont(size=16, weight="bold"))
        title_label.pack(pady=(20, 10))

        # Student selection
        student_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        student_frame.pack(pady=10, padx=20, fill="x")
        student_label = ctk.CTkLabel(student_frame, text="Select Student:")
        student_label.pack(anchor="w", pady=(10, 5))
        self.student_var = ctk.StringVar()
        self.student_combo = ctk.CTkComboBox(student_frame, variable=self.student_var,
                                            values=[f"{s.student_id} - {s.name}" for s in self.app.students])
        self.student_combo.pack(fill="x", pady=(0, 10))

        # Filename
        filename_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        filename_frame.pack(pady=10, padx=20, fill="x")
        filename_label = ctk.CTkLabel(filename_frame, text="Filename:")
        filename_label.pack(anchor="w", pady=(10, 5))
        self.filename_entry = ctk.CTkEntry(filename_frame, placeholder_text="student_report.pdf")
        self.filename_entry.insert(0, "student_report.pdf")
        self.filename_entry.pack(fill="x", pady=(0, 10))

        # Export button
        export_button = ctk.CTkButton(main_frame, text="Export PDF", command=self.export_pdf, height=35)
        export_button.pack(pady=(10, 20), padx=20, fill="x")

    def export_pdf(self):
        """Exports the PDF report."""
        selected = self.student_var.get()
        if not selected:
            messagebox.showerror("Error", "Please select a student.")
            return
        student_id = selected.split(" - ")[0]
        student = next((s for s in self.app.students if s.student_id == student_id), None)
        if not student:
            messagebox.showerror("Error", "Student not found.")
            return

        filename = self.filename_entry.get()
        if not filename:
            messagebox.showerror("Error", "Please enter a filename.")
            return

        grades = [g for g in self.app.grades if g.student_id == student_id]
        generate_student_report(student, grades, self.app.courses, filename)
        messagebox.showinfo("Success", f"PDF exported to {filename}")
        self.window.destroy()
