import goslate
import tkinter as tk

gs = goslate.Goslate()
french_text = ""


class TranslateWindow():
    """A class that requires a tkinter window to be passed, allows the translation of text from english to french."""

    def __init__(self, window):
        window.title("English to French Translator")
        window.geometry("500x500")
        window.config(bg="green")

        title_frame = tk.Frame(root, bg="white")
        title_frame.pack(padx=5, pady=5)

        title_text = tk.Label(title_frame, text="French Translator", font=("Rubrik", 30), bg="green")
        title_text.pack()

        main_frame = tk.Frame(root, bg="dark green")
        main_frame.pack(padx=5, pady=5)

        convert_frame = tk.Frame(root, bg="green")
        convert_frame.pack(padx=5, pady=20)

        english_label = tk.Label(main_frame, text="Please enter the English to be translated:", font=("Rubrik", 15), bg="dark green")
        english_label.grid(row=0, column=0)

        english_entry = tk.Entry(main_frame, font=("Rubrik", 15), width=44)
        english_entry.grid(row=1, column=0)

        output_text = tk.Label(root, text="", font=("Rubrik", 15), bg="green")
        output_text.pack(padx=5, pady=10)

        def convert_text(text):
            global french_text
            french_text = gs.translate(text, "fr")
            output_text.config(text=french_text)

        convert_button = tk.Button(convert_frame, text="Convert", font=("Rubrik", 25), command=lambda:convert_text(english_entry.get()))
        convert_button.grid(row=2, column=0)


if __name__ == "__main__":
    root = tk.Tk()
    TranslateWindow(root)
    root.mainloop()
