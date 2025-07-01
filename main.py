# main.py
import tkinter as tk
from tkinter import messagebox
from generator import generate_text_animation

def on_generate():
    title = title_entry.get().strip()
    content = text_input.get("1.0", tk.END).strip()
    if not title or not content:
        messagebox.showerror("Error", "Please enter both title and text.")
        return

    lines = content.split("\n")
    try:
        output_file = generate_text_animation(title, lines)
        messagebox.showinfo("Success", f"Video saved at:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate video:\n{str(e)}")

# === GUI Setup ===
window = tk.Tk()
window.title("Text Animation Generator")
window.geometry("500x400")
window.configure(bg="#f0f4f8")

tk.Label(window, text="🎥 Enter Video Title", font=("Segoe UI", 12, "bold"), bg="#f0f4f8").pack(pady=10)
title_entry = tk.Entry(window, width=50)
title_entry.pack()

tk.Label(window, text="📝 Enter Text (each line will animate)", font=("Segoe UI", 12), bg="#f0f4f8").pack(pady=10)
text_input = tk.Text(window, height=8, width=60)
text_input.pack()

tk.Button(window, text="✨ Generate Video", command=on_generate, bg="#2ecc71", fg="white", font=("Segoe UI", 11)).pack(pady=20)

window.mainloop()
