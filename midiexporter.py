import os
import sys
import sv_ttk
import secrets
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

def select_soundfont():
    soundfont_path = filedialog.askopenfilename(title="Select SoundFont file", filetypes=[("SoundFont files", "*.sf2")])
    soundfont_entry.delete(0, tk.END)
    soundfont_entry.insert(tk.END, soundfont_path)

def select_midi():
    midi_path = filedialog.askopenfilename(title="Select MIDI file", filetypes=[("MIDI files", "*.mid")])
    midi_entry.delete(0, tk.END)
    midi_entry.insert(tk.END, midi_path)

def convert_to_mp3():
    soundfont_path = soundfont_entry.get()
    midi_path = midi_entry.get()
    output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

    if soundfont_path and midi_path and output_path:
        token = secrets.token_urlsafe(16)

        subprocess.Popen(f'{application_path}\\fluidsynth\\fluidsynth.exe -F "%temp%\\{token}.wav" -ni "{soundfont_path}" "{midi_path}"', shell = True).wait()
        subprocess.Popen(f'{application_path}\\ffmpeg\\bin\\ffmpeg.exe -i "%temp%\\{token}.wav" -acodec mp3 "{output_path}"', shell = True).wait()
        subprocess.Popen(f'del %temp%\\{token}.wav', shell = True).wait()
    else:
        status_label.config(text="Please select SoundFont, MIDI, and output path.")

root = tk.Tk()
root.iconbitmap(application_path + "\\midi.ico")
root.title("Fire's MIDI to MP3 Exporter")

ttk.Label(root, text="Select SoundFont file:").grid(row=0, column=0, padx=5, pady=5)
soundfont_entry = ttk.Entry(root, width=50)
soundfont_entry.grid(row=0, column=1, padx=5, pady=40)
soundfont_button = ttk.Button(root, text="Browse", command=select_soundfont)
soundfont_button.grid(row=0, column=2, padx=5, pady=5)

ttk.Label(root, text="Select MIDI file:").grid(row=1, column=0, padx=5, pady=5)
midi_entry = ttk.Entry(root, width=50)
midi_entry.grid(row=1, column=1, padx=5, pady=5)
midi_button = ttk.Button(root, text="Browse", command=select_midi)
midi_button.grid(row=1, column=2, padx=5, pady=5)

convert_button = ttk.Button(root, text="Convert to MP3", command=convert_to_mp3)
convert_button.grid(row=2, column=1, padx=5, pady=5)

status_label = ttk.Label(root, text="")
status_label.grid(row=3, column=1, padx=5, pady=15)

sv_ttk.set_theme("dark")

root.resizable(False, False)
root.mainloop()
