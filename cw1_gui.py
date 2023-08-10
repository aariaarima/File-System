import os
import subprocess
import PySimpleGUI as sg

def set_file_permissions(filename, permissions):
    try:
        command = ['sudo', 'chmod', permissions, filename]
        print("Running command:", " ".join(command))
        subprocess.run(command, check=True)
        print(f"File permissions for '{filename}' set to {permissions}.")
    except subprocess.CalledProcessError as e:
        print(f"Error setting file permissions: {e}")

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
    def create_file(self, filename):
        if filename in self.files:
            return f"File '{filename}' already exists."
        file_path = self.get_file_path(filename)
        with open(file_path, "w") as file:
            file.write("")
        self.files[filename] = file_path
        return f"File '{filename}' created."

    # Delete an existing file
    def delete_file(self, filename):
        if filename in self.files:
            file_path = self.files.pop(filename)
            os.remove(file_path)
            return f"File '{filename}' deleted."
        return f"File '{filename}' does not exist."

    # Read the content of an existing file
    def read_file(self, filename):
        if filename in self.files:
            file_path = self.files[filename]
            with open(file_path, "r") as file:
                return file.read()
        return f"File '{filename}' does not exist."

    # Write content to an existing file
    def write_file(self, filename, content):
        if filename in self.files:
            file_path = self.files[filename]
            with open(file_path, "w") as file:
                file.write(content)
            return f"Content written to '{filename}'."
        return f"File '{filename}' does not exist."

    # Append content to an existing file
    def append_file(self, filename, content):
        if filename in self.files:
            file_path = self.files[filename]
            with open(file_path, "a") as file:
                file.write(content)
            return f"Content appended to '{filename}'."
        return f"File '{filename}' does not exist."
    # Set permissions for a file
    def set_permissions(self, filename, permissions):
        if filename in self.files:
            set_file_permissions(self.files[filename], permissions)
            return f"Permissions for '{filename}' set to {permissions}."
        return f"File '{filename}' does not exist."
        

    # Create a new directory
    def create_directory(self, dirname):
        dir_path = self.get_file_path(dirname)
        if os.path.exists(dir_path):
            return f"Error: Directory '{dirname}' already exists."
        os.makedirs(dir_path)
        return f"Directory '{dirname}' created."


    # Delete an existing directory
    def delete_directory(self, dirname):
        dir_path = self.get_file_path(dirname)
        if os.path.exists(dir_path):
            os.rmdir(dir_path)
            return f"Directory '{dirname}' deleted."
        return f"Directory '{dirname}' does not exist."

    # Rename a directory
    def rename_directory(self, old_name, new_name):
        old_path = self.get_file_path(old_name)
        new_path = self.get_file_path(new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            return f"Directory '{old_name}' renamed to '{new_name}'."
        return f"Directory '{old_name}' does not exist."

    # Set permissions for a file or directory
    def set_permissions(self, path, permissions):
        if os.path.exists(path):
            set_permissions(path, permissions)
            return f"Permissions for '{path}' set to {permissions}."
        return f"Path '{path}' does not exist."
    # List all files and directories
    def list_files(self):
        return os.listdir(self.base_dir)

# Main function
def main():
    fs = FileSystem()

    # Set a custom theme and color scheme for the GUI
    sg.theme('TanBlue')
    sg.set_options(element_padding=(0, 0))

    # File management tab layout definition
    file_layout = [
        [sg.Text("  \nOptions:")],
        [sg.Text(" ")],
        [sg.Text(" "), sg.Button("Create File"), sg.Text(" "),
         sg.Button("Delete File"), sg.Text(" "),
         sg.Button("Read File"), sg.Text(" "),
         sg.Button("Write to File"), sg.Text(" "),
         sg.Button("Append to File"), sg.Text(" "),
         sg.Button("Set Permissions")],
        [sg.Text(" ")],
        [sg.Text(" "), sg.Text("Filename:               "), sg.InputText(key="filename")],
        [sg.Text(" ")],
        [sg.Text(" "), sg.Text("File Permissions:    "), sg.InputText(key="permissions")],
        [sg.Text(" ")],
        [sg.Text(" "), sg.Text("Content of the         \nfile:"), sg.Multiline(size=(43, 5), key="output", disabled=True)],
        [sg.Text(" ")],
        [sg.Text(" "), sg.Text("Content to add:       "), sg.Multiline(size=(43, 5), key="content", disabled=False)],
        [sg.Text(" ")], 
        [sg.Text(" "), sg.Column([[sg.Button("Execute", size=(15, 1), pad=(250, 0))]], element_justification='center')]
    ]

    # Directory management tab layout definition
    directory_layout = [
        [sg.Text(" ")], 
        [sg.Text(" Options:")],
        [sg.Text(" ")], 
        [sg.Text(" "), sg.Button("Create Directory"), sg.Text(" "),
         sg.Button("Delete Directory"), sg.Text(" "),
         sg.Button("Rename Directory")],
        [sg.Text(" ")], 
        [sg.Text(" "), sg.Text("Directory Name:"), sg.InputText(key="dirname")],
        [sg.Text(" ")], 
        [sg.Text(" "), sg.Button("List Directories")]
    ]

    # Main layout with tabs
    layout = [
        [sg.TabGroup([
            [sg.Tab("File Management", file_layout)],
            [sg.Tab("Directory Management", directory_layout)]
        ])]
    ]

    # Create the PySimpleGUI window
    window = sg.Window("File System by Garima Shrestha", layout)

    # Event loop
    while True:
        event, values = window.read()

        # Handle window closure or "Exit" button
        if event == sg.WINDOW_CLOSED:
            break
        # Handle file management events
        elif event == "Create File":
            filename = values["filename"]
            message = fs.create_file(filename)
            sg.popup(message)
        elif event == "Delete File":
            filename = values["filename"]
            message = fs.delete_file(filename)
            sg.popup(message)
        elif event == "Read File":
            filename = values["filename"]
            content = fs.read_file(filename)
            window["output"].update(content)
        elif event == "Write to File":
            filename = values["filename"]
            window["output"].update("")
            window["content"].update(disabled=False)
        elif event == "Append to File":
            filename = values["filename"]
            window["output"].update("")
            window["content"].update(disabled=False)
        elif event == "Set Permissions":
            filename = values["filename"]
            permissions = values["permissions"]
            if filename and permissions:
                message = fs.set_permissions(filename, permissions)
                sg.popup(message)
        elif event == "Execute":
            filename = values["filename"]
            content = values["content"]
            write_mode = "w" if sg.popup_yes_no("Do you want to overwrite the file?") == "Yes" else "a"

            if write_mode == "w":
                message = fs.write_file(filename, content)
            else:
                message = fs.append_file(filename, content)
                
        # Handle directory management events
        elif event == "Create Directory":
            dirname = values["dirname"]
            message = fs.create_directory(dirname)
            sg.popup(message)
        elif event == "Delete Directory":
            dirname = values["dirname"]
            message = fs.delete_directory(dirname)
            sg.popup(message)
        elif event == "Rename Directory":
            old_name = values["dirname"]
            new_name = sg.popup_get_text("Enter new directory name:")
            if old_name and new_name:
                message = fs.rename_directory(old_name, new_name)
                sg.popup(message)
        elif event == "List Directories":
            dirs = fs.list_files()
            sg.popup("Directories:\n" + "\n".join(dirs))

    # Close the PySimpleGUI window
    window.close()

# Entry point
if __name__ == "__main__":
    main()
