class Entity:
    def __init__(self, id):
        """
        creates an entity object
        :param id: int, id of the object
        """
        self.__id = id

    def getID(self):
        """
        gets the id
        :return: the id
        """
        return self.__id
