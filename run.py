import random

def print_welcome_message():
    print('\nWELCOME TO THE ISLAND SURVIVAL GAME!\n')
    
    print('How to play:\n1. You will be given a scenario and you will have to choose from a list of options.\n2. You use the arrow keys to enter your option eg.(left, right, up, down).\n3. You will be given a new scenario based on your choice.\n4. You will have to make the right choices to survive and escape the island.\n')

    get_user_name()

    
def get_user_name():
    user_name = input('What is your name adventure? ').lower().capitalize()
    print(f'\nWelcome {user_name}! You are the sole survivor of your plan crash, having washed ashore on a deserted island.\n')
    
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
