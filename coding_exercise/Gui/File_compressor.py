import PySimpleGUI as sg


label1 = sg.Text("Selects to compress file")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Selects destination folder")
input2 = sg.Input()
choose_button2 = sg.FilesBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button]])
window.read()
windew.close()
