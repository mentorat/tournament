"""Helpers."""


class Input:
    """Help class for input function.

    NOTE: Cette classe n'est pas un controller mais une classe d'aide d'inputs.
    """

    @classmethod
    def for_string(cls, message):
        """Check if the value of an input is a string.

        NOTE: pas besoin d'une valeur booléenne car tu fais
        un retour direct si la condition est vrai.

        Pas besoin de raise une erreur car tu la traite directement
        en continuant la boucle si c'est faux.

        Pourquoi tu met "self" dans la fonction input ? Elle attend
        une chaîne de caractères, pas une instance de classe.
        En fait, tu mettais un paramètre à chaque fois qui était la chaîne de caractère
        à afficher, mais tu l'a mis en tant que "self" !

        Au final tu peux mettre la condition directement au niveau de while. ;)

        Même chose pour les autres méthodes.
        """
        value = input(message)
        while not value.isalpha():
            print("Incorrect value, it has to be a word !")
            value = input(message)
        return value

    @classmethod
    def for_integer(cls, message):
        """Check if the value of an input is an integer."""
        value = input(message)
        while not value.isdigit() or "." in value:
            print("Incorrect value, it has to be a positive number !")
            value = input(message)
        return int(value)

    @classmethod
    def for_score(cls, message):
        """Check the value of the score is correct.

        Enter the scores for each round:
        1 point for the winner,
        0.5 point if draw,
        0 point for the loser.

        NOTE: attention en transformant le résultat en integer tu ne peux pas
        récupérer de chiffre à virgule
        """
        score = -1
        scores = [0, 0.5, 1]
        error = (
            "Incorrect score, it has to be 1 point for the winner, "
            "0.5 point if draw, 0 point for the loser!"
        )
        while score not in scores:
            try:
                score = input(message)
                score = int(score) if "." not in score else float(score)
            except (ValueError, TypeError):
                print(error)
        return score

    @classmethod
    def for_range(cls, message, range=[1, 2, 3]):
        """Check the input value when the choices are from 1 to 3.

        NOTE: ici on a une boucle infinie, mais si aucune erreur ne sort
        on retourne la commande (ce qui nous fait sortir de la boucle par extension).

        On évite d'avoir des méthodes redondances (check_for_3, check_for_5...) car
        la seule chose qui change c'est l'interval ! autant le passer en paramètres ;)
        """
        while True:
            try:
                choice = int(input(message))
                if choice not in range:
                    raise ValueError

                print(f"Your command ({choice}) has been successfully entered...\n")
                return choice

            except TypeError:
                print("Incorrect value, it has to be a positive number !")
            except ValueError:
                print("The value entered doesn't match the possible choices !\n")

    @classmethod
    def for_gender(cls, message):
        """Check if the gender value is 'm' or 'f'."""
        genders = ["m", "f"]
        while True:
            try:
                gender = input(message).lower()
                if gender not in genders:
                    raise ValueError

                return gender

            except TypeError:
                print("Incorrect gender, it has to be 'm' / 'f' !")
            except ValueError:
                print("Incorrect gender, it has to be 'm' / 'f' !")
