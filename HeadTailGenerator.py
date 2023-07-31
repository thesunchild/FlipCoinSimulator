# This program simulates flipping a coin a certain number of times.
# It imports the random module to generate random numbers.
import random

# This function flips a coin and returns "Heads" or "Tails".
def flip_coin():
    return random.choice(["Heads", "Tails"])

# This line asks the user to enter the number of flips.
flips = int(input("Flips: "))

# These two lines initialize the variables to count the number of heads and tails.
total_heads = 0
total_tails= 0

# This loop flips the coin the specified number of times.
for i in range(flips):
    # This line checks if the coin landed on heads.
    if (flip_coin()=="Heads"):
        # If so, it increments the total_heads counter.
        total_heads +=1
    else:
        # Otherwise, it increments the total_tails counter.
        total_tails +=1

# These two lines print the number of heads and tails.
print("Total Heads: " + str(total_heads))
print("Total Tails: " + str(total_tails))