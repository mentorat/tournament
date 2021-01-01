from models.players import Player
from models.tournaments import Tournament
from models.database import Data
from view.menu import MainView
from view.newplayer import NewPlayer
from view.newtournament import NewTournament
from view.score import Score
from view.displayround import DisplayRound
from view.report import DisplayReport


import datetime
from tinydb import TinyDB, Query

class MenuController:
    def create_player():
        """ Create a new player. """
        first_name = NewPlayer.player_first_name()
        last_name = NewPlayer.player_last_name()
        birth_date = NewPlayer.player_birth_date()
        gender = NewPlayer.player_gender()
        rank = NewPlayer.player_rank()
        score = NewPlayer.player_score()
        return Player(first_name, last_name, birth_date, gender, rank, score)

    


    def create_tournament(players):
        """Create a new tournament. """
        name = NewTournament.tournament_name()
        location = NewTournament.tournament_location()
        mode = NewTournament.tournament_mode()
        description = NewTournament.tournament_description()
        return Tournament(name, location, mode, description, players)
    
    def display_reports():
        # a enlever pour DataBase __init__
        db = TinyDB("db.json")
        tournament_table = db.table("TOURNAMENTS")
        actors_table = db.table("ACTORS")
        rounds_table = db.table("ROUNDS")
        matches_table = db.table("MATCHES")
        user = Query()
        report = DisplayReport.menu_report()
        if report == 1:
            display_report = Data.sorted_actors(actors_table)
            DisplayReport.report_1(display_report)
        elif report == 2:
            display_report = tournament_table.all()
            DisplayReport.report_2(display_report)
        elif report == 3:
            display_report = Data.request_tournament(tournament_table, user)
            DisplayReport.report_3(display_report)
        elif report == 4:
            display_report = Data.request_players(tournament_table, user)
            DisplayReport.report_4(display_report)
        else:
            MainView.welcome()
        DisplayReport.menu_report()


    def back_menu():
        """Display menu to go back to the Main Menu."""
        choice = MainView.back_menu()
        if choice == 1:
            MainView.welcome()
        elif choice == 2:
            Data.update_rank(actors_table, players_by_tournament, user)
            return back_menu()
        elif choice == 3:
            print("Program ended ! See you soon !")
        else:
            print("An error occurred.")
            return back_menu()


    def inter_menu():
        """Display menu between rounds."""
        choice = MainView.interround_menu()
        if choice == 1:
            pass
        elif choice == 2:
            Data.update_rank(actors_table, players_by_tournament, user)
            return inter_menu()
        elif choice == 3:
            MainView.welcome()
        elif choice == 4:
            print("Program ended ! See you soon !")
        else:
            print("An error occurred.")
            return inter_menu()