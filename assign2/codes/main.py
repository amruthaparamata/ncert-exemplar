import random
# roll a dice 100000 times to compute the probability of rolling 1

import random

def simulate_dice_rolls(num_rolls):
    # Counter for the number of times we roll a '1'
    count_rolls_of_one = 0
    
    # Perform 'num_rolls' simulations
    for _ in range(num_rolls):
        # Simulate rolling a fair six-sided die
        roll_result = random.randint(1, 6)
        
        # Check if the roll result is '1'
        if roll_result == 1:
            count_rolls_of_one += 1
            
    # Calculate the probability estimate
    probability_estimate = count_rolls_of_one / num_rolls
    
    return probability_estimate

# Simulate rolling a die 100,000 times
num_rolls = 100000
estimated_probability = simulate_dice_rolls(num_rolls)

# Print the estimated probability
print(f"Estimated Probability of Rolling a '1' after {num_rolls} rolls: {estimated_probability:.4f}")
print("It's clearly not 0.5")
# Expected output (should be close to 1/6 = 0.1667)
