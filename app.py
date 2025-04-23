import random

#write 'hello world' to the console
print("Hello, World!")

def play_game():
    options = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0  # Initialize player's score
    computer_score = 0  # Initialize computer's score
    
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors or 'quit' to exit): ").strip().lower()
        if player_choice == "quit":
            print(f"Thanks for playing! Final scores - You: {player_score}, Computer: {computer_score}")
            break
        if player_choice not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            player_score += 1  # Increment player's score
        else:
            print("You lose!")
            computer_score += 1  # Increment computer's score
        
        while True:
            play_again = input("Do you want to play again? (yes or no): ").strip().lower()
            if play_again in ["yes", "no"]:
                break
            print("Invalid response. Please answer 'yes' or 'no'.")
        
        if play_again != "yes":
            print(f"Thanks for playing! Final scores - You: {player_score}, Computer: {computer_score}")
            break

# Start the game
play_game()