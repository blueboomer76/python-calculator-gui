import tkinter
from math import sqrt

# Root
calculator = tkinter.Tk()
calculator.geometry("400x350")

# Frames
home_screen = tkinter.Frame(calculator, width=600, height=300)
home_screen.grid_propagate(False)
home_screen.grid(row=0, column=0, sticky="nsew")
config_screen = tkinter.Frame(calculator)
config_screen.grid(row=0, column=0, sticky="nsew")

# Brings the home frame to the front
home_screen.tkraise()

def showHome():
    home_screen.tkraise()

def showConfig():
    config_screen.tkraise()

# -------------------------------------------
# Main screen
number_1 = None
operator = None
user_input = ""
calc_input = ""
calc_output = ""
memory = None
clear_next = False

# Calculator operations
def checkClear():
    global clear_next
    if clear_next:
        clearCalculator()
        clear_next = False

def clearCalculator():
    global number_1
    global operator
    global user_input
    global calc_input
    global calc_output
    number_1 = None
    operator = None
    user_input = ""
    calc_input = ""
    calc_output = ""
    input_label.config(text="")
    output_label.config(text="")

def onBackspaceClick():
    global user_input
    checkClear()
    if len(user_input) == 0:
        return
    user_input = user_input[:-1]
    input_label.config(text=calc_input+user_input)

def onMemorySetClick():
    global memory
    if len(calc_output) > 0:
        memory = float(calc_output)
    elif len(user_input) > 0:
        res = cleanUserInput()
        if res == False:
            return
        memory = user_input
    elif number_1 != None:
        memory = number_1

def onMemoryRecallClick():
    global user_input
    global memory
    if memory != None:
        checkClear()
        user_input = str(memory)
        input_label.config(text=calc_input+user_input)

def onPercentClick():
    global user_input
    global calc_output
    if len(user_input) > 0:
        res = cleanUserInput()
        if res == False:
            return
        if number_1 == None:
            calc_output = str(float(calc_output)/100)
            input_label.config(text=user_input+"% =")
            output_label.config(text=calc_output)
            user_input = ""
            clear_next = True
        else:
            user_input = str(float(user_input) / 100)
            input_label.config(text=calc_input+user_input)
    elif len(calc_output) > 0:
        input_label.config(text=calc_output+"% =")
        output_label.config(text=str(float(calc_output)/100))

def onNumpadClick(n):
    global user_input
    checkClear()
    user_input += str(n)
    input_label.config(text=calc_input+user_input)

def onSqrtClick():
    global user_input
    global calc_output
    if (number_1 != None and number_1 < 0):
        return
    if len(user_input) > 0:
        res = cleanUserInput()
        if res == False:
            return
        if number_1 == None:
            calc_output = str(sqrt(float(user_input)))
            input_label.config(text="√"+user_input+" =")
            output_label.config(text=calc_output)
            user_input = ""
            clear_next = True
        else:
            user_input = str(sqrt(float(user_input)))
            input_label.config(text=calc_input+user_input)
    elif len(calc_output) > 0:
        input_label.config(text="√"+calc_output+" =")
        output_label.config(text=str(sqrt(float(calc_output))))

def onSquareClick():
    global user_input
    global calc_output
    if len(user_input) > 0:
        res = cleanUserInput()
        if res == False:
            return
        if number_1 == None:
            calc_output = str(float(user_input) ** 2)
            input_label.config(text=user_input+"^2 =")
            output_label.config(text=calc_output)
            user_input = ""
            clear_next = True
        else:
            user_input = str(float(user_input) ** 2)
            input_label.config(text=calc_input+user_input)
    elif len(calc_output) > 0:
        input_label.config(text=calc_output+"^2 =")
        output_label.config(text=str(float(calc_output)**2))

def onOperatorClick(op):
    global number_1
    global operator
    global user_input
    global calc_input
    global clear_next
    if len(user_input) > 0:
        res = cleanUserInput()
        if res == False:
            return
        if number_1:
            number_1 = evalExpression(operator, number_1, float(user_input))
            calc_input = str(number_1) + " " + op + " "
        else:
            number_1 = float(user_input)
            calc_input = user_input + " " + op + " "
        user_input = ""
    elif len(calc_output) > 0:
        number_1 = float(calc_output)
        calc_input = calc_output + " " + op + " "
        user_input = ""
        clear_next = False
    else:
        calc_input = calc_input[:-3] + " " + op + " "
    operator = op
    input_label.config(text=calc_input+user_input)
        
def onSignClick():
    global user_input
    checkClear()
    if (len(user_input) > 0 and user_input[0] == "-"):
        user_input = user_input[1:]
    else:
        user_input = "-" + user_input
    input_label.config(text=calc_input+user_input)

def onDecimalClick():
    global user_input
    checkClear()
    new_user_input = user_input + "."
    if new_user_input.count(".") == 1:
        user_input = new_user_input
    input_label.config(text=calc_input+user_input)

def onEqualsButtonClick():
    global user_input
    global calc_output
    global clear_next
    if len(user_input) > 0:
        res = cleanUserInput()
        if res == False:
            return
        if number_1:
            input_label.config(text=calc_input+user_input+" =")
            calc_output = str(evalExpression(operator, number_1, float(user_input)))
        else:
            input_label.config(text=user_input+" =")
            calc_output = str(user_input)
        output_label.config(text=calc_output)
        user_input = ""
        clear_next = True

def cleanUserInput():
    global user_input
    if user_input[0] == "-":
        user_input = user_input[1:]
    if user_input[-1:] == ".":
        user_input = user_input[:-1]
    if len(user_input) > 0:
        return True
    else:
        return False

def evalExpression(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2

# Calculator widgets and buttons
calc_widgets = []
calc_buttons = {
    "C": clearCalculator,
    "<<": onBackspaceClick,
    "M": onMemorySetClick,
    "MR": onMemoryRecallClick,
    "%": onPercentClick,
    "7": lambda: onNumpadClick(7),
    "8": lambda: onNumpadClick(8),
    "9": lambda: onNumpadClick(9),
    "√x": onSqrtClick,
    "x^2": onSquareClick,
    "4": lambda: onNumpadClick(4),
    "5": lambda: onNumpadClick(5),
    "6": lambda: onNumpadClick(6),
    "-": lambda: onOperatorClick("-"),
    "/": lambda: onOperatorClick("/"),
    "1": lambda: onNumpadClick(1),
    "2": lambda: onNumpadClick(2),
    "3": lambda: onNumpadClick(3),
    "+": lambda: onOperatorClick("+"),
    "*": lambda: onOperatorClick("*"),
    "+/-": onSignClick,
    "0": lambda: onNumpadClick(n=0),
    ".": onDecimalClick
}

# Home UI widgets
theme_button = tkinter.Button(home_screen, text="Set Theme", command=showConfig)
theme_button.grid(column=0, row=0, columnspan=5)
calc_widgets.append(theme_button)
input_label = tkinter.Label(home_screen, text="This is the input", anchor="e")
input_label.grid(column=0, row=1, columnspan=5)
calc_widgets.append(input_label)
output_label = tkinter.Label(home_screen, text="This is the output", anchor="e", font=(None, 18))
output_label.grid(column=0, row=2, columnspan=5)
calc_widgets.append(output_label)

# Main calculator buttons
i = 0
row = 3
for key, value in calc_buttons.items():
    button = tkinter.Button(home_screen, text=key, width=8, height=2, command=value)
    button.grid(row=row, column=i)
    calc_widgets.append(button)
    i += 1
    if (i == 5):
        i = 0
        row += 1

equals_button = tkinter.Button(home_screen, text="=", width=18, height=2, command=onEqualsButtonClick)
equals_button.grid(row=7, column=3, columnspan=2)
calc_widgets.append(equals_button)

# -------------------------------------------
# Configuration screen
colors = ["R", "G", "B"]
default_colors = [
    {"name": "Dark", "bg": "black", "fg": "white"},
    {"name": "Light", "bg": "white", "fg": "black"}
]
dc_value = tkinter.IntVar(config_screen)
dc_value.set(1)

# Config operations
def changeThemeDefault():
    theme = default_colors[dc_value.get()]
    home_screen.config(bg=theme["bg"])
    config_screen.config(bg=theme["bg"])
    for cw in calc_widgets:
        cw.config(bg=theme["bg"], fg=theme["fg"])
    for cw in config_widgets:
        cw.config(bg=theme["bg"], fg=theme["fg"])

def changeThemeAdvanced():
    bg_values = []
    fg_values = []
    for i in range(3):
        try:
            bg_entry = entry_widgets[i].get()
            if bg_entry == "":
                bg_entry = 255
            bg_entry = int(bg_entry)
            if bg_entry > 255:
                raise ValueError
            fg_entry = entry_widgets[i+3].get()
            if fg_entry == "":
                fg_entry = 0
            fg_entry = int(fg_entry)
            if fg_entry > 255:
                raise ValueError
            bg_values.append(str(hex(bg_entry))[2:].zfill(2))
            fg_values.append(str(hex(fg_entry))[2:].zfill(2))
        except ValueError:
            advanced_note_label.config(text="ERROR: Invalid value")
            return
    
    bgcolor = "#" + "".join(bg_values)
    fgcolor = "#" + "".join(fg_values)
    home_screen.config(bg=bgcolor)
    config_screen.config(bg=bgcolor)
    for cw in calc_widgets:
        cw.config(bg=bgcolor, fg=fgcolor)
    for cw in config_widgets:
        cw.config(bg=bgcolor, fg=fgcolor)
    advanced_note_label.config(text="Enter numbers between 0-255.")

# Config widgets and buttons
config_widgets = []
entry_widgets = []

# Config UI widgets
# Default
return_button = tkinter.Button(config_screen, text="Return to home", command=showHome)
return_button.grid(row=0, column=0, columnspan=7)
config_widgets.append(return_button)
default_label = tkinter.Label(config_screen, text="---------- Default ----------")
default_label.grid(row=1, column=0, columnspan=7)
config_widgets.append(default_label)

config_row = 2
for theme in default_colors:
    radio_button = tkinter.Radiobutton(config_screen, text=theme["name"], variable=dc_value, value=config_row-2)
    radio_button.grid(row=config_row, column=0, columnspan=7)
    config_widgets.append(radio_button)
    config_row += 1

change_color_default_button = tkinter.Button(config_screen, text="Change color theme", command=changeThemeDefault)
change_color_default_button.grid(row=config_row, column=0, columnspan=7)
config_widgets.append(change_color_default_button)

# Advanced
advanced_label = tkinter.Label(config_screen, text="---------- Advanced ----------")
advanced_label.grid(row=config_row+1, column=0, columnspan=7)
config_widgets.append(advanced_label)
bg_label = tkinter.Label(config_screen, text="Background")
bg_label.grid(row=config_row+2, column=0)
config_widgets.append(bg_label)
fg_label = tkinter.Label(config_screen, text="Text color")
fg_label.grid(row=config_row+3, column=0)
config_widgets.append(fg_label)

for i in range(2,4):
    for j in range(6):
        if (j % 2 == 0):
            widget = tkinter.Label(config_screen, text=colors[int(j/2)])
        else:
            widget = tkinter.Entry(config_screen, width=10)
            entry_widgets.append(widget)
        widget.grid(row=config_row+i, column=j+1)
        config_widgets.append(widget)

change_color_advanced_button = tkinter.Button(config_screen, text="Change color theme", command=changeThemeAdvanced)
change_color_advanced_button.grid(row=config_row+4, column=0, columnspan=7)
config_widgets.append(change_color_advanced_button)
advanced_note_label = tkinter.Label(config_screen, text="Enter numbers between 0-255.")
advanced_note_label.grid(row=config_row+5, column=0, columnspan=7)
config_widgets.append(advanced_note_label)

calculator.mainloop()