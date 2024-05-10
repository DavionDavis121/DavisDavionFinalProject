from tkinter import *
from tkinter import messagebox as msg
from PIL import Image, ImageTk


def openNewWindow():
    #Defines the formula to convert Celsius to Fahrenheit
    def Celsius_to_Fahrenheit(Celsius):
        return (1.8) * Celsius + 32   
    
    #Defines the formula to convert Fahrenheit to Celsius
    def Fahrenheit_to_Celsius(Fahrenheit):
        return (0.55) * (Fahrenheit - 32)
    #Introduces an try statement, if a certain parameter isn't met with deciding the temperature type it will print that there was an invalid user input. 
    def convert_temperature():
        try:
            temperature = float(entry.get())
            if temperature_type.get() == "Celsius":
                result = Celsius_to_Fahrenheit(temperature)
                result_label.config(text =f"{temperature} Celsius is {result:.2f} Fahrenehit")
            else:
                result = Fahrenheit_to_Celsius(temperature)
                result_label.config(text = f"{temperature} Fahrenheit is {result:.2f} Celsius")
        except ValueError:
            result_label.config(text = "Invalid User input. Please enter a valid number.")

    #Creates a new window using Toplevel
    NewWindow = Toplevel(master_window)

    #Sets the title of Toplevel widget
    NewWindow.title("Dave's Temperature conversion app")

    #Sets the geometry of Toplevel
    NewWindow.geometry('290x250')
    
    #Label widget to show in Toplevel
    Label(NewWindow, text = "Temperature Conversion", fg = '#62a1c7', bg = '#95d6ea', font = ('bold, 14')).pack()

    #Configures window color
    NewWindow.configure(bg = '#95d6ea')

    #RadioButtons to include Fahrenheit or Celsius
    temperature_type = StringVar(value = 'Celsius')
    celc = Radiobutton(NewWindow, text = 'Convert from Fahrenheit to Celsius', variable = temperature_type, value = 'celc', )  
    celc.pack()
    
    #Displays the Enter Temperature label
    label = Label(NewWindow, text = "Enter Temperature:")
    label.configure(font= ("Courier", 8))
    label.pack()
    
    #Allows the user to input integers 
    entry = Entry(NewWindow)
    entry.pack()

    #Convert button acts as an enter key and allows the program to process the number
    convert_btn = Button(NewWindow, text = "Convert", command = convert_temperature)
    convert_btn.pack()
    
    #Defines the reset button to allow the user to reset the entry box
    def clearFunc():
        entry.delete(0,"end")

    #Reset button allows user to delete inputted integers 
    reset = Button(NewWindow,text = "Reset", command = clearFunc)
    reset.pack(side = BOTTOM,padx= 5, pady=5)

    #Result label outputs
    result_label = Label(NewWindow, text = "")
    result_label.pack()
    
    
    #Displays  message upon closing app
    def on_closing():
        if msg.askokcancel("Quit", "Do you want to quit?"):
            NewWindow.destroy()
    NewWindow.protocol("WM_DELETE_WINDOW", on_closing)

def openNewWindow2():
    #Creates a new window using Toplevel
    NewWindow = Toplevel(master_window)

    #Sets the title of Toplevel widget
    NewWindow.title("Dave's Recommendation App")

    #Sets the geometry of Toplevel
    NewWindow.geometry('850x350')

    #Sets the background color of the TopLevel Window
    NewWindow.configure(bg = '#95d6ea')

    #Welcome screen exit button
    btn2 = Button(NewWindow, text = "Exit", command = exit)
    btn2.pack(expand = True, side = BOTTOM)

    #Label widget
    label2 = Label(NewWindow, text = "Clothing Recommendation based off temperature:")
    label2.configure(font= ("Courier", 8))
    label2.pack()

    #Textbox widget. The textbox will display messages and depending on the temperature achieved from the above code, the user will decide what items to wear. 
    label3 = Label(NewWindow, text = "If your recorded temperature was <= 50 but not exceeding 30 degrees Fahreneheit we recommend you wear."
                   "  A Jacket, Gloves, Trainers.")
    label3.pack(pady = 10, padx= 10)
    label4 = Label(NewWindow, text = "If your recorded temperature was <= 30 degrees Fahreneheit we recommend you wear."
                   "  A toboggan, Winter Jacket, Gloves, boots.")
    label4.pack(pady = 15, padx = 15)
    label5 = Label(NewWindow, text = "If your recorded temperature was >= 55 but not exceeding 75 degrees Fahreneheit we recommend you wear."
                   "  A Linen Shirt, Shorts, Tennis shoes.")
    label5.pack(pady = 20, padx = 20)
    label6 = Label(NewWindow, text = "If your recorded temperature was >= 75 degrees Fahreneheit we recommend you wear."
                   "  A Tank top, Shorts, Sandals.")
    label6.pack(pady = 25, padx = 25)


#Main NewWindow welcome screen
master_window = Tk()
master_window.title("Welcome Screen")
#master_window.configure(bg = '#95d6ea')
master_window.geometry('250x250')
bg = PhotoImage(file = 'clouds.png')
my_label = Label(master_window, image = bg)
my_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
#Welcome label for the master window
label = Label(master_window, text = "Welcome!")
label.configure(font= ("Courier", 8))
label.pack( pady = 10)

#Button to open Dave's weather app 
btn1 = Button(master_window, text = "Click to open Dave's Weather app", command = openNewWindow)
btn1.pack(expand = True)

#Button to open Dave's recommenadtion app 
btn2 = Button(master_window, text = "Click to open Dave's Recommendation app", command = openNewWindow2)
btn2.pack(expand = True)

#Welcome screen exit button
btn2 = Button(master_window, text = "Exit", command = exit)
btn2.pack(expand = True)

#Defines the warning box that will display on clicking x button on toolbar. 
def on_closing():
    if msg.askokcancel("Quit", "Do you want to quit?"):
            master_window.destroy()
master_window.protocol("WM_DELETE_WINDOW", on_closing)

master_window.mainloop()