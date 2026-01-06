import os

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