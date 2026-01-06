from file_manager import FileManager
from file_selector import FileSelector
from local_filesystem import LocalFileSystem
from file_explorer import FileExplorer


def main_menu():
    explorer = FileExplorer()
    selector = FileSelector()
    filesystem = LocalFileSystem()

    manager = FileManager(selector, filesystem)

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
            explorer.display_directory_contents(selector)

        elif choice == "2":
            index = int(input("Enter navigation index: "))
            explorer.navigate(index, selector)

        elif choice == "3":
            explorer.go_to_parent_directory(selector)

        elif choice == "4":
            explorer.display_directory_contents(selector)
            indices = input("Enter file indices: ")
            selector.select_files_by_indices(indices, explorer.current_path)

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
