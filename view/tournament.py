class TournamentView:
    @classmethod
    def display(cls):
        """Display the creation of a new tournament."""
        print("\n==================================================")
        print("************CREATE A NEW TOURNAMENT**************\n")

    @classmethod
    def display_menu(cls):
        """Display the menu between 2 rounds during a tournament."""
        print("\n==================================================")
        print("\n What would you like to do ?")
        print("1 - CONTINUE THE TOURNAMENT")
        print("2 - Change the ranking from a player ?")
        print("3 - End the tournament and return to the general menu")

    def display_final_score(self, players):
        """Display the final menu with the final score of the tournament."""
        print("\n==================================================")
        print(f"FINAL RESULTS OF {self.name} :\n")
        for player in players:
            print(f"SCORE : {player.points}, {player.first_name} {player.last_name}")
        print("\n==================================================")

    @classmethod
    def display_next_round(cls, players, i, j):
        """Display a match of a round different to the 1st round."""
        print(f"{players[i].first_name} vs {players[j].first_name}")
