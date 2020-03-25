from games import *


class ServiceGames:
    def __init__(self, repositoryGames, validator):
        self.__repositoryGames = repositoryGames
        self.__validator = validator

    def add(self, id, date, league, team1, team2, score1, score2):
        game = Games(id, date, league, team1, team2, score1, score2)
        self.__validator.validate(game)
        self.__repositoryGames.add(game)

    def read(self, ID):
        return self.__repositoryGames.read(ID)

    def getAll(self):
        return self.__repositoryGames.read()

    def delete(self, ID):
        self.__repositoryGames.delete(ID)
