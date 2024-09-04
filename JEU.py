import random

def get_computer_choice():
    return random.choice(["pierre", "feuille", "ciseaux"])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "égalité"
    elif (user_choice == "pierre" and computer_choice == "ciseaux") or \
         (user_choice == "feuille" and computer_choice == "pierre") or \
         (user_choice == "ciseaux" and computer_choice == "feuille"):
        return "vous avez gagné"
    else:
        return "vous avez perdu"

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 3

    for _ in range(rounds):
        user_choice = input("Choisissez pierre, feuille ou ciseaux : ").lower()
        if user_choice not in ["pierre", "feuille", "ciseaux"]:
            print("Choix invalide, veuillez réessayer.")
            continue

        computer_choice = get_computer_choice()
        print(f"L'ordinateur a choisi : {computer_choice}")

        result = get_winner(user_choice, computer_choice)
        print(f"Résultat : {result}")

        if result == "vous avez gagné":
            user_score += 1
        elif result == "vous avez perdu":
            computer_score += 1

    print(f"\nScore final : Vous {user_score} - {computer_score} Ordinateur")

    while True:
        replay = input("Voulez-vous rejouer ? (oui/non) : ").lower()
        if replay == "oui":
            play_game()
            break
        elif replay == "non":
            print("Merci d'avoir joué !")
            break
        else:
            print("Choix invalide, veuillez répondre par 'oui' ou 'non'.")

# Démarrer le jeu
play_game()

