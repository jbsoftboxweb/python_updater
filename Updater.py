import tkinter as tk
from tkinter import messagebox, ttk
import requests, zipfile, io, os, shutil, sys, psutil
import subprocess

# ======= CONFIG ========
GITHUB_ZIP_URL = "https://github.com/jbsoftboxweb/python_updater/releases/download/tesing/updater.zip"
APP_DIR = os.path.abspath("")  # Folder of main app
TEMP_DIR = "temp_update"
# =======================

def download_with_progress(url, dest_label, progress_bar):
    """Download file with progress bar"""
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total = int(response.headers.get('content-length', 0))
    downloaded = 0
    buffer = io.BytesIO()

    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            buffer.write(chunk)
            downloaded += len(chunk)
            percent = int((downloaded / total) * 100)
            progress_bar["value"] = percent
            dest_label.config(text=f"Downloading... {percent}%")
            root.update_idletasks()

    buffer.seek(0)
    print("download")
    return buffer

def extract_and_replace(zip_data):
    """Extract and replace app files"""
    with zipfile.ZipFile(zip_data) as zip_ref:
        zip_ref.extractall(TEMP_DIR)

    for root_dir, _, files in os.walk(TEMP_DIR):
        rel_path = os.path.relpath(root_dir, TEMP_DIR)
        target_dir = os.path.join(APP_DIR, rel_path)

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        for file in files:
            shutil.copy2(os.path.join(root_dir, file), os.path.join(target_dir, file))
        
        print("Replace")

def start_update():
    try:
        status_label.config(text="Preparing to download...")
        zip_data = download_with_progress(GITHUB_ZIP_URL, status_label, progress)
        status_label.config(text="Extracting files...")
        extract_and_replace(zip_data)
        cleanup()
        status_label.config(text="Update complete!")
        messagebox.showinfo("Success", "Update completed.")
        root.destroy()
    except Exception as e:
        messagebox.showerror("Update Failed", str(e))

def cleanup():
    shutil.rmtree(TEMP_DIR, ignore_errors=True)

# === UI Setup ===
root = tk.Tk()
root.title("Software Updater")
root.geometry("350x160")
root.resizable(False, False)

tk.Label(root, text="Updater", font=("Arial", 14)).pack(pady=10)
status_label = tk.Label(root, text="Ready to update", fg="blue")
status_label.pack(pady=5)

progress = ttk.Progressbar(root, orient="horizontal", length=280, mode="determinate")
progress.pack(pady=5)

tk.Button(root, text="Start Update", command=start_update).pack(pady=10)

root.mainloop()
