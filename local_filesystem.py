import os
import shutil
from filesystem_interface import FileSystemInterface


class LocalFileSystem(FileSystemInterface):

    def exists(self, path):
        return os.path.exists(path)

    def copy(self, source, destination):
        shutil.copy2(source, destination)

    def move(self, source, destination):
        shutil.move(source, destination)

    def delete_file(self, path):
        os.remove(path)

    def delete_directory(self, path):
        shutil.rmtree(path)

    def is_file(self, path):
        return os.path.isfile(path)

    def is_directory(self, path):
        return os.path.isdir(path)
