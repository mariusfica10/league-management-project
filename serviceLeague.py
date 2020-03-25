from league import *


class ServiceLeague:
    def __init__(self, repositoryLeague, validator):
        self.__repositoryLeague = repositoryLeague
        self.__validator = validator

    def add(self, id, league, name, played, wins, draw, loses, made, got):
        league = League(id, league, name, played, wins, draw, loses, made, got)
        self.__validator.validate(league)
        self.__repositoryLeague.add(league)

    def update(self, id, league, name, played, wins, draw, loses, made, got):
        league = League(id, league, name, played, wins, draw, loses, made, got)
        self.__repositoryLeague.update(league)

    def read(self, ID):
        return self.__repositoryLeague.read(ID)

    def getAll(self):
        return self.__repositoryLeague.read()

    def delete(self, ID):
        self.__repositoryLeague.delete(ID)
