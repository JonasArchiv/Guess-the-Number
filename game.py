import random

def start_game(language):
    messages = {
        'DE': {
            'welcome': "Willkommen zum Zahlenraten-Spiel!",
            'intro': "Ich denke an eine Zahl zwischen 1 und 100.",
            'guess_prompt': "Gib deine Schätzung ein: ",
            'too_low': "Zu niedrig! Versuch es noch einmal.",
            'too_high': "Zu hoch! Versuch es noch einmal.",
            'congratulations': "Herzlichen Glückwunsch! Du hast die Zahl {0} in {1} Versuchen erraten.",
            'thank_you': "Danke fürs Spielen!"
        },
        'EN': {
            'welcome': "Welcome to the Number Guessing Game!",
            'intro': "I’m thinking of a number between 1 and 100.",
            'guess_prompt': "Enter your guess: ",
            'too_low': "Too low! Try again.",
            'too_high': "Too high! Try again.",
            'congratulations': "Congratulations! You guessed the number {0} in {1} attempts.",
            'thank_you': "Thank you for playing!"
        }
    }
    
    lang = messages.get(language, messages['EN'])
    
    print(lang['welcome'])
    print(lang['intro'])
    
    geheime_zahl = random.randint(1, 100)
    
    versuche = 0
    geraten = False
    
    while not geraten:
        benutzer_input = input(lang['guess_prompt'])
        
        try:
            schatz = int(benutzer_input)
        except ValueError:
            print("Bitte gib eine gültige Zahl ein." if language == 'DE' else "Please enter a valid number.")
            continue
        
        versuche += 1
        
        if schatz < geheime_zahl:
            print(lang['too_low'])
        elif schatz > geheime_zahl:
            print(lang['too_high'])
        else:
            geraten = True
            print(lang['congratulations'].format(geheime_zahl, versuche))
    
    print(lang['thank_you'])

def choose_language():
    while True:
        print("Please select your language / Bitte wählen Sie Ihre Sprache:")
        print("1. English")
        print("2. Deutsch")
        choice = input("Enter 1 for English or 2 for Deutsch: ")
        
        if choice == '1':
            return 'EN'
        elif choice == '2':
            return 'DE'
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    language = choose_language()
    start_game(language)
