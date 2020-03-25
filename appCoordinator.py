from repositoryGeneric import *
from serviceLeague import *
from validatorLeague import *
from serviceGames import *
from validatorGames import *

repositoryLeague = RepositoryGeneric('league.pkl')
repositoryGame = RepositoryGeneric('game.pkl')

validatorLeague = LeagueValidator()
validatorGame = GamesValidator()

serviceLeague = ServiceLeague(repositoryLeague, validatorLeague)
serviceGame = ServiceGames(repositoryGame, validatorGame)
