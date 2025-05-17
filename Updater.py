import tkinter as tk
from tkinter import messagebox
import requests, zipfile, io, os, shutil
import sys

# Configuration
GITHUB_ZIP_URL = "https://github.com/username/repo/releases/latest/download/update.zip"
APP_DIR = os.path.abspath("..")  # one folder up from updater
TEMP_DIR = "temp_update"

def download_and_extract():
    try:
        status_label.config(text="Downloading...")
        response = requests.get(GITHUB_ZIP_URL, stream=True)
        response.raise_for_status()

        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(TEMP_DIR)

        status_label.config(text="Download complete. Updating...")
        replace_files()
        cleanup()
        messagebox.showinfo("Update", "Update completed successfully.")
        root.quit()

    except zipfile.BadZipFile:
        messagebox.showerror("Error", "Downloaded file is not a valid ZIP.")
    except Exception as e:
        messagebox.showerror("Error", f"Update failed: {e}")

def replace_files():
    for root_dir, dirs, files in os.walk(TEMP_DIR):
        rel_path = os.path.relpath(root_dir, TEMP_DIR)
        target_path = os.path.join(APP_DIR, rel_path)

        if not os.path.exists(target_path):
            os.makedirs(target_path)

        for file in files:
            src_file = os.path.join(root_dir, file)
            dst_file = os.path.join(target_path, file)
            shutil.copy2(src_file, dst_file)

def cleanup():
    shutil.rmtree(TEMP_DIR, ignore_errors=True)

# UI Setup
root = tk.Tk()
root.title("Updater")
root.geometry("300x120")

tk.Label(root, text="Software Updater", font=("Arial", 14)).pack(pady=10)
status_label = tk.Label(root, text="Ready to update", fg="blue")
status_label.pack()

tk.Button(root, text="Update Now", command=download_and_extract).pack(pady=10)

root.mainloop()
