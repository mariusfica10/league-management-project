from entity import *


class Games(Entity):
    # class games for the scoreboard
    def __init__(self, id, date, league, nameOne, nameTwo, scoreOne, scoreTwo):
        super().__init__(id)
        self.__date = date
        self.__league = league
        self.__nameOne = nameOne
        self.__nameTwo = nameTwo
        self.__scoreOne = scoreOne
        self.__scoreTwo = scoreTwo

    def getLeague(self):
        return self.__league

    def getNameOne(self):
        return self.__nameOne

    def getNameTwo(self):
        return self.__nameTwo

    def getScoreOne(self):
        return self.__scoreOne

    def getScoreTwo(self):
        return self.__scoreTwo

    def getDate(self):
        return self.__date

    def __str__(self):
        "{} {} {} {} {} {} {}".format(self.getID(), self.getDate(), self.getLeague(), self.getNameOne(), self.getNameTwo(), self.getScoreOne(), self.getScoreTwo())
