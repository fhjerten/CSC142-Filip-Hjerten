import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pygame
import pygwidgets

pygame.init()

#WINDOW CONSTANTS
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 300

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Temperature Converter Assignment")

# COLOR CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creates a textinput widget here
temperatureInput = pygwidgets.InputText(window, (50, 50), width = 150,)

# Create the radio buttons here
#FAHRENHEIT
fahrenheitRadio = pygwidgets.TextRadioButton ( window, (50, 100), 1, "Convert to Fahrenheit", value = True)

#CELSIUS
celsiusRadio = pygwidgets.TextRadioButton( window, (50, 140), 1, "Convert to Celsius", value = False)

# The convert button
convertButton = pygwidgets.TextButton( window, (50, 180), "Convert")

# Creates DisplayText for result
resultDisplay = pygwidgets.DisplayText( window, (50, 230), "Result here:", fontSize = 24)


# The main loop of the project here
running = True

while running: 
    for event in pygame.event.get():

        temperatureInput.handleEvent(event)
        fahrenheitRadio.handleEvent(event)
        celsiusRadio.handleEvent(event)

        if event.type == pygame.QUIT:
            running = False

        # For button clicks here
        if convertButton.handleEvent(event):
            try:
                temp = float(temperatureInput.getValue())

                if fahrenheitRadio.getValue():
                    result = temp * 9/5 + 32
                    resultDisplay.setValue(f"{result:.2f} degrees Fahrenheit")

                else:
                    result = (temp - 32) / (9/5)
                    resultDisplay.setValue(f"{result:.2f} degrees Celsius")

            except:
                resultDisplay.setValue("Invalid input")

    #Drawing the whole window
    window.fill(WHITE)
    temperatureInput.draw()
    pygame.draw.rect(window, BLACK, temperatureInput.getRect(), 2)  # drawing, so there is an outlining for the input
    fahrenheitRadio.draw()
    celsiusRadio.draw()
    convertButton.draw()
    resultDisplay.draw()

    pygame.display.update()

# Exiting the program
pygame.quit()



