import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Selects to compress file")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Selects destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", colors="green")

window = sg.Window("File compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button],[output_label]])
while True:
    event, values = window.read()
    filespaths = values["files"].split(";")
    print(filespaths)
    folder = values["folder"]
    print(folder)
    make_archive(filespaths, folder)
    window["output"].update(value="Compression completed")

window.close()
