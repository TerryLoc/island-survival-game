import random
import time

def exit_game():
    '''This function is called when the user decides not to board the flight.'''
    print('Game Over! You have decided not to board your flight.')
    print('Maybe you will catch the next flight.')
    print('Goodbye!')
    exit()

def print_welcome_message():
    print('\nWELCOME TO THE ISLAND SURVIVAL GAME!\n')
    
    print('How to play:\n1. You will be given a scenario and you will have to choose from a list of options.\n2. You use the arrow keys to enter your option eg.(left, right, up, down).\n3. You will be given a new scenario based on your choice.\n4. You will have to make the right choices to survive and escape the island.\n')

    get_user_name()

    
def get_user_name():
    user_name = input('What is your name adventure? ').lower().capitalize()
    board_plan = input(f'\nWelcome {user_name}! Are you ready to board your flight (y/n)? ').lower()
    if board_plan == 'y':
        print('\nGreat! You are now boarding your flight to your work destination.\n')
        print('Unfortunately your plane gets caught in a freak storm.\n')
        print(f'Oh no {user_name}! You are the sole survivor of your plan crashing, having washed ashore on a deserted island.\n')
    else:
        exit_game()
   
    time.sleep(3)
    random_event()
    
def random_event():
    day_night = random.choice(['day', 'night'])
    if day_night == 'day':
        print('It is day time. You can see the sun shining brightly.\nThe weather is warm and the sky is clear. You can see the blue ocean and golden beach.\nStraight ahead is a dense jungle To your left, you see a dark cave entrance.\nTo your right, you see a tall rocky cliff face.\n')
    else:  
        print('It is night time. The moon is shining brightly.\nThe weather is cool and the sky is clear.\nYou can see the stars twinkling in the sky. You can hear the sound of the ocean waves crashing on the shore.\nStraight ahead is a dark dense jungle. To your left, you can just about make out a dark cave.\nTo your right, you see a steep rocky cliff.\n')

    
def main():
    print_welcome_message()
    

if __name__ == '__main__':
    main()
