from tkinter import*   #import every thing from tkinter
expression = ""        #globally declare the expression variable
def  press(num):    #function to update the expression in the entry box
    global expression  #point out the global expression
    expression = expression + str(num)  #concatenation of string
    equation.set(expression) #update the expression by using the set method
    def equalpress(): # function to evaluate the final expression
        try:            #for handling errors like zero and division errors
            global expression
            total = str(eval(expression))   #eval function to evaluate the expression
                                             #   & str function to convert the result into string
            equation.set(total)
            expression = ""  #initialize the expression variable by empting string
        except:                #if error is generated then handle with the except block
              equation.set("error")
              expression = ""
              def clear():      #function to clear the contents
                  global expression
                  expression = ""
                  equation.set("")

                 gui = Tk() #create a gui window  #Driver code
        gui.configure(background = "green") #set the background of gui wimdow
        gui.title("simple calc")
        gui.geometry(270*150) #set the configuration of gui window
        equation = StringVar() #StringVar() is the variable class
                               #we create an instance of this class
        expression_field = Entry(gui, textvariable=equation)
        expression_field.grid(columnspan=4, ipadx=70)  #use grid method for placing widgets at respective positions
        equation.set('enter your expression')
        #create buttons and place at a particular location
        #when button is pressed the function affiliated to that button is executed
        button1 = Button(gui, text='1', fg='black',bg='red',
                         command=lambda: press(1),height=(1), width=7)
        button1.grid(row=2, column=0)











