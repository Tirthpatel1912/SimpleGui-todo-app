import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("ADD")

window = sg.Window('My to-do App', layout=[[label], [input_box, add_button]])
window.read()
print("Window successfully closed")
window.close()

