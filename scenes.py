import time
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
                "1": "You have chosen to go left. You walk for a while and come across a sparkling river. "
                "The water looks refreshing, and you notice some colorful fish swimming beneath the surface. "
                "You can choose to swim across, fish on the bank, or head back to the beach.",
                "2": "You have chosen to go right. You walk through the dense jungle and encounter a group of friendly monkeys. "
                "They offer to show you a hidden path or lead you back to the beach.",
                "3": "You have chosen to head back to the beach.",
            },
        },
        "night": {
            "description": "You are now in the dark jungle. The trees are tall and dense and all around you.\n"
            "You feel like a million eyes are watching you.\n"
            "All of a sudden a big black panther leaps from a tree.\n"
            "You are taken out and your journey has ended.\n    🪦  YOU'RE DEAD 🪦\n\n"
            # + time.sleep(3)
            + images.game_over,
        },
    },
    "cave": {
        "day": {
            "description": "You are now in the cave. It's dark and damp, and you can hear the sound of dripping water.\n"
            "You see two paths ahead of you. The left one is narrow and winding, and the other dark and deeper.\n"
            "Or you can head back to the beach.\n",
            "choices": {
                "1": "Go left down the narrow path",
                "2": "Or go right towards the dark and deeper path",
                "3": "Head back to the beach",
            },
            "outcome": {},
        },
        "night": {
            "description": "You are now in the cave at night. It's pitch black and you can barely see your own hands.\n"
            "You hear a strange noise coming from the darkness.\n"
            "You decide to explore deeper into the cave.\n"
            "As you walk further, run into a massive bear. As you turn to run...\n"
            "The bear catches you and you are mauled to death.\n    🪦  YOU'RE DEAD 🪦\n\n"
            # + time.sleep(3)
            + images.game_over,
        },
    },
    "cliffs": {
        "day": [
            "You are now at the cliffs. The view is breathtaking and you can see the ocean far below. "
            "There is a narrow path leading down the cliffs, and another path going back to the jungle.\n"
            "You can choose to climb down, look for a way around, or go back to the jungle."
        ],
        "choices": {
            "1": "You have chosen to climb down the cliffs. It's a challenging descent, but you manage to reach a secluded beach.",
            "2": "You have chosen to look for a way around. After a long walk, you find a hidden cave entrance.",
            "3": "You have chosen to go back to the jungle.",
        },
        "night": [
            "You are now at the cliffs at night.\nThe wind is howling and it's hard to see anything above your head. "
            "You decide to climb the cliff.\n"
            "As you are climbing a rock falls and hits you on the head.\nYou lose your grip  & fall into the darkness.\n    🪦YOU'RE DEAD🪦\n\n"
            + images.game_over,
        ],
    },
}
