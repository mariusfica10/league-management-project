import pickle
from repositoryException import *


class RepositoryGeneric:
    def __init__(self, fileName):
        self.__storage = {}
        self.__fileName = fileName
        self.readFile()


    def readFile(self):
        try:
            with open(self.__fileName, 'rb') as f_read:
                self.__storage = pickle.load(f_read)
        except FileNotFoundError:
            self.__storage.clear()
        except Exception:
            self.__storage.clear()

    def writeFile(self):
        with open(self.__fileName, 'wb') as f_write:
            pickle.dump(self.__storage, f_write)

    def add(self, entity):
        ID = entity.getID()
        if ID in self.__storage:
            raise RepositoryException('ID must be unique')
        self.__storage[ID] = entity
        self.writeFile()

    def read(self, ID = None):
        self.readFile()
        if ID is None:
            return self.__storage.values()
        if ID in self.__storage:
            return self.__storage[ID]
        return None

    def update(self, entity):
        self.readFile()
        id_entity = entity.getID()
        if id_entity not in self.__storage:
            raise RepositoryException('There is no entity with that id!')
        self.__storage[id_entity] = entity
        self.writeFile()

    def delete(self, id_entity):
        self.readFile()
        if id_entity not in self.__storage:
            raise RepositoryException('There is no entity with that id!')
        del self.__storage[id_entity]
        self.writeFile()
