# Probability distribution for the sums of two dice rolls
probability = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Read the number of rounds
R = int(input())  

# Initialize win counters for both players
player1_wins = 0
player2_wins = 0
draws = 0

# Process each round
for _ in range(R):
    # Read the dice rolls for both players
    P1_d1, P1_d2, P2_d1, P2_d2 = map(int, input().split())
    
    # Calculate the sums of both players
    P1_sum = P1_d1 + P1_d2
    P2_sum = P2_d1 + P2_d2
    
    # Get the probabilities of the sums
    P1_prob = probability[P1_sum]
    P2_prob = probability[P2_sum]
    
    # Compare the probabilities to determine the winner of the round
    if P1_prob < P2_prob:
        player1_wins += 1
    elif P2_prob < P1_prob:
        player2_wins += 1
    else:
        draws += 1

# Output the overall result
if player1_wins > player2_wins:
    print("Player 1 wins")
elif player2_wins > player1_wins:
    print("Player 2 wins")
else:
    print("It's a draw")
