import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_form = [rock, paper, scissors]
human_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0, 2)
print(hand_form[int(human_choice)])
print(f"Computer chose:\n{hand_form[computer_choice]}")
if int(human_choice) == 0 and int(computer_choice) == 0:
  print("It's a draw")
elif int(human_choice) == 0 and int(computer_choice) == 1:
  print("You lose")
elif int(human_choice) == 0 and int(computer_choice) == 2:
  print("You win!")
elif int(human_choice) == 1 and int(computer_choice) == 0:
  print("You win!")
elif int(human_choice) == 1 and int(computer_choice) == 1:
  print("It's a draw")
elif int(human_choice) == 1 and int(computer_choice) == 2:
  print("You lose")
elif int(human_choice) == 2 and int(computer_choice) == 0:
  print("You lose")
elif int(human_choice) == 2 and int(computer_choice) == 1:
  print("You win!")
elif int(human_choice) == 2 and int(computer_choice) == 2:
  print("It's a draw")

# alternative

# hand_form = [rock, paper, scissors]
# human_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
# computer_choice = random.randint(0, 2)
# print(hand_form[int(human_choice)])
# print(f"Computer chose:\n{hand_form[computer_choice]}")
# you_win = ["02", "10", "21"]
# you_lose = ["01", "12", "20"]
# you_draw = ["00", "11", "22"]
# rules = [you_win, you_lose, you_draw]
# if human_choice + str(computer_choice) == rules[0][0] or rules[0][1] or rules[0][2]:
#   print("You win!")
# elif human_choice + str(computer_choice) == rules[1][0] or rules[1][1] or rules[1][2]:
#   print("You lose")
# elif human_choice + str(computer_choice) == rules[2][0] or rules[2][1] or rules[2][2]:
#   print("It's a draw")
