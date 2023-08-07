import os
import PySimpleGUI as sg

# Define a class for the file system operations
class FileSystem:
    def __init__(self):
        self.base_dir = "files"
        os.makedirs(self.base_dir, exist_ok=True)
        self.files = {}

    # Get the full path of a file within the base directory
    def get_file_path(self, filename):
        return os.path.join(self.base_dir, filename)

    # Create a new file
    def create(self, filename):
        if filename in self.files:
            return f"File '{filename}' already exists."
        file_path = self.get_file_path(filename)
        with open(file_path, "w") as file:
            file.write("")
        self.files[filename] = file_path
        return f"File '{filename}' created."

    # Delete an existing file
    def delete(self, filename):
        if filename in self.files:
            file_path = self.files.pop(filename)
            os.remove(file_path)
            return f"File '{filename}' deleted."
        return f"File '{filename}' does not exist."

    # Read the content of an existing file
    def read(self, filename):
        if filename in self.files:
            file_path = self.files[filename]
            with open(file_path, "r") as file:
                return file.read()
        return f"File '{filename}' does not exist."

    # Write content to an existing file
    def write(self, filename, content):
        if filename in self.files:
            file_path = self.files[filename]
            with open(file_path, "w") as file:
                file.write(content)
            return f"Content written to '{filename}'."
        return f"File '{filename}' does not exist."
    
    # Append content to an existing file
    def write(self, filename, content):
        if filename in self.files:
            file_path = self.files[filename]
            with open(file_path, "a") as file:
                file.write(content)
            return f"Content appended to '{filename}'."
        return f"File '{filename}' does not exist."

# Main function
def main():
    fs = FileSystem()

    # Set a custom theme and color scheme for the GUI
    sg.theme('TanBlue')
    sg.set_options(element_padding=(0, 0))

    # GUI layout definition
    layout = [
        [sg.Text(" "), sg.Text("Options:")],
        [sg.Text(" ")],
        [sg.Text(" "), sg.Button("Create File", button_color=('#9dc7b7', 'black')), sg.Text(" "),
         sg.Button("Delete File", button_color=('#9dc7b7', 'black')), sg.Text(" "),
         sg.Button("Read File", button_color=('#9dc7b7', 'black')), sg.Text(" "),
         sg.Button("Write to File", button_color=('#9dc7b7', 'black')), sg.Text(" "),
         sg.Button("Append to File", button_color=('#9dc7b7', 'black')), sg.Text(" "),
         sg.Button("Exit", button_color=('#9dc7b7', 'black'))],
        [sg.Text(" ")],
        [sg.Text(" "), sg.Text("Filename:        "), sg.InputText(key="filename")],
        [sg.Text(" ")],
        [sg.Text(" "), sg.Text("Content of the  \nfile:"), sg.Multiline(size=(43, 5), key="output", disabled=True)],
        [sg.Text(" ")],
        [sg.Text(" "), sg.Text("Content to add:"), sg.Multiline(size=(43, 5), key="content", disabled=False)],
        [sg.Text(" ")],
        [sg.Text(" "), sg.Column([[sg.Button("Execute", size=(15, 1), pad=(150, 0), button_color=('#9dc7b7', 'black'))]], element_justification='center')]
    ]

    # Create the PySimpleGUI window
    window = sg.Window("File System by Garima Shrestha", layout)

    # Event loop
    while True:
        event, values = window.read()

        # Handle window closure or "Exit" button
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        # Handle "Create File" button
        elif event == "Create File":
            filename = values["filename"]
            message = fs.create(filename)
            sg.popup(message)
        # Handle "Delete File" button
        elif event == "Delete File":
            filename = values["filename"]
            message = fs.delete(filename)
            sg.popup(message)
        # Handle "Read File" button
        elif event == "Read File":
            filename = values["filename"]
            content = fs.read(filename)
            window["output"].update(content)
            window["content"].update(disabled=True)
        # Handle "Write to File" button
        elif event == "Write to File":
            filename = values["filename"]
            window["output"].update("")
            window["content"].update(disabled=False)
        # Handle "Append to File" button
        elif event == "Append to File":
            filename = values["filename"]
            window["output"].update("")
            window["content"].update(disabled=False)
        # Handle "Execute" button
        elif event == "Execute":
            filename = values["filename"]
            content = values["content"]
            message = fs.write(filename, content)
            sg.popup(message)

    # Close the PySimpleGUI window
    window.close()

# Entry point
if __name__ == "__main__":
    main()
