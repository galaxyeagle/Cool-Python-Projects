import torch
import torch.nn as nn
import torch.optim as optim

# Simple feedforward network with 2 inputs (current guess, range midpoint)
class GuessNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 16),  # Input: normalized guess and range midpoint
            nn.ReLU(),
            nn.Linear(16, 1),  # Output: new guess (normalized)
            nn.Sigmoid()       # Keep output in [0, 1]
        )

    def forward(self, x):
        return self.net(x)

# Use standard MSE loss with feedback logic
def feedback_loss(guess, target, feedback):
    mse_loss = nn.MSELoss()
    if feedback == "correct":
        return mse_loss(guess, target)
    elif feedback == "higher":
        # Encourage guess to increase by setting a higher target
        adjusted_target = torch.tensor([[min(1.0, guess.item() + 0.1)]], dtype=torch.float32)
        return mse_loss(guess, adjusted_target)
    elif feedback == "lower":
        # Encourage guess to decrease by setting a lower target
        adjusted_target = torch.tensor([[max(0.0, guess.item() - 0.1)]], dtype=torch.float32)
        return mse_loss(guess, adjusted_target)
    else:
        raise ValueError("Invalid feedback: must be 'higher', 'lower', or 'correct'")

# Game loop with dynamic input and range tracking
def play_game():
    net = GuessNet()
    optimizer = optim.RMSprop(net.parameters(), lr=0.05)  # RMSprop with higher lr
    low, high = 1, 100  # Initial range
    current_guess = 50.0  # Start in the middle

    # Get target number
    target_number = int(input("Think of a number between 1 and 100 (we won't cheat): "))
    target_tensor = torch.tensor([[target_number / 100.0]], dtype=torch.float32)

    for round in range(1, 20):
        # Input: current guess and midpoint of current range (normalized)
        range_midpoint = (low + high) / 2.0
        input_tensor = torch.tensor([[current_guess / 100.0, range_midpoint / 100.0]], 
                                  dtype=torch.float32, requires_grad=True)
        
        # Get network's guess
        guess_tensor = net(input_tensor)
        guess_number = guess_tensor.item() * 100.0  # Scale to [0, 100]
        guess_number = max(low, min(high, guess_number))  # Clamp to current range
        
        print(f"Round {round}: I guess {int(guess_number)}")
        feedback = input("Feedback? (higher/lower/correct): ").strip().lower()

        # Update range based on feedback
        if feedback == "higher":
            low = max(low, guess_number + 1)
        elif feedback == "lower":
            high = min(high, guess_number - 1)
        elif feedback == "correct":
            print(f"Yay! Guessed it in {round} rounds! 🎉")
            break
        else:
            print("Invalid feedback. Please enter 'higher', 'lower', or 'correct'.")
            continue

        # Compute loss and update network
        loss = feedback_loss(guess_tensor, target_tensor, feedback)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Update current guess for next round
        current_guess = guess_number

    else:
        print("I couldn't guess it in 20 tries... Maybe you're cheating, partner! 😢")

if __name__ == "__main__":
    play_game()
