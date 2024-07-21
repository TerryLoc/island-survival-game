import random
import time
import curses

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
    while True:
        user_name = input('What is your name, adventurer? ').lower().capitalize()
        if user_name.isalpha():
            break
        else:
            print("Please enter a name using letters only.\n")
    board_plan = input(f'\nWelcome {user_name}! Are you ready to board your flight (y/n) ? ').lower()
    
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
        print('It is day time. You can see the sun shining brightly.\nThe weather is warm and the sky is clear. You can see the blue ocean and golden beach.\n\nStraight ahead is a dense jungle.\nTo your left you see a dark cave entrance.\nTo your right, you see a tall rocky cliff face.\n')
    else:  
        print('It is night time. The moon is shining brightly.\nThe weather is cool and the sky is clear.\nYou can see the stars twinkling in the sky. You hear the sound of the ocean waves crashing on the shore.\n\nStraight ahead is a dark dense jungle.\nTo your left, you can just about make out a dark cave.\nTo your right, you see a steep rocky cliff.\n')
        
    
    # To run the curses application, wrap the function call with curses.wrapper
    curses.wrapper(get_user_choice)


def get_user_choice(stdscr):
    curses.curs_set(0)  # Hide the cursor
    options = ['left', 'right', 'up', 'down']
    current_row = 0

    def print_menu(current_row):
        stdscr.clear()
        stdscr.addstr("Choose your direction using arrow keys and press Enter:\n")
        for idx, option in enumerate(options):
            if idx == current_row:
                stdscr.addstr(idx + 1, 0, option, curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 1, 0, option)
        stdscr.refresh()

    while True:
        print_menu(current_row)
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            break

    user_choice = options[current_row]
    stdscr.clear()
    if user_choice == 'left':
        stdscr.addstr('You have chosen to explore the dark cave.\n')
    elif user_choice == 'right':
        stdscr.addstr('You have chosen to climb the rocky cliff.\n')
    elif user_choice == 'up':
        stdscr.addstr('You have chosen to walk straight ahead into the dense jungle.\n')
    else:
        stdscr.addstr('You have chosen to stay put and wait till morning.\n')
    stdscr.refresh()
    stdscr.getch()


    
def main():
    print_welcome_message()
    

if __name__ == '__main__':
    main()
