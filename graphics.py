import tkinter as tk
from utils import is_palindrome


def launch_palindrome_gui():
    def on_text_change(*args):
        user_input = entry_var.get()
        if user_input.strip() == '':
            result_label.config(text='Waiting for input...', fg='gray')
            return

        if is_palindrome(user_input):
            result_label.config(
                text=f'{user_input} is a palindrome!', fg='green')
        else:
            result_label.config(
                text=f'{user_input} is not a palindrome!', fg='red')

    # Set up Window
    root = tk.Tk()
    root.title('Real-TimePalindrome Checker')
    root.geometry('400x200')

    # Entry box
    entry_var = tk.StringVar()
    entry_var.trace_add('write', on_text_change)

    entry_label = tk.Label(root, text='Type something:')
    entry_label.pack(pady=(20, 5))

    entry = tk.Entry(root, textvariable=entry_var,
                     font=('Helvetica', 16), width=30)
    entry.pack()

    # Result label
    result_label = tk.Label(
        root, text='Waiting for input...', font=('Helvetica', 16))
    result_label.pack(pady=20)

    root.mainloop()
