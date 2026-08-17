"""A small text reader made with only Python's standard library.

Pasted text and .txt files are supported fully.  PDF text extraction below is
only a very basic attempt: many PDFs store text in compressed or unusual forms,
so their text cannot be read reliably without a PDF library.
"""

import os
import re
import subprocess
import sys
import tempfile
import tkinter as tk
from tkinter import filedialog


class ReadItOutApp:
    #Keep the interface and its actions together in one simple class.

    def __init__(self, window):
        self.window = window
        self.speech_process = None
        self.temp_speech_file = None

        window.title("Read It Out")
        #window.icomiconbitmap(default="info")
        window.geometry("760x560")
        window.minsize(620, 460)

        title = tk.Label(window, text="Read It Out", font=("Arial", 22, "bold"))
        title.pack(pady=(15, 4))

        instructions = tk.Label(
            window,
            text="Paste text below, or choose a .txt file. PDF reading is a basic attempt only.",
            font=("Arial", 12),
        )
        instructions.pack(pady=(0, 10))

        text_frame = tk.Frame(window)
        text_frame.pack(fill="both", expand=True, padx=20)

        self.text_box = tk.Text(text_frame, wrap="word", font=("Arial", 14), height=14)
        scroll_bar = tk.Scrollbar(text_frame, command=self.text_box.yview)
        self.text_box.configure(yscrollcommand=scroll_bar.set)
        self.text_box.pack(side="left", fill="both", expand=True)
        scroll_bar.pack(side="right", fill="y")

        buttons = tk.Frame(window)
        buttons.pack(pady=14)

        button_options = {"font": ("Arial", 13, "bold"), "padx": 12, "pady": 8}
        tk.Button(buttons, text="Choose .txt File", command=self.open_text_file, **button_options).grid(
            row=0, column=0, padx=5, pady=4
        )
        tk.Button(buttons, text="Choose PDF File", command=self.open_pdf_file, **button_options).grid(
            row=0, column=1, padx=5, pady=4
        )
        tk.Button(buttons, text="Read Aloud", command=self.read_aloud, **button_options).grid(
            row=0, column=2, padx=5, pady=4
        )
        tk.Button(buttons, text="Stop", command=self.stop_reading, **button_options).grid(
            row=0, column=3, padx=5, pady=4
        )

        self.status = tk.StringVar(value="Ready. Add text, then click Read Aloud.")
        tk.Label(window, textvariable=self.status, font=("Arial", 12), anchor="w").pack(
            fill="x", padx=20, pady=(0, 14)
        )

        window.protocol("WM_DELETE_WINDOW", self.close_window)

    def put_text_in_box(self, text):
        """Replace the text box contents with text loaded from a file."""
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert("1.0", text)

    def open_text_file(self):
        """Let the user choose a normal plain-text file."""
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not filename:
            return

        try:
            # utf-8-sig also handles text files saved with a UTF-8 BOM.
            with open(filename, "r", encoding="utf-8-sig") as text_file:
                self.put_text_in_box(text_file.read())
            self.status.set("Loaded text file: " + os.path.basename(filename))
        except (OSError, UnicodeDecodeError) as error:
            self.status.set("Could not open that text file: " + str(error))

    def open_pdf_file(self):
        """Try to find simple, uncompressed text inside a PDF.

        This intentionally does not claim to be a real PDF reader.  PDF files
        often compress or encode their text, which needs a dedicated PDF library.
        """
        filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if not filename:
            return

        try:
            with open(filename, "rb") as pdf_file:
                raw_pdf = pdf_file.read()

            # Some very simple PDFs contain visible text inside parentheses.
            # Decoding as latin-1 never fails, but it is not a reliable PDF decoder.
            possible_text = re.findall(r"\(([^()]*)\)", raw_pdf.decode("latin-1"))
            text = " ".join(self.clean_pdf_piece(piece) for piece in possible_text)
            text = re.sub(r"\s+", " ", text).strip()

            if text:
                self.put_text_in_box(text)
                self.status.set(
                    "Basic PDF attempt completed. Please check the text; many PDFs will not work."
                )
            else:
                self.status.set(
                    "No simple text was found. This PDF may be compressed, scanned, or encoded."
                )
        except OSError as error:
            self.status.set("Could not open that PDF: " + str(error))

    @staticmethod
    def clean_pdf_piece(piece):
        """Remove a few common PDF escape characters from a text fragment."""
        return piece.replace(r"\n", " ").replace(r"\r", " ").replace(r"\t", " ").replace(r"\(", "(").replace(r"\)", ")")

    def read_aloud(self):
        """Use an operating-system voice when one is available.

        Python's standard library has no cross-platform text-to-speech feature.
        Windows and macOS include voice commands, so this program uses them via
        subprocess. Linux users receive an honest status message instead.
        """
        text = self.text_box.get("1.0", tk.END).strip()
        if not text:
            self.status.set("Please paste text or choose a file first.")
            return

        self.stop_reading(update_status=False)

        try:
            if sys.platform.startswith("win"):
                environment = os.environ.copy()
                environment["READ_IT_OUT_TEXT"] = text
                command = (
                    "Add-Type -AssemblyName System.Speech; "
                    "$voice = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
                    "$voice.Speak($env:READ_IT_OUT_TEXT)"
                )
                self.speech_process = subprocess.Popen(
                    ["powershell", "-NoProfile", "-Command", command], env=environment
                )
            elif sys.platform == "darwin":
                # A temporary file avoids putting a long paragraph on the command line.
                temporary_file = tempfile.NamedTemporaryFile(
                    mode="w", encoding="utf-8", suffix=".txt", delete=False
                )
                temporary_file.write(text)
                temporary_file.close()
                self.temp_speech_file = temporary_file.name
                self.speech_process = subprocess.Popen(["say", "-f", self.temp_speech_file])
            else:
                self.status.set(
                    "Read Aloud is not built in on this system. Pasted text and .txt files still work."
                )
                return

            self.status.set("Reading aloud... Click Stop to end it.")
            self.window.after(300, self.check_speech_finished)
        except (OSError, subprocess.SubprocessError) as error:
            self.status.set("Could not start the system voice: " + str(error))

    def check_speech_finished(self):
        """Update the status after the voice process ends."""
        if self.speech_process and self.speech_process.poll() is None:
            self.window.after(300, self.check_speech_finished)
        elif self.speech_process:
            self.speech_process = None
            self.remove_temp_file()
            self.status.set("Finished reading.")

    def stop_reading(self, update_status=True):
        """Stop the voice process when the operating system allows it."""
        if self.speech_process and self.speech_process.poll() is None:
            self.speech_process.terminate()
            self.speech_process = None
            self.remove_temp_file()
            if update_status:
                self.status.set("Reading stopped.")
        elif update_status:
            self.status.set("Nothing is currently being read.")

    def remove_temp_file(self):
        """Delete the temporary macOS speech file after it is no longer needed."""
        if self.temp_speech_file:
            try:
                os.remove(self.temp_speech_file)
            except OSError:
                pass
            self.temp_speech_file = None

    def close_window(self):
        self.stop_reading(update_status=False)
        self.window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    ReadItOutApp(root)
    root.mainloop()
