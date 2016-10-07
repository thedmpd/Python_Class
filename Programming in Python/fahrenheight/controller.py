import tkinter
import view
import model

class Controller:
    """
    Controller at the center of the MVC temp conversion app,
    which converts a float input to Celsius or Fahrenheit
    """
    def __init__(self):
        """
        Initialize MVC components
        """
        root = tkinter.Tk()
        root.wm_title("Temperature Converter")
        self.model = model.Model()
        self.view = view.View(self)
        self.view.mainloop()
        root.destroy()

    def celsiusToFahrenheit(self):
        """
        Interpret user input as Celsius and converts to Fahrenheit
        """
        resultTemperature = ""
        try:
            celsius = float(self.view.enterTemperature.get())
        except:
            resultTemperature = "Not a number!"
        else:
            resultTemperature = str(self.model.celsiusToFahrenheit(celsius))
            self.view.outputLabel["text"] = resultTemperature + " Fahrenheit."

    def fahrenheitToCelsius(self):
        """
        Interprets user input as Fahrenheit and converts to Celsius
        """
        resultTemperature = ""
        try:
            fahrenheit = float(self.view.enterTemperature.get())
        except:
            resultTemperature = "Not a number!"
        else:
            resultTemperature = str(self.model.fahrenheitToCelsius(fahrenheit))
            self.view.outputLabel["text"] = resultTemperature + " Celsius."

if __name__ == "__main__":
    print("MVC Temp control check")
    c = Controller()
