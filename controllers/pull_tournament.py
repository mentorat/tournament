from .tournament import TournamentController
from .helpers import Input

from models.round import Round
from models.tournament import Tournament

from view.tournament import TournamentView as View


class PullTournament(TournamentController):
    """To continue an unfinished tournament."""

    def __init__(self):
        """Init."""
        self.view = View()
        self.tournament = None

    def display(self):
        if not tournament:
            print("The value entered doesn't match any tournament !\n")

    def get_command(self):
        "Choose a uncompleted tournament in the database."
        tournament = self.tournament
        if not tournament:
            name = Input.for_string("Name of an UNcompleted tournament ? ")
            tournament = Tournament.get(name)
            if not tournament:
                return ""  # ici je retourne rien pour faire marcher la "vue" (qui n'existe pas ! :O) en gros pour rediriger le print vers display.
        # concrètement j'évite la boucle while ici et je me repose sur la boucle principale pour faire tourner la demande en boucle.
        # pour cela, j'avais besoin d'initialiser l'attribut tournament à la classe, pour l'avoir en mémoire à chaque tour de boucle

        # dans l'idéal les rounds devraient déjà être sérialisés - normalement c'est peut être le cas
        rounds = tournament.rounds
        # toute cette partie peut donc être évitée
        serialized_rounds = []
        for round in rounds:
            serialized_round = Round.serialized(round)
            serialized_rounds.append(serialized_round)

        players = tournament.players
        nb_rounds = 4 - len(rounds)
        super().progress_next_rounds(
            tournament,
            players,
            serialized_rounds,
            nb_rounds,
        )
        return "main menu"
