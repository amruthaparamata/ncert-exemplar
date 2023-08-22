import numpy as np

# Number of dice rolls
n = 100000

# Simulate n rolls of a dice using Bernoulli distribution
# Use np.random.binomial(1, p) where p is the probability of success (rolling a 1)
rolls = np.random.binomial(1, 1/6, n)

# Compute the estimated probability of rolling a 1
estimated_probability = np.mean(rolls)

print(f"Estimated probability of rolling a 1 in {n} trials: {estimated_probability:.4f}")
