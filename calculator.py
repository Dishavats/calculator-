import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("340x550")
root.resizable(False, False)
root.configure(bg='#FFF4A3')

# Global variables
num1 = ''
num2 = ''
operator = None

# Display
display = tk.Entry(root, font=("Ink Free", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def get_number(number):
    global num1, num2, operator
    if operator is None:
        num1 += str(number)
        display.delete(0, tk.END)
        display.insert(tk.END, num1)
    else:
        num2 += str(number)
        display.delete(0, tk.END)
        display.insert(tk.END, num2)

def get_operator(op):
    global operator, num1, num2
    if num1 == '':
        return
    if num2 != '':
        equal()
    operator = op
    display.delete(0, tk.END)

def equal():
    global num1, num2, operator
    if num1 == '' or num2 == '':
        return
    try:
        n1 = float(num1)
        n2 = float(num2)
    except ValueError:
        return
    
    total = None
    if operator == '+':
        total = n1 + n2
    elif operator == '-':
        total = n1 - n2
    elif operator == '*':
        total = n1 * n2
    elif operator == '/':
        total = n1 / n2

    if total is not None:
        display.delete(0, tk.END)
        display.insert(tk.END, str(total))
        num1 = str(total)
        num2 = ''
        operator = None

def clear_display():
    global num1, num2, operator
    num1 = ''
    num2 = ''
    operator = None
    display.delete(0, tk.END)

def delete_last():
    global num1, num2, operator
    if operator is None:
        num1 = num1[:-1]
        display.delete(0, tk.END)
        display.insert(tk.END, num1)
    else:
        num2 = num2[:-1]
        display.delete(0, tk.END)
        display.insert(tk.END, num2)

# Create Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+',
    'C', 'Del', 'Exit'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=("Ink Free", 18), 
                  bg='#FFD1A0', command=equal).grid(row=row, column=col, columnspan=2, sticky='nsew')
        col += 2
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=("Ink Free", 18), 
                  bg='#FFD1A0', command=clear_display).grid(row=row, column=col, sticky='nsew')
        col += 1
    elif button == 'Del':
        tk.Button(root, text=button, padx=20, pady=20, font=("Ink Free", 18), 
                  bg='#FFD1A0', command=delete_last).grid(row=row, column=col, sticky='nsew')
        col += 1
    elif button == 'Exit':
        tk.Button(root, text=button, padx=20, pady=20, font=("Ink Free", 18), 
                  bg='#FFD1A0', command=root.quit).grid(row=row, column=col, sticky='nsew')
        col += 1
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Ink Free", 18), 
                  bg='#FFD1A0', command=lambda b=button: get_number(b) if b.isdigit() or b == '.' else get_operator(b)
                  ).grid(row=row, column=col, sticky='nsew')
        col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
