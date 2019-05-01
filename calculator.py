import tkinter

# Root
calculator = tkinter.Tk()
calculator.geometry("600x300")

# Frames
home_screen = tkinter.Frame(calculator, bg="blue", width=600, height=300)
home_screen.grid_propagate(False)
home_screen.grid(row=0, column=0, sticky="nsew")
config_screen = tkinter.Frame(calculator, bg="red")
config_screen.grid(row=0, column=0, sticky="nsew")

# Brings the home frame to the front
home_screen.tkraise()

def showHome():
    home_screen.tkraise()

def showConfig():
    config_screen.tkraise()

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
    if len(calc_output) != 0:
        memory = float(calc_output)
    elif len(user_input) != 0:
        if user_input[-1:] == ".":
            memory = float(user_input[:-1])
        else:
            memory = float(user_input)
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
    pass

def onNumpadClick(n):
    global user_input
    checkClear()
    user_input += str(n)
    input_label.config(text=calc_input+user_input)

def onSqrtClick():
    pass

def onSquareClick():
    pass

def onOperatorClick(op):
    global user_input
    global calc_input
    global number_1
    global operator
    if len(user_input) > 0:
        if user_input[-1:] == ".":
            user_input = user_input[:-1]
        if number_1:
            number_1 = evalExpression(operator, number_1, float(user_input))
            calc_input = str(number_1) + " " + op + " "
        else:
            number_1 = float(user_input)
            calc_input = user_input + " " + op + " "
        user_input = ""
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
        if user_input[-1:] == ".":
            user_input = user_input[:-1]
        if number_1:
            input_label.config(text=calc_input+user_input+" =")
            calc_output = str(evalExpression(operator, number_1, float(user_input)))
        else:
            input_label.config(text=user_input+" =")
            calc_output = str(user_input)
        output_label.config(text=calc_output)
        clear_next = True

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

calculator.mainloop()