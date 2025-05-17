import tkinter as tk
import os

def start_update():
    # Get the absolute path to updater.exe
    updater_path = os.path.join(os.path.dirname(__file__),"updater.exe")

    if os.path.exists(updater_path):
        try:
            root.after(2000,root.destroy)
            os.startfile(updater_path)
        except Exception as e:
            print(f"Failed to start updater: {e}")
    else:
        print("Updater not found at:", updater_path)

root = tk.Tk()
root.title("Main")
root.geometry("200x100")

tk.Button(root, text="Update", command=start_update).pack(pady=20)

root.mainloop()

# add this code into your main file and make sure file type (eg: .py,.exe)
# You can make this code into def fuction and access it by button & etc..
