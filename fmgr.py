import os
import shutil


class FileSelector:
    def __init__(self):
        self.selected_files = []
        self.current_directory_contents = []

    def load_directory_contents(self, directory_path):
        try:
            self.current_directory_contents = os.listdir(directory_path)
            return self.current_directory_contents
        except Exception as e:
            print(f"Error loading directory contents: {e}")
            return []

    def select_files_by_indices(self, indices, directory_path):
        try:
            selected_indices = [int(i.strip()) for i in indices.split(",")]
            self.selected_files.clear()

            for index in selected_indices:
                if 0 <= index < len(self.current_directory_contents):
                    full_path = os.path.join(
                        directory_path,
                        self.current_directory_contents[index]
                    )
                    self.selected_files.append(full_path)

            return self.selected_files
        except ValueError:
            print("Invalid input.")
            return []

    def get_selected_files(self):
        return self.selected_files

    def clear_selection(self):
        self.selected_files.clear()

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

class FileManager:
    def __init__(self):
        self.file_selector = FileSelector()

    def copy_files(self, destination):
        selected_files = self.file_selector.get_selected_files()

        for file in selected_files:
            if os.path.exists(file):
                shutil.copy2(file, destination)
        self.file_selector.clear_selection()

        print(f"{len(selected_files)} file(s) copied")


    def move_files(self, destination):
        selected_files = self.file_selector.get_selected_files()

        for file in selected_files:
            if os.path.exists(file):
                shutil.move(file, destination)
        self.file_selector.clear_selection()

        print(f"{len(selected_files)} file(s) moved")

    def delete_files(self):
        selected_files = self.file_selector.get_selected_files()

        for file in selected_files:
            if os.path.isfile(file):
                os.remove(file)
            elif os.path.isdir(file):
                shutil.rmtree(file)
        self.file_selector.clear_selection()

        print(f"{len(selected_files)} file(s)/folder(s) deleted")

def main_menu():
    explorer = FileExplorer()
    manager = FileManager()

    while True:
        print("""
--- File Explorer ---
1. Display Directory
2. Navigate
3. Go to Parent Directory
4. Select Files
5. Copy
6. Move
7. Delete
8. Quit
""")

        choice = input("Your choice: ")

        if choice == "1":
            explorer.display_directory_contents(manager.file_selector)

        elif choice == "2":
            index = int(input("Enter navigation index: "))
            explorer.navigate(index, manager.file_selector)

        elif choice == "3":
            explorer.go_to_parent_directory(manager.file_selector)

        elif choice == "4":
            explorer.display_directory_contents(manager.file_selector)
            indices = input("Enter file indices: ")
            manager.file_selector.select_files_by_indices(
                indices, explorer.current_path
            )

        elif choice == "5":
            dest = input("Destination: ")
            manager.copy_files(dest)

        elif choice == "6":
            dest = input("Destination: ")
            manager.move_files(dest)

        elif choice == "7":
            manager.delete_files()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()
