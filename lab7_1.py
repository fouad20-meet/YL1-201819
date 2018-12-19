import Tkinter as tk
import tkSimpleDialog

#Then when ever you want to ask the user for input use this code:
greeting = tkSimpleDialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
if greeting in ("Arrr!"):
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")

