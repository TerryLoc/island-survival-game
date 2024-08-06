
# Island Survival Game

Welcome to the **Island Survival Game**, a text-based adventure where you must survive on a deserted island after a plane crash. Make the right choices and ultimately escape the island.

## How to Play

1. You will be given a scenario and you choose from a list of options.
2. Use numbers to enter your option (e.g., 1, 2, 3, 4).
3. You will be presented with a new scenario based on your choice.
4. Make the right choices to survive and escape the island.

## Game Structure
### Main Functions
1.  **print_welcome_message()**: Displays the welcome message and game rules.
2.  **get_user_name()**: Prompts the user for their name and initiates the boarding process.
3.  **initiate_boarding(user_name)**: Handles the boarding process and starts the first event.
4.  **exit_game()**: Exits the game with a goodbye message.
5.  **get_numeric_choice(prompt)**: Prompts the user for a numeric input and validates it.
6.  **first_event()**: Determines the time of day and presents the first event scenario.
7.  **second_event(day_night)**: Presents the second event scenario based on the user's choice.
8.  handle_scenarios(day_night, user_choice, movements): Handles scenarios based on the user's choice.
9.  **choices(day_info, print_choices)**: Prints the choices based on it being daytime.
10. **choices_outcomes(day_info, print_choices)**: Prints the choices based on the outcome decision of the user.
11. **handle_stay_put_scenario()**: Handles the scenario when the user chooses to stay put.
12. **main()**: The main function to start the game.

#### Sample Code
Here’s a snippet of the main game loop:

            def main():
                """Main function to start the game."""
                print_welcome_message()

            if __name__ == "__main__":
                main()


### Example Usage
After starting the game, you'll be asked for your name and whether you're ready to board the plane.
If you choose to board, the adventure begins with the plane crashing and you being stranded on an island.
You'll be presented with various scenarios and must choose your actions wisely to survive.

### Images and Scenes
The game uses images and scenes from the images and scenes modules.
Make sure these modules are included in your project directory.


### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/island-survival-game.git
    cd island-survival-game
    ```

2. Install any required packages (if applicable):

    ```bash
    pip install -r requirements.txt
    ```

### Running the Game

Run the main Python file to start the game:

```bash
python main.py


## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
