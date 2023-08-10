#python preogram for unit testing
import unittest
from unittest.mock import patch
from mainGUI import FileSystem

class TestFileSystem(unittest.TestCase):

    def setUp(self):
        self.fs = FileSystem()

    def test_create_file(self):
        result = self.fs.create_file("garima.txt")
        self.assertEqual(result, "File 'garima.txt' created.")

    def test_create_existing_file(self):
        self.fs.create_file("garima.txt")
        result = self.fs.create_file("garima.txt")
        self.assertEqual(result, "File 'garima.txt' already exists.")

    def test_delete_file(self):
        self.fs.create_file("garima.txt")
        result = self.fs.delete_file("garima.txt")
        self.assertEqual(result, "File 'garima.txt' deleted.")

    def test_delete_nonexistent_file(self):
        result = self.fs.delete_file("garima.txt")
        self.assertEqual(result, "File 'garima.txt' does not exist.")

    def test_read_file(self):
        self.fs.create_file("garima.txt")
        self.fs.write_file("garima.txt", "Hello, world!")
        result = self.fs.read_file("garima.txt")
        self.assertEqual(result, "Hello, world!")

    def test_read_nonexistent_file(self):
        result = self.fs.read_file("nonexistent_file.txt")
        self.assertEqual(result, "File 'nonexistent_file.txt' does not exist.")

    def test_write_file(self):
        self.fs.create_file("garima.txt")
        result = self.fs.write_file("garima.txt", "Hello, world!")
        self.assertEqual(result, "Content written to 'garima.txt'.")
        with open(self.fs.files["garima.txt"], "r") as file:
            content = file.read()
        self.assertEqual(content, "Hello, world!")

    def test_append_file(self):
        self.fs.create_file("garima.txt")
        self.fs.write_file("garima.txt", "Hello, ")
        result = self.fs.append_file("garima.txt", "world!")
        self.assertEqual(result, "Content appended to 'garima.txt'.")
        with open(self.fs.files["garima.txt"], "r") as file:
            content = file.read()
        self.assertEqual(content, "Hello, world!")

    def test_create_directory(self):
        result = self.fs.create_directory("garima")
        self.assertEqual(result, "Directory 'garima' created.")

    def test_create_existing_directory(self):
        self.fs.create_directory("garima")
        result = self.fs.create_directory("garima")
        self.assertEqual(result, "Error: Directory 'garima' already exists.")

    def test_delete_directory(self):
        self.fs.create_directory("garima")
        result = self.fs.delete_directory("garima")
        self.assertEqual(result, "Directory 'garima' deleted.")

    def test_delete_nonexistent_directory(self):
        result = self.fs.delete_directory("nonexistent_directory")
        self.assertEqual(result, "Directory 'nonexistent_directory' does not exist.")

    def test_rename_directory(self):
        self.fs.create_directory("old_directory")
        result = self.fs.rename_directory("old_directory", "new_directory")
        self.assertEqual(result, "Directory 'old_directory' renamed to 'new_directory'.")

    def test_rename_nonexistent_directory(self):
        result = self.fs.rename_directory("nonexistent_directory", "new_directory")
        self.assertEqual(result, "Directory 'nonexistent_directory' does not exist.")

if __name__ == '__main__':
    unittest.main()
