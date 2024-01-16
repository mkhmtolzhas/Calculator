import tkinter as tk
from pynput import keyboard
import sys

def on_key_event(key, entry):
    try:
        value = key.char
        if value.isdigit() or value in "+-*/":
            entry.insert("end", value)
    except AttributeError:
        # Не-char клавиша
        pass

def click(value, entry):
    e = entry.get()
    try:
        if value == "=":
            answer = eval(e)
            entry.delete(0, "end")
            entry.insert(0, answer)
        elif value == "C":
            e = e[0: len(e)-1]
            entry.delete(0, "end")
            entry.insert(0, e)
        elif value == "CE":
            entry.delete(0, "end")
        elif value ==  "√":
            entry.delete(0, "end")
            entry.insert(0, eval(e)**0.5)
        elif value ==  "x²":
            entry.delete(0, "end")
            entry.insert(0, eval(e)**2)
        else:
            entry.insert("end", value)
            
    except (SyntaxError, ZeroDivisionError):
        entry.delete(0, "end")

def main():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("365x486+100+100")
    root.config(bg="black")

    entry = tk.Entry(root, font=("arial", 20, "bold"), bg="black", fg="white", bd=10, width=30)
    entry.grid(row=0, column=0, columnspan=16)

    buttons = ["C", "CE", "√", "x²",
               "1", "2", "3", "+", 
               "4", "5", "6", "-",
               "7", "8", "9", "*",
               "=", "0", " ", "/"]
    row_buttons = 1
    column_buttons = 0

    for i in buttons:
        button = tk.Button(root, width=5, height=2, bd=2, text=i, bg="black", fg="white", font=("arial", 18, "bold"), command=lambda button=i, entry=entry: click(button, entry))
        button.grid(row=row_buttons, column=column_buttons, pady=1)
        column_buttons += 1
        if column_buttons > 3:
            row_buttons += 1
            column_buttons = 0

    # Регистрируем обработчик клавиш
    listener = keyboard.Listener(on_press=lambda key: on_key_event(key, entry))
    listener.start()

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "console":
        # Запускаем код в консольном режиме (для отладки и т.д.)
        main()
    else:
        # Запускаем код в режиме приложения, избегая вывода в консоль
        sys.stdout = open("NUL", "w")
        sys.stderr = open("NUL", "w")
        main()