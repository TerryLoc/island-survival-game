import random
import time
import images
import jungle
import cave

YES = 'y'
NO = 'n'

def exit_game():
    """Exits the game with a goodbye message."""
    print('\nYou have decided not to board your flight.')
    print('Maybe you will catch the next one.')
    print('Goodbye for now!')
    print(images.game_over)
    exit()

def print_welcome_message():
    """Prints the welcome message and game rules."""
    print(images.title)
    print('How to play:\n1. You will be given a scenario and you choose from a list of options.\n2. You use the arrow keys to enter your option eg.(left, right, up, down).\n3. You will be given a new scenario based on your choice.\n4. You will have to make the right choices to survive and escape the island.\n')
    get_user_name()

def get_user_name():
    """Prompts the user for their name and initiates the boarding process."""
    while True:
        user_name = input('What is your name, adventurer? ').strip().capitalize()
        if user_name.isalpha():
            break
        else:
            print("Please enter a name using letters only.\n")
    initiate_boarding(user_name)

def initiate_boarding(user_name):
    """Initiates the boarding process based on user's choice."""
    board_plan = ''
    while board_plan not in [YES, NO]:
        board_plan = input(f'\nWelcome {user_name}! Are you ready to board your flight (y/n)? \n').lower()
        if board_plan not in [YES, NO]:
            print("Please enter 'y' for yes or 'n' for no.")
    
    if board_plan == YES:
        print('\nGreat! You are now boarding your flight to your work destination.\n')
        print('Unfortunately your plane gets caught in a freak storm.\n')
        print(f'Oh no {user_name}! You are the sole survivor of your plan crashing, having washed ashore on a deserted island.\n')
        time.sleep(3)
        first_event()
    else:
        exit_game()

def first_event():
    """Determines the time of day and presents the first event scenario."""
    day_night = random.choice(['day', 'night'])
    if day_night == 'day':
        print('It is day time. You can see the sun shining brightly.\nThe weather is warm and the sky is clear. You can see the blue ocean and golden beach.\n\nStraight ahead is a dense jungle.\nTo your left you see a dark cave entrance.\nTo your right, you see a tall rocky cliff face.\n')
    else:  
        print('It is night time. The moon is shining brightly.\nThe weather is cool and the sky is clear.\nYou can see the stars twinkling in the sky. You hear the sound of the ocean waves crashing on the shore.\n\nStraight ahead is a dark dense jungle.\nTo your left, you can just about make out a dark cave.\nTo your right, you see a steep rocky cliff.\n')
    second_event(day_night)

def second_event(day_night):
    """Presents the second event scenario based on the user's choice."""
    print('Which direction would you like to go?')
    print('1. Straight ahead to the jungle.')
    print('2. To the left to the dark cave.')
    print('3. Head right to the steep cliff.')
    print('4. Stay put.')
    user_choice = input('Enter your choice: \n')
    
    if user_choice == '1':
        time.sleep(2)
        jungle.jungle()
    elif user_choice == '2':
        time.sleep(2)
        cave.cave()
    elif user_choice == '3':
        handle_cliff_scenario()
    else:
        handle_stay_put_scenario()

def handle_cliff_scenario():
    """Handles the scenario when the user chooses to go to the cliff."""
    print('You have chosen to go to the right to the steep cliff.')
    time.sleep(2)
    print('You walk towards the steep cliff and see that it is too high to climb.\n')
    print('You decide to head back to the beach.\n')
    time.sleep(2)
    print('You walk back to the beach and see a ship in the distance.\n')
    print('You wave your hands and the ship sees you and comes to rescue you.\n')
    print('Congratulations! You have been rescued and survived the island.\n')
    print('You have won the game.\n')
    print(images.game_over)
    exit()

def handle_stay_put_scenario():
    """Handles the scenario when the user chooses to stay put."""
    print('You have chosen to stay put and wait for help to arrive.\n')
    time.sleep(2)
    print('You wait for a while but no help arrives.\n')
    print('You decide to go look for help.\n')
    time.sleep(2)
    first_event()

def main():
    """Main function to start the game."""
    print_welcome_message()

if __name__ == '__main__':
    main()