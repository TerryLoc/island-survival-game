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
            f"Oh no {user_name}! You are the sole survivor of your plan crashing, having washed ashore on a deserted island.\n"
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

    second_event(day_night)


def second_event(day_night):
    """Presents the second event scenario based on the user's choice."""
    print("Which direction would you like to go?")
    print("1. Straight ahead to the creepy jungle.")
    print("2. To the left towards the dark cave in the distance.")
    print("3. Head right to the steep cliff to check it out.")
    print("4. Or would you rather stay put.")

    print(movements["beach"][day_night])

    user_choice = get_numeric_choice("Enter your choice: \n")

    if user_choice == 1:
        time.sleep(2)
        jungle.jungle()
    elif user_choice == 2:
        time.sleep(2)
        cave.cave()
    elif user_choice == 3:
        time.sleep(2)
        handle_cliff_scenario()  # Assuming there's a cliff module and function
    elif user_choice == 4:
        handle_stay_put_scenario()
    else:
        print("Invalid choice. Please try again.")
        second_event(day_night)  # Re-prompt if the choice is not valid


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
