from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=choice(figlet.getFonts()))
    print(figlet.renderText(text))

elif len(sys.argv) == 2 and (sys.argv[1] != "-f" or sys.argv[1] != "--font"):
    sys.exit("Invalid usage")

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in figlet.getFonts()):
    text = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))
else:
    sys.exit("Invalid usage")
