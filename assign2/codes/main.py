import numpy as np

def simulate_dice_rolls(num_rolls):
    # Counter for the number of times we roll a '1'
    count_rolls_of_one = 0
    X = np.random.randint(1,7,num_rolls)
    # Calculate the probability estimate
    probability_estimate = len([i for i in X if i == 1]) / num_rolls
    
    return probability_estimate

# Simulate rolling a die 100,000 times
num_rolls = 100_000
estimated_probability = simulate_dice_rolls(num_rolls)

# Print the estimated probability
print(f"Estimated Probability of Rolling a '1' after {num_rolls} rolls: {estimated_probability:.4f}")
print("It's clearly not 0.5")
# Expected output (should be close to 1/6 = 0.1667)
