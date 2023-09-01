class Driver:
    def __init__(self, name: str, nationality: str, seasons, championships, entries, starts, poles, wins, podiums) -> None:
        self.name = name
        self.nationality = nationality
        self.seasons = seasons
        self.championships = championships
        self.entries = entries
        self.starts = starts
        self.poles = poles
        self.wins = wins
        self.podiums = podiums
        pass


    def get_dict(self):
        return {
            'name': self.name,
            'nationality': self.nationality,
            'seasons': self.seasons,
            'championships': self.championships,
            'entries': self.entries,
            'starts': self.starts,
            'poles': self.poles,
            'wins': self.wins,
            'podiums': self.podiums
        }