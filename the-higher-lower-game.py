#import logo and game_data 
#import random module to use for randomizing items from the list
#access each item of the "data" list(dictionaries are the items), access the values of the dictionaries through keys
#pick a random item from the "data" list
#write up the basic text comparing the items from the list
#use a while loop to keep playing the game until the user guesses wrong
#make a counter for the score user has achieved
#for successive correct guesses transfer item from B to A position
#break the while loop using a flag for when user guesses wrong
#make sure you don't get the same item and compare it with itself in the comparison(remove the item from the list while it's being compared)
#use a for loop to go through randomized choices from the list
#compare the follower count between items
from art import logo, vs
from game_data import data
import random


#creating a list of two random items from data list
list_of_items = []
for _ in range(0,2):
  random_item = random.choice(data)
  list_of_items.append(random_item)

#items as dictionaries
a = list_of_items[0]
x = list_of_items[1]
#avoiding comparing the same item with itself
while a['name'] == x['name']:
  x = random.choice(data)

#calling the keys from each dictionary(item)

print(logo)
print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
print(vs)
print(f"Against B: {x['name']}, a {x['description']}, from {x['country']}.")
guess = input("Who has more followers? Type 'A' or 'B': ")


#determining which item has a higher value and placing it in a dictionary
higher_value = {}
if a['follower_count'] > x['follower_count']:
  higher_value = {"A": a['follower_count']}
else:
  higher_value = {"B": x['follower_count']}

#extracting key from the dictionary(item)
for higher_value1 in higher_value:
  something = 0



i = 0
answer = True
while answer:
  if guess == higher_value1:
    print(logo)

    print(f"You're right! Current score: {i+1}.")
    i += 1

    print(f"Compare A: {x['name']}, a {x['description']}, from {x['country']}.")
    print(vs)
    y = random.choice(data)
    #avoiding to compare the same items
    while y['name'] == x['name']:
      y = random.choice(data)
    print(f"Against B: {y['name']}, a {y['description']}, from {y['country']}.")
    
    #testing
    higher_value = {}
    if x['follower_count'] > y['follower_count']:
      higher_value = {"A": x['follower_count']}
    else:
      higher_value = {"B": y['follower_count']}

    for higher_value1 in higher_value:
      something = 0

    guess = input("Who has more followers? Type 'A' or 'B': ")
    
    z = y
    x = z


    
  else:
    print(logo)
    print(f"Sorry, that's wrong. Final score: {i}")
    answer = False


