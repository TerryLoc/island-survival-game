import time
import images
import run

def user_choice():
    return run.get_numeric_choice('Enter your choice: \n')

def get_valid_choice(prompt, valid_choices):
    """Prompts the user for input and validates it against a list of valid choices."""
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in valid_choices:
            return user_input
        else:
            print(f'Invalid input. Please enter one of the following: {", ".join(valid_choices)}\n')

def cave():
    while True:
        prompt = ('\nYou have chosen to go to the left to the dark cave. You walk for a while and come across a dark cave entrance.\n'
            'You can choose to go inside the cave or head back to the beach.\n'
            'What would you like to do? (Enter cave or beach): \n')
        
        valid_choices = ['cave', 'beach']
        user_direction = get_valid_choice(prompt, valid_choices)
       
        if user_direction == 'cave':
            print('\nYou have chosen to go inside the cave.\nYou walk inside the cave and it is dark and damp.\nYou can hear the sound of bats flying around.\n')
            time.sleep(2)
            print('You can walk further inside or head back to the beach.\n')

            print('Which direction would you like to go?')
            print('1. Deeper into the cave.')
            print('2. Head back out of the cave.')
        
            choice = user_choice()
            
            if choice == 1:
                print('You have chosen to go deeper into the cave. You walk for a while and come across what looks like a treasure chest.\n')
                print('You can choose to open the treasure chest or head back out of the cave.\n')
                print('What would you like to do?')
                print('1. Open the treasure chest.')
                print('2. Head back out of the cave.\n')
                
                choice = user_choice()
                
                if choice == 1:
                    print('\nYou have chosen to open the treasure chest. You open the treasure chest and find a lot of gold and jewels inside.\n')
                    print('You have found the treasure and are now rich.\nCongratulations! You have won the game.\n')
                    print(images.game_over)
                    exit()
                else:
                    print('\nYou have chosen to head back out of the cave. You walk back to the beach and see a ship in the distance.\n')
                    print('You wave your hands and the ship sees you and comes to rescue you.\n')
                    print('Congratulations! You have been rescued and survived the island.\n')
                    print('You have won the game.\n')
                    print(images.game_over)
                    exit()   
            else: 
                print('\nYou have chosen to head back out of the cave. You walk back to the beach and see a ship in the distance.\n')
                print('You wave your hands and the ship sees you.\nAs the ship comes closer, you see that it is a pirate ship.\n')
                print('The pirates capture you and take you on board their ship.\n')
                print('You have been captured by the pirates, leading to you never being seen again.\nYou have lost the game.\n')
                print(images.game_over)
                exit()     
        else:
            print('\nYou have chosen to head back out of the cave. You walk back to the beach and see a ship in the distance.\n')
            print('You wave your hands and the ship sees you.\nAs the ship comes closer, you see that it is a pirate ship.\n')
            print('The pirates capture you and take you on board their ship.\n')
            print('You have been captured by the pirates, leading to you never being seen again.\nYou have lost the game.\n')
            print(images.game_over)
            exit()