from tkinter import*
expression = ""
def input_number(number, equation):
    #accessing the global expression variable
    global expression
    #concatenation of string
    expression = expression + str(number)
    equation.set(expression)
    def clear_input_field(equation):
        global expression
        expression = ""
        #setting empty field in the input field
        equation.set("Enter the expression")
        def evaluate(equation):
            global  expression
            #trying to evaluate the expression
            try:
                result = str(eval(expression))
                equation.set(result)
                expression = ""
                def main():
                    window.title("calculator")
