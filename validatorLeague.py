class LeagueValidationError(Exception):
    pass


class LeagueValidator():
    def validate(self, league):
        errors = []

        #unused

        if errors != []:
            raise LeagueValidationError(errors)
