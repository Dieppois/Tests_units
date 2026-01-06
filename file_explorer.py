import os
from file_selector import FileSelector

class FileExplorer:
    def __init__(self):
        self.current_path = os.path.expanduser("~")

    def display_directory_contents(self, selector: FileSelector):
        contents = selector.load_directory_contents(self.current_path)
        print(f"\nCurrent Directory: {self.current_path}")
        print("-" * 50)
        for index, element in enumerate(contents):
            full_path = os.path.join(self.current_path, element)
            element_type = "📁 Folder" if os.path.isdir(full_path) else "📄 File"
            print(f"{index}. {element_type}: {element}")

    def navigate(self, index, selector: FileSelector):
        try:
            contents = os.listdir(self.current_path)
            target = os.path.join(self.current_path, contents[index])

            if os.path.isdir(target):
                self.current_path = target
                self.display_directory_contents(selector)
            else:
                print("Not a directory.")
        except Exception as e:
            print(f"Navigation error: {e}")

    def go_to_parent_directory(self, selector: FileSelector):
        self.current_path = os.path.dirname(self.current_path)
        self.display_directory_contents(selector)