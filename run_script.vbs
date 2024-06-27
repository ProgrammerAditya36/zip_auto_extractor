' VBScript to run Python script in the background

' Create a shell object
Set objShell = CreateObject("WScript.Shell")

' Define paths
pythonExe = "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe"  ' Replace with your Python executable path
pythonScript = "D:\Programming\Python\Zip_auto_extractor\main.py"  ' Replace with the full path to main.py

' Build the command to run the Python script silently
command = """" & pythonExe & """ """ & pythonScript & """"

' Run the command in the background
objShell.Run command, 0, False
