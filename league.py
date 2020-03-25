from entity import *


class League(Entity):
    # class league for the league admin of frame 2
    def __init__(self, id, league, name, played, wins, draw, loses, made, got):
        super().__init__(id)
        self.__league = league
        self.__name = name
        self.__played = played
        self.__wins = wins
        self.__draw = draw
        self.__loses = loses
        self.__made = made
        self.__got = got


    def getLeague(self):
        return self.__league

    def getName(self):
        return self.__name

    def getPlayed(self):
        return self.__played

    def getWins(self):
        return self.__wins

    def getDraw(self):
        return self.__draw

    def getLoses(self):
        return self.__loses

    def getMade(self):
        return self.__made

    def getGot(self):
        return self.__got

    def setLeague(self, value):
        self.__league = value

    def setName(self, value):
        self.__name = value

    def setPlayed(self, value):
        self.__name = value

    def setWins(self, value):
        self.__wins = value

    def setDraw(self, value):
        self.__draw = value

    def setLoses(self, value):
        self.__loses = value

    def setMade(self, value):
        self.__made = value

    def setGot(self, value):
        self.__got = value


    def __str__(self):
        return "{} {} {} {} {} {} {} {} {}".format(self.getID(), self.getLeague(), self.getName(), self.getPlayed(), self.getWins(), self.getDraw(), self.getLoses(), self.getMade(),self.getGot())
