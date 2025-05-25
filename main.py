import random

# choices = [1, -1, 0]
# result = random.choice(choices)
# print(result)
print("Welcome to Snake, Water & Gun Game!")
print("Let's play!")
com = random.choice([1, -1, 0])
user_ip = input("\nEnter your Choice: (s)nake, (w)ater, (g)un ") # s,w,g
user_dict = {"s":1,"w":-1,"g":0}
com_dict = {1:"Snake",-1:"Water",0:"Gun"}
user = user_dict[user_ip]

print(f"You chose: {com_dict[user]}\nComputer chose: {com_dict[com]}")

# Winning conditions: (com, user)
win_cases = [(-1, 1), (1, 0), (0, -1)]

# Losing Condition: (com,user)
lose_cases = [(-1, 0), (1, -1), (0, 1)]

if (com, user) in win_cases:
    print("You win")
elif (com, user) in lose_cases:
    print("You Lose")
else:
    # everything else is a tie
    print("Tie")
