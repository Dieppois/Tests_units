from filesystem_interface import FileSystemInterface

class FileManager:
    def __init__(self, file_selector, file_system: FileSystemInterface):
        self.file_selector = file_selector
        self.file_system = file_system

    def copy_files(self, destination):
        selected_files = self.file_selector.get_selected_files()

        for file in selected_files:
            if self.file_system.exists(file):
                self.file_system.copy(file, destination)
        self.file_selector.clear_selection()


    def move_files(self, destination):
        selected_files = self.file_selector.get_selected_files()

        for file in selected_files:
            if self.file_system.exists(file):
                self.file_system.move(file, destination)
        self.file_selector.clear_selection()

    def delete_files(self):
        selected_files = self.file_selector.get_selected_files()

        for file in selected_files:
            if self.file_system.is_file(file):
                self.file_system.delete_file(file)
            elif self.file_system.is_directory(file):
                self.file_system.delete_directory(file)
        self.file_selector.clear_selection()