import random

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH =4 

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True:
        guess = input("Guess: " ).upper().split(" ")
        if len(guess) != 4:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
        
        """ here, the for-else framework executes as a whole
         else block runs only if the for loop completes without a break
         if a break occurs, the else block is skipped """
        
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color {color}, Try again.")
                break
        else:
            break
    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1
    

    return correct_pos, incorrect_pos


