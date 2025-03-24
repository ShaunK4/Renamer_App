import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import logging
import customtkinter as ctk
from renamer import file_operations

def select_excel_file(excel_entry: ctk.CTkEntry) -> None:
    try:
        excel_file = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if not excel_file:
            return
        excel_entry.delete(0, tk.END)
        excel_entry.insert(0, excel_file)
    except Exception as e:
        logging.error("Error selecting Excel file: %s", e)

def select_image_directory(image_entry: ctk.CTkEntry) -> None:
    try:
        image_directory = filedialog.askdirectory()
        if not image_directory:
            return
        image_entry.delete(0, tk.END)
        image_entry.insert(0, image_directory)
    except Exception as e:
        logging.error("Error selecting directory: %s", e)

def start_renaming(excel_entry: ctk.CTkEntry, image_entry: ctk.CTkEntry, output_text: scrolledtext.ScrolledText) -> None:
    try:
        excel_file = excel_entry.get()
        image_directory = image_entry.get()
        if not excel_file and not image_directory:
            messagebox.showwarning("Selection Required", "Please select an Excel file and a directory before starting.")
            return
        elif not excel_file:
            messagebox.showwarning("Selection Required", "Please select an Excel file before starting.")
            return
        elif not image_directory:
            messagebox.showwarning("Selection Required", "Please select a directory before starting.")
            return

        filename_mapping = file_operations.read_excel_table(excel_file)
        output_text.delete('1.0', tk.END)
        file_operations.rename_files(image_directory, filename_mapping, output_text)
    except Exception as e:
        output_text.insert(tk.END, f"Error starting renaming process: {e}\n")

def export_template(output_text: scrolledtext.ScrolledText) -> None:
    file_operations.export_template(output_text)

def run_app() -> None:
    # Initialize the app window using customtkinter.
    app = ctk.CTk()
    app.geometry("800x400")
    ctk.set_appearance_mode("dark")
    app.title("Renamer")
    app.wm_iconbitmap('icon.ico')

    # Frame for Excel file selection.
    excel_frame = ctk.CTkFrame(app)
    excel_frame.pack(pady=5)
    excel_label = ctk.CTkLabel(excel_frame, text="Select Excel File:")
    excel_label.pack(side=tk.LEFT)
    excel_entry = ctk.CTkEntry(excel_frame, width=200)
    excel_entry.pack(side=tk.LEFT, padx=5)
    excel_button = ctk.CTkButton(excel_frame, text="Browse", command=lambda: select_excel_file(excel_entry))
    excel_button.pack(side=tk.LEFT)
    export_template_button = ctk.CTkButton(excel_frame, text="Export Template", command=lambda: export_template(output_text))
    export_template_button.pack(side=tk.LEFT, padx=5)

    # Frame for image directory selection.
    image_frame = ctk.CTkFrame(app)
    image_frame.pack(pady=5)
    image_label = ctk.CTkLabel(image_frame, text="Select Directory for File Renaming:")
    image_label.pack(side=tk.LEFT)
    image_entry = ctk.CTkEntry(image_frame, width=200)
    image_entry.pack(side=tk.LEFT, padx=5)
    image_button = ctk.CTkButton(image_frame, text="Browse", command=lambda: select_image_directory(image_entry))
    image_button.pack(side=tk.LEFT)

    # Start renaming button.
    start_button = ctk.CTkButton(app, text="Start Renaming", command=lambda: start_renaming(excel_entry, image_entry, output_text))
    start_button.pack(pady=5)

    # Frame for output text.
    output_frame = ctk.CTkFrame(app)
    output_frame.pack(pady=5)
    output_label = ctk.CTkLabel(output_frame, text="Renaming Process Output:")
    output_label.pack()
    output_text = scrolledtext.ScrolledText(output_frame, height=30, width=200, bg="#F8F8FF")
    output_text.pack()
    output_text.tag_config('error', foreground='red')

    app.mainloop()
