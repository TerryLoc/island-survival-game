import random
import time
import images

# import jungle
# import cave
from scenes import DAY_NIGHT
from scenes import movements

YES = "y"
NO = "n"


# Functions to handle user input and game flow
def exit_game():
    """Exits the game with a goodbye message."""
    print("\nYou have decided not to board your flight.")
    print("Maybe you will catch the next one.")
    print("Goodbye for now!")
    print(images.game_over)
    exit()


def get_numeric_choice(prompt):  # Now user_choice is guaranteed to be a number
    """Prompts the user for a numeric input and validates it."""
    while True:
        user_choice = input(prompt).strip()  # Remove leading/trailing whitespaces
        if user_choice.isdigit():
            return int(user_choice)  # Convert to integer
        else:
            print("Invalid input. Please enter a number matching your choice.")


def print_welcome_message():
    """Prints the welcome message and game rules."""
    print(images.title)
    print(
        "How to play:\n1. You will be given a scenario and you choose from a list of options.\n2. You use numbers to enter your option eg.(1, 2, 3, 4).\n3. You will be given a new scenario based on your choice.\n4. You will have to make the right choices to survive and escape the island.\n"
    )
    get_user_name()


def get_user_name():
    """Prompts the user for their name and initiates the boarding process."""
    while True:
        user_name = input("What is your name, adventurer? ").strip().capitalize()
        if user_name.isalpha():
            break
        else:
            print("Please enter a name using letters only.\n")

    initiate_boarding(user_name)


def initiate_boarding(user_name):
    """Initiates the boarding process based on user's choice."""
    board_plan = ""
    while board_plan not in [YES, NO]:
        board_plan = (
            input(
                f"\nWelcome {user_name}! Are you ready to board your flight (y/n)? \n"
            )
            .lower()
            .strip()
        )
        if board_plan not in [YES, NO]:
            print("Please enter 'y' for yes or 'n' for no.")

    if board_plan == YES:
        print("\nGreat! You are now boarding your flight to your work destination.\n")
        print("Unfortunately your plane gets caught in a freak storm.\n")
        print(
            f"Oh no {user_name}! Your plane has crashed and you are the sole survivor.\nYou have washed ashore on a deserted island.\n"
        )
        time.sleep(4)
        first_event()
    else:
        exit_game()


def first_event():
    """Determines the time of day and presents the first event scenario."""
    day_night = random.choice(["day", "night"])
    if day_night == "day":
        print(DAY_NIGHT["day"][0])
    else:
        print(DAY_NIGHT["night"][0])

    time.sleep(3)
    second_event(day_night)

def second_event(day_night):
    """Presents the second event scenario based on the user's choice."""

    def print_choices(day_night):
        """Prints the choices based on the time of day."""
        choices = movements["first_choices"][day_night]
        print("What would you like to do next?\n")
        for key, value in choices.items():
            print(f"{key}: {value}")

    # Call the function to print the choices
    print_choices(day_night)
    # Get the user's choice 
    user_choice = get_numeric_choice("\nPick your direction (1-4): \n")
    
    handle_scenarios(day_night, user_choice, movements)


def handle_scenarios(day_night, user_choice, movements):
    
    def print_choices(description, choices=None):
        """Prints the description and choices."""
        print(description)
        if choices:
            print("Where would you like to explore?\n")
            for key, value in choices.items():
                print(f"{key}: {value}")
        
    """Handles the scenarios based on the user's choice."""
    if user_choice == 1:
        if day_night == 'day':
            # To print choices for day:
            day_info = movements["jungle"]["day"] # Get the day info
            print_choices(day_info["description"], day_info["choices"])
        else:
            # To print choices for night:
            night_info = movements["jungle"]["night"] # Get the night info
            print_choices(night_info["description"])
            exit()
    elif user_choice == 2:
        if day_night == 'day':
            # To print choices for day:
            day_info = movements["cave"]["day"]
            print_choices(day_info["description"], day_info["choices"])
        else:
            # To print choices for night:
            night_info = movements["cave"]["night"]
            print_choices(night_info["description"])
            exit()
        
        
def handle_cliff_scenario():
    """Handles the scenario when the user chooses to go to the cliff."""
    print("You have chosen to go to the right to the steep cliff.")
    time.sleep(2)
    print("You walk towards the steep cliff and see that it is too high to climb.\n")
    print("You decide to head back to the beach.\n")
    time.sleep(2)
    print("You walk back to the beach and see a ship in the distance.\n")
    print("You wave your hands and the ship sees you and comes to rescue you.\n")
    print("Congratulations! You have been rescued and survived the island.\n")
    print("You have won the game.\n")
    print(images.game_over)
    exit()


def handle_stay_put_scenario():
    """Handles the scenario when the user chooses to stay put."""
    print("You have chosen to stay put and wait for help to arrive.\n")
    time.sleep(2)
    print("You wait for a while but no help arrives.\n")
    print("You decide to go look for help.\n")
    time.sleep(2)
    first_event()


def main():
    """Main function to start the game."""
    print_welcome_message()


if __name__ == "__main__":
    main()
