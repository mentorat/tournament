class Player:
    """Define the characteristics of a player."""

    def __init__(
        self,
        first_name,
        last_name,
        birth_date,
        gender,
        rank,
        score,
        score_game=0,
        point=0,
    ):
        """
        First name :
        Last Name :
        Date of birth :
        Gender :
        Ranking :
        Score :
        Tournament Score : 0
        Opponents : list of opponentss already met during a tournament.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score
        self.score_game = score_game
        self.opponents = []

    def __repr__(self):
        """Display Rank:[] [First Name], [Last Name], Score Game: [], Opponnents :[]."""
        return "Rank : {} {} {}, Score : {}, Opponnents :{}\n".format(
            self.rank,
            self.first_name,
            self.last_name,
            self.score_game,
            self.opponents,
        )

    def serialized_player(self):
        """Serialize player's data."""
        return {
            "first name": self.first_name,
            "last name": self.last_name,
            "birth date": self.birth_date,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
            "score game": self.score_game,
            "opponents": self.opponents,
        }

    @classmethod
    def deserialized_player(cls, serialized_player):
        """Pull player's informations from the database to continue a tournament."""
        first_name = serialized_player["first name"]
        last_name = serialized_player["last name"]
        birth_date = serialized_player["birth date"]
        gender = serialized_player["gender"]
        rank = serialized_player["rank"]
        score = serialized_player["score"]
        score_game = serialized_player["score game"]
        opponents = serialized_player["opponents"]
        return Player(
            first_name,
            last_name,
            birth_date,
            gender,
            rank,
            score,
            score_game,
            opponents,
        )

    def store_data_actors(self, user, actors_table):
        """Store actor's informations in the database."""
        ser_player = Player.serialized_player(self)
        actors_table.update(
            {"rank": self.rank, "score": self.score},
            user["first name"] == self.first_name
            and user["last name"] == self.last_name,
        )
        if ser_player not in actors_table:
            actors_table.insert(ser_player)
        return ser_player

    def update_score(self, actors_table, score, user):
        """Update actor's score in the database."""
        actors_table.update(
            {"score": score},
            user["first name"] == self.first_name
            and user["last name"] == self.last_name,
        )

    @classmethod
    def update_rank(cls, actors_table, tournaments_table, user):
        """Update actor's rank in the database and in the current tournament."""
        first_name = input("First name ? ").capitalize()
        last_name = input("Last name ? ").capitalize()
        new_rank = int(input("New rank ? "))
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )
        # NE FONCTIONNE PAS SUR LE TOURNOIS . A CORRIGER
        tournaments_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )

    def add_score_game(self, add_point):
        """At the end of all the rounds.
        Add match score to player's score_game."""
        self.score_game += add_point
        return self.score_game

    def add_final_score(self, score_game, score):
        """Last round only.
        Add tournament score to player's total score."""
        self.score = score_game + score
        return self.score

    @classmethod
    def sorted_actors(cls, actors_table):
        """Sort all actors by alphabetic order or by rank."""
        actors = actors_table.all()
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(actors, key=lambda actor: actor["last name"])
        else:
            return sorted(actors, key=lambda actor: actor["rank"])
