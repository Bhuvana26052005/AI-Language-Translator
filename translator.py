import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip

def translate_text():
    try:
        # Get user input and selected target language
        source_text = text_input.get("1.0", tk.END).strip()
        target_lang = lang_choice.get()
        
        if not source_text:
            messagebox.showwarning("Input Error", "Please enter some text to translate.")
            return

        # Perform translation (automatically detects source language)
        translated = GoogleTranslator(source="auto", target=target_lang).translate(source_text)
        
        # Display the result in the output box
        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated)
        text_output.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

def copy_to_clipboard():
    translated_text = text_output.get("1.0", tk.END).strip()
    if translated_text:
        pyperclip.copy(translated_text)
        messagebox.showinfo("Success", "Text copied to clipboard!")

# --- UI Layout Setup ---
root = tk.Tk()
root.title("CodeAlpha AI - Language Translator")
root.geometry("500x460")
root.configure(bg="#f5f5f5")

# Header
tk.Label(root, text="AI Language Translator", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

# Input Box
tk.Label(root, text="Enter Text:", font=("Arial", 10, "bold"), bg="#f5f5f5").pack(anchor="w", padx=50)
text_input = tk.Text(root, height=4, width=50, font=("Arial", 10))
text_input.pack(pady=5)

# Language Dropdown Selection
tk.Label(root, text="Select Target Language:", font=("Arial", 10, "bold"), bg="#f5f5f5").pack(anchor="w", padx=50)
languages = ["spanish", "french", "german", "hindi", "arabic", "chinese (simplified)", "japanese"]
lang_choice = ttk.Combobox(root, values=languages, state="readonly", width=47)
lang_choice.set("spanish")
lang_choice.pack(pady=5)

# Translate Action Button
btn_translate = tk.Button(root, text="Translate Text", command=translate_text, bg="#007ACC", fg="white", font=("Arial", 10, "bold"), width=20)
btn_translate.pack(pady=15)

# Output Box
tk.Label(root, text="Translation Output:", font=("Arial", 10, "bold"), bg="#f5f5f5").pack(anchor="w", padx=50)
text_output = tk.Text(root, height=4, width=50, state=tk.DISABLED, bg="#e0e0e0", font=("Arial", 10))
text_output.pack(pady=5)

# Copy Button
btn_copy = tk.Button(root, text="📋 Copy to Clipboard", command=copy_to_clipboard, bg="#4CAF50", fg="white", font=("Arial", 9))
btn_copy.pack(pady=10)

root.mainloop()