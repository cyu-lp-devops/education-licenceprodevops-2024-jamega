from tkinter import Label, Button, Checkbutton, Tk, IntVar, Entry, StringVar, DISABLED, NORMAL
import tkinter.ttk as ttk
from random import choice, randint

lowercase_letters = [chr(i) for i in range(97, 123)]
uppercase_letters = [chr(i) for i in range(65, 91)]
numbers = [chr(i) for i in range(48, 58)]
special_characters = ['%', '_', '-', '!', '$', '^', '&', '#', '(', ')', '[', ']', '=', '@']

class PasswordGenerator:
    def __init__(self, window):
        self.window = window
        window.geometry('450x350')
        window.title('Password Generator')
        window.resizable(1, 0)

        Label(window, text="Number of characters:").place(x=5, y=5)
        self.num_characters = IntVar(window, value=20)
        self.n = Entry(window, width=3, textvariable=self.num_characters)
        self.n.place(x=140, y=6)

        Label(window, text="Alphabets to include:").place(x=5, y=40)
        self.checkLowercase = IntVar(value=1)
        self.lowercase = Checkbutton(window, text='Lowercase letters:\n' + ', '.join(lowercase_letters), variable=self.checkLowercase, width=56)
        self.lowercase.place(x=0, y=60)

        self.checkUppercase = IntVar(value=1)
        self.uppercase = Checkbutton(window, text='Uppercase letters:\n' + ', '.join(uppercase_letters), variable=self.checkUppercase, width=60)
        self.uppercase.place(x=0, y=100)

        self.checkNumbers = IntVar(value=1)
        self.numbers = Checkbutton(window, text='Numbers: ' + ', '.join(numbers), variable=self.checkNumbers, width=35)
        self.numbers.place(x=0, y=140)

        self.checkSpecialChars = IntVar(value=1)
        self.special_chars = Checkbutton(window, text='Special characters: ' + ', '.join(special_characters), variable=self.checkSpecialChars, width=49)
        self.special_chars.place(x=0, y=160)

        self.checkCustom = IntVar(value=0)
        self.custom_chars = StringVar()
        self.customCheck = Checkbutton(window, text='Custom characters:', variable=self.checkCustom, width=18, command=self.toggle_custom)
        self.customCheck.place(x=0, y=200)
        self.customEntry = Entry(window, width=30, textvariable=self.custom_chars, state=DISABLED)
        self.customEntry.place(x=160, y=205)
        Label(window, text='(in sequence, without commas)').place(x=25, y=230)

        generate_button = Button(window, text='Generate', width=15, font=('Tahoma', 10), command=self.generate_password)
        generate_button.place(x=170, y=250)
        
        self.generated_pwd = StringVar()
        self.result_label = Label(self.window, textvariable=self.generated_pwd)
        self.result_label.place(x=5, y=280)

        self.copy_to_clipboard_button = Button(self.window, text='Copy to clipboard', width=20, font=('Tahoma', 10), command=self.copy_to_clipboard)
        self.copy_to_clipboard_button.place(x=150, y=300)
        self.copy_to_clipboard_button.config(state=DISABLED)

    def toggle_custom(self):
        if self.checkCustom.get() == 1:
            self.customEntry.config(state=NORMAL)
        else:
            self.customEntry.config(state=DISABLED)

    def generate_password(self):
        n = int(self.n.get())
        lowercase = int(self.checkLowercase.get())
        uppercase = int(self.checkUppercase.get())
        numbers = int(self.checkNumbers.get())
        special_chars = int(self.checkSpecialChars.get())
        custom = int(self.checkCustom.get())

        self.style = dict()
        i = 0
        
        if lowercase == 1:
            self.style[i] = lowercase_letters
            i += 1
        if uppercase == 1:
            self.style[i] = uppercase_letters
            i += 1
        if numbers == 1:
            self.style[i] = numbers
            i += 1
        if special_chars == 1:
            self.style[i] = special_characters
            i += 1
        if custom == 1 and self.custom_chars.get().strip():
            self.style[i] = list(self.custom_chars.get().strip())
            i += 1

        if i == 0:
            self.generated_pwd.set("Please select at least one type of character.")
            self.copy_to_clipboard_button.config(state=DISABLED)
            return

        self.pwd = ''.join(choice(self.style[randint(0, i - 1)]) for _ in range(n))
        
        self.generated_pwd.set('Generated password: ' + self.pwd)
        self.copy_to_clipboard_button.config(state=NORMAL)

    def copy_to_clipboard(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.pwd)
        self.window.update()

root = Tk()
app = PasswordGenerator(root)
root.mainloop()
