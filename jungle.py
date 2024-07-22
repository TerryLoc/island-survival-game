import time

def jungle():
    print('You have chosen to go straight ahead to the jungle.')
    time.sleep(2)
    print('You are now in the jungle. The trees are tall and dense. The air is humid and you can hear the sound of the birds chirping.\n')
    time.sleep(2)
    print('You walk for a while and come across a fork in the path.\nYou can choose to go left, right or head back to the beach.\n')
    
    print('Which direction would you like to go?')
    print('1. To the left.')
    print('2. To the right.')
    print('3. Head back to the beach.')
    user_choice = input('Enter your choice: ')
    
    if user_choice == '1':
        print('You have chosen to go left. You walk for a while and come across a river.\n As you go closer to the river, you see a boat on the other side.\n')
        time.sleep(2)
        print('You can choose to swim across the river or head back to the jungle.\n')
        print('What would you like to do?')
        print('1. Swim across the river.')
        print('2. Head back to the jungle.\n')
        user_choice = input('Enter your choice: ')
        
        if user_choice == '1':
            print('\nYou have chosen to swim across the river.\n You start swimming across the river but the current is too strong and you get swept away.\n')
            print('You drown and die.\n')
        else:
            print('You have chosen to head back to the jungle.\n You walk back to the jungle and come across a wild boar.\n')
            print('The boar charges at you and you try to run but the boar catches up to you and attacks you.\n')
            print('You get injured and die.\n')
        
    
    elif user_choice == '2':
        print('\nYou have chosen to go right. You walk for a while and come across a what looks like man made shelter.\n')
        print('You can choose to go inside the shelter or head back to the jungle.\n')
        print('What would you like to do?')
        print('1. Go inside the shelter.')
        print('2. Head back to the jungle.\n')
        user_choice = input('Enter your choice: ')
        
        if user_choice == '1':
            print('\nYou have chosen to go inside the shelter.\n You walk inside the shelter.\n There is a bed, a table and a chair inside the shelter.\nYou also find some food and water.\n')
            print('You decide to rest for a while and eat some food.\n')
        else:
            print('You have chosen to head back to the jungle.\n You walk back to the jungle and come across a wild boar.\n')
            print('The boar charges at you and you run for your life.\n')
            print('You manage to escape the boar and find your way back to the beach.\n')
    
    else:
        print('\nYou have chosen to head back to the beach.\n You walk back to the beach and see a ship in the distance.\n')
        print('You wave your hands and the ship sees you and comes to rescue you.\n')
        print('Congratulations! You have been rescued and survived the island.\n')
        print('You have won the game.\n')
        exit()
        