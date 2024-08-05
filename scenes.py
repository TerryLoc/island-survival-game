# Description: This file contains the scenes and choices for the game. The scenes are divided into different sections such as day, night, jungle, cave, and cliff. Each section has a description, choices, and outcomes based on the user's choice. The scenes are stored in a dictionary format for easy access and retrieval. The scenes are displayed to the user based on the time of day and the user's choice. The user can explore different paths and make choices that will determine the outcome of the game. The scenes are designed to create an immersive and interactive experience for the user.
import images


DAY_NIGHT = {
    "day": [
        "It is day time. You can see the sun shining brightly.\nThe weather is warm and the sky is clear. You can see the blue ocean and golden beach.\nStraight ahead is a dense jungle.\nTo your left you see a dark cave entrance.\nTo your right, you see a tall rocky cliff face.\n"
    ],
    "night": [
        "It is night time. The moon is shining brightly.\nThe weather is cool and the sky is clear.\nYou can see the stars twinkling in the sky. You hear the sound of the ocean waves crashing on the shore.\nStraight ahead is a dark dense jungle.\nTo your left, you can just about make out a dark cave.\nTo your right, you see a steep rocky cliff.\n"
    ],
}


movements = {
    "first_choices": {
        "day": {
            "1": "Head straight ahead to the creepy jungle.",
            "2": "Go to the left towards the dark cave in the distance.",
            "3": "Chance going right to the steep cliff and check it out.",
            "4": "Or would you rather stay put.",
        },
        "night": {
            "1": "Go straight ahead to the very dark jungle.",
            "2": "Chance going left towards what looks like a cave.",
            "3": "Head right to what looks like a cliff or wall.",
            "4": "Or stay put, on the beach till morning.",
        },
    },
    "jungle": {
        "day": {
            "description": "You are now in the jungle. The trees are tall and dense.\n"
            "The air is humid and you can hear the sound of the birds chirping.\n"
            "You walk for a while and come across a fork in the path.\n",
            "choices": {
                "1": "Go left",
                "2": "Go right",
                "3": "Head back to the beach",
            },
            "outcome": {
                "1": "You have chosen to go left.\nYou walk for a while and come across a sparkling river.\nThe water looks refreshing, & you notice some colorful fish swimming beneath the surface.\nYou choose to swim up stream but the river is so strong.\n You are swept away and your journey has ended.\n\n    🪦  YOU'RE DEAD 🪦\n\n"
                + images.game_over,
                "2": "You have chosen to go right.\nYou walk through the dense jungle & encounter a group of friendly monkeys.\nThey offer to show you 1. A hidden path or 2. lead you back to the beach\n.",
                "3": "You have chosen to head back to the beach.\n\n",
            },
            "options": {
                "1": "You follow the monkeys and they lead you to a hidden path that takes you to a beautiful waterfall.\nYou decide to take a swim in the cool water and relax.\nAfter a while, a rescue party find you relaxing and swimming.\nYour journey has ended happily. 🏝️\n\n    🎉  YOU ARE SAVED 🎉\n\n"
                + images.game_over,
                "2": "You are heading back to the beach and you see smoke.\nAs you emerge from the forest, there is a group of people partying.\nThey have a boat and want to help you.2\nYour journey has ended happily. 🍻\n\n    🎉  YOU ARE SAVED 🎉\n\n"
                + images.game_over,
                "3": "You are nearly at the beach when you hear a noise behind you.\nYou turn around and see a group of unfriendly looking people.\nThey are armed and you are taken captive.\nYour journey has ended.\n\n   💀  YOU ARE NEVER SEEN AGAIN  💀\n\n"
                + images.game_over,
            },
        },
        "night": {
            "description": "You are now in the dark jungle. The trees are tall and dense and all around you.\n"
            "You feel like a million eyes are watching you.\n"
            "All of a sudden a big black panther leaps from a tree.\n"
            "You are taken out and your journey has ended.\n\n    🪦  YOU'RE DEAD 🪦\n\n"
            + images.game_over,
        },
    },
    "cave": {
        "day": {
            "description": "You are now in the cave.\nIt's dark and damp, and you can hear the sound of dripping water.\n"
            "You see two paths ahead of you.\nThe left one is narrow and winding, and the other dark and deeper.\nOr you could head back to the beach.\n",
            "choices": {
                "1": "Go left down the narrow path",
                "2": "Or go right towards the dark and deeper path",
                "3": "Head back to the beach",
            },
            "outcome": {
                "1": "You have chosen to go left down the narrow path.\nYou walk for a while and come across a dead end.\nAs you go to turn a massive bolder FALLS from the celling.\nYou are trapped and your journey has ended.\n\n   🪨  UNFORTUNATELY YOU DIE   🪨\n\n"
                + images.game_over,
                "2": "You have chosen to go right towards the dark and deeper path.\nAs you go a little deeper you see a light in the distance.\nYou walk towards it and find a hidden exit.\nYou are on a small beach and there is a little rowing boat.\nYour journey has ended happily. 🚣🏻\n\n    🎉  YOU SAVE YOURSELF  🎉\n\n"
                + images.game_over,
                "3": "You have chosen to head back to the beach.\nYou run into some friendly pirates\nThey offer to drop you to the closest main land.\n\n  🏝️  YOU ARE SAFE  🏝️\n\n",
            },
        },
        "night": {
            "description": "You are now in the cave at night. It's pitch black and you can barely see your own hands.\n"
            "You hear a strange noise coming from the darkness.\n"
            "You decide to explore deeper into the cave.\n"
            "As you walk further, run into a massive bear. As you turn to run...\n"
            "The bear catches you and you are mauled to death.\n\n    🪦  YOU'RE DEAD 🪦\n\n"
            + images.game_over,
        },
    },
    "cliff": {
        "day": {
            "description": "You are now at the cliffs. The view is breathtaking and you can see the ocean far below. "
            "There is a narrow path leading down the cliffs, and another path going back to the jungle.\n"
            "You can choose to climb up, look for a way around, or go back to the jungle.\n",
            "choices": {
                "1": "You have chosen to climb down the cliffs. It's a challenging climb, but you manage to reach a secluded plato.",
                "2": "You have chosen to look for a way around. After a long walk, you find a hidden cave entrance.",
                "3": "You have chosen to go back to the jungle.",
            },
            "outcome": {},
        },
        "night": {
            "description": "You are now at the cliffs at night.\nThe wind is howling and it's hard to see anything above your head. "
            "You decide to climb the cliff.\n"
            "As you are climbing a rock falls and hits you on the head.\nYou lose your grip & fall into the darkness.\n\n    🪦  YOU'RE DEAD 🪦\n\n"
            + images.game_over,
        },
    },
}
