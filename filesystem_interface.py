from abc import ABC, abstractmethod


class FileSystemInterface(ABC):

    @abstractmethod
    def exists(self, path):
        pass

    @abstractmethod
    def copy(self, source, destination):
        pass

    @abstractmethod
    def move(self, source, destination):
        pass

    @abstractmethod
    def delete_file(self, path):
        pass

    @abstractmethod
    def delete_directory(self, path):
        pass

    @abstractmethod
    def is_file(self, path):
        pass

    @abstractmethod
    def is_directory(self, path):
        pass
