
#A Python Dictionary is a data structure that relates a set of keys to a set of values, each key is assigned to a value, which defines the relationship between the two sets
#Lists and Turple: Acess values by a index (ex: list[0]), Dictionaries: Acess itens by a key (ex: Dictionary["key1"])

#Review Exercises:
    #   captain = {}
    #   captain[ "Voyager"] = "Janeway"
    #   captain[ "Enterprise"] = "Picard"
    #   captain[ "Defiant"] = "Sisko"
    #   if 'Discovery' in captain:
    #       print(captain["Discovery"]);
    #   else:
    #       captain["Discovery"] = "Unknown";   
    #   for ship,captains in captain.items():
    #       print(f"the captain of {ship} is {captains}")
    #   del captain['Discovery']; #*finished~
#! Chapter 9.7 Challenge: Capital City Loop
#this is a game where a random state is choicen and the User needs to guess the correct capital
# it isnt case sensitive, so it works in every correct possible input.

import random;
capitals_dict = {
    'Alabama':'Montgomery',
    'Alaska':'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California':'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida':'Tallahassee',
    'Georgia':'Atlanta',
}
RandomState = random.choice(list(capitals_dict));
userInput = (input(f"What is the capital of {RandomState}?\n"))
for state, capital in capitals_dict.items():
    state = state.lower();
    capital = capital.lower();

userInput = userInput.lower();
while userInput != 0:
    if userInput == "exit":
        print("Goodbye");
        break;
    elif(userInput == capitals_dict[RandomState].lower()):
        print("Correct");
        break;
    else:
        print("Incorrect");
        break;