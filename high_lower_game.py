# import all data we need
from game_data import data
from art import logo, vs
import random
from replit import clear

# Generate a random index that's the current index
def get_random_index(A_index):
  while True:
    next_index = random.randint(0, len(data) - 1)
    if next_index != A_index:
      return next_index
def format_data(account):
  """Format the account data into printable format"""
  return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, a_follower, b_follower):
  """Take user's guess and follower account, and returns if the answer is correct"""
  if guess == 'A':
    if a_follower > b_follower
      return
  else:
    return a_follower < b_follower

def play_a_round(A_index):
  if A_index == -1:
    A_index = get_random_index(A_index)
  B_index = get_random_index(A_index)
  A_data = data[A_index]
  B_data = data[B_index]
  print(f"Compare A: {format_data(A_data)}")
  print(vs)
  print(f"Against B: {format_data(B_data)}")
  guess = input("Who has more followers? Type 'A' or 'B': ")
  answer_correct = check_answer(guess, A_data['follower'], B_data['follower'])
  if answer_correct:
    # Update the guessed index
    if guess == 'B':
      A_index = B_index
    return A_index
  else:
    return -1
    

A_index = -1
is_game_over = False
cur_score = 0
print(logo)
while not is_game_over:
  A_index = play_a_round(A_index)
  clear()
  print(logo)
  if A_index == -1:
    is_game_over = True
    print(f"Sorry, that's wrong. Your final score is {cur_score}")
  else:
    cur_score += 1
    print(f"You got it right. Your current score is {cur_score}")
    
