# Create a (10, 5) array of 10 batsmen × 5 match scores using np.random.randint(0, 150). Then: compute each player's average (axis=1), find the top 3 performers using np.argsort(), replace scores below 20 with 0 using boolean masking, normalize all scores to [0,1] using min-max: (x - min) / (max - min), stack with a second innings array using vstack and compute combined averages.


import numpy as np

# ===============================
# 1. Generate Data (10 players × 5 matches)
# ===============================
scores = np.random.randint(0, 150, size=(10, 5))
print("Scores:\n", scores)

# ===============================
# 2. Player Averages
# ===============================
averages = np.mean(scores, axis=1)
print("\nPlayer Averages:\n", averages)

# ===============================
# 3. Top 3 Performers
# ===============================
top_3_indices = np.argsort(averages)[-3:][::-1]
print("\nTop 3 Players (indices):", top_3_indices)
print("Top 3 Averages:", averages[top_3_indices])

# ===============================
# 4. Replace Scores < 20 with 0
# ===============================
scores[scores < 20] = 0
print("\nScores after replacing <20:\n", scores)

# ===============================
# 5. Min-Max Normalization
# ===============================
min_val = np.min(scores)
max_val = np.max(scores)

normalized = (scores - min_val) / (max_val - min_val)
print("\nNormalized Scores:\n", normalized)

# ===============================
# 6. Second Innings Data
# ===============================
second_innings = np.random.randint(0, 150, size=(10, 5))
print("\nSecond Innings:\n", second_innings)

# ===============================
# 7. Combine Both Innings
# ===============================
combined = np.vstack((scores, second_innings))
print("\nCombined Data Shape:", combined.shape)

# ===============================
# 8. Combined Averages
# ===============================
combined_avg = np.mean(combined, axis=1)
print("\nCombined Averages:\n", combined_avg)