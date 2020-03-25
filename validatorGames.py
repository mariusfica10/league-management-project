class GamesValidationError(Exception):
    pass


class GamesValidator():
    def validate(self, game):
        errors = []

        #unused

        if errors != []:
            raise GamesValidationError(errors)
