#I use 'better comments' extention for colorful commenting
#All finished practice exercises are turn into comment lines
#*Python Basics: A practical introduction to Python 3
    #@ex1:Concatenation
        #!1. Create a float object named weight with the value 0.2, and create
        #!a string object named animal with the value "newt". Then use these
        #!objects to print the following string using only string concatenation:
        #!0.2 kg is the weight of the newt. \\ OK
        #weight = 0.2;
        #animal = "newt";  
        #print(F"{weight}kg is the weight of the {animal}");  ## Finished~
    #@ ex2: find.() and replace.()
        #!1. In one line of code, display the result of trying to .find() the substring "a" in the string "AAA". The result should be -1. \\ OK
        #!2. Replace every occurrence of the character "s" with "x" in the string "Somebody said something to Samantha." \\ OK
        #!3. Write and test a script that accepts user input using the input() function and displays the result of trying to .find() a particular...
        #!letter in that input \\OK
        #print("a".find("AAA\n"));
        #print("Somebody said something to Samantha\n".replace("s","x"));
        #prompt = input("write a word with or without the letter 'a': ");
        #print("\n",prompt.find("a"));  #* Finished~
    #@ ex3: testing f string method and .f
        #speed = 1.2543;
        #sadness = f"time is {speed:.2f} faster";
       # print(sadness); #* Finished~
    #@ ex4: Loops: While and for:
        #!1. Write a for loop that prints out the integers 2 through 10, each on
        #!a new line, by using the range() function.
            #numbers = range(1,6);
            #for x in numbers:
                #    print(f"{x*2}");  #* Finished~
    #@ Challenge Chapter 6.5: Investment Calculator:
        # amount = int(input("inform the amount invested: "));
        # rate = float(input("inform the rate of profit per year"));
        #years = int(input("inform the years invested"));
        #def investment(A,R,Y):
            #"""Invests 'A' amount by 'R' rate for 'Y' years.""";
            #time = range(Y);
            #for Y in time:
            #    A = A + A*R;
            #    print(f'year {Y:}: ${A:.2f}');
        #investment(amount,rate,years); #* Finished~
    #@Challenge Chapter 7: Debugging
        ##Before Debugging:
        #def add_underscores(word):
            #new_word = "_"
            #for i in range(0, len(word)):
                #new_word = word[i] + "_" #! Error in operation, assignment Overwrites the value of new_word, but don't add the previous value.
        #return new_word
        #phrase = "hello"
        #print(add_underscores(phrase))

        ##After Debugging the for loop:
        #def add_underscores(word):
            #new_word = "_";
            #for i in range(0, len(word)): //  for char in word: ; 
                #new_word += word[i] + "_"; // new_word += word + "_";  #* Corrected Code
        #return new_word;
        #phrase = "hello";
        #print(add_underscores(phrase)); #* Finished~
    #@Challenge Chapter 8: Write a script that prompts the user to enter a word using the input() function, stores that input in a variable, and then displays whether the length of that string is less than 5 characters, greater than 5 characters, or equal to 5 characters by using a set of if, elif and else statements
        #print(f"Enter a number to find it's remainder");
        #number = int(input());
        #if number <=0:
        #    print(f"numbers under 0 have no remainder");
        #else:
        #    for i in range(1,number):
        #        if number % i == 0:
        #            print(f"{i} is a remainder of {number}");
        #            continue;
    #@Review Exercise chapter 8: Rolling the dice, whatever, i dont want to describe this one 
        #import random;
        #def rol():
        #    """Rolls a dice 10.000 times and gives the average number rolled"""
        #    #another of doing this is ordenating all numbers and finding the 5000th number, as it may also represent the average number rolled.
        #    #!but I'm too lazy to code that, so i will leave a Red comment for when i have more time and disposition.
        #    AverageNumber = 0;
        #    for n in range(10000):
        #        rol1 = random.randint(1,7);
        #        AverageNumber += rol1;
        #    Total = AverageNumber/10000
        #    return Total;   
        #print(rol()); #* Finished~

#You might be asking "Why don't you make different files for each exercise?" well, Because opening more than 1 file makes my computer run like a potato
#Also is quite easier for me to review code while coding, i keep the finished exercises folded and unfold them when necessary, 
#tho for OOP i will only do individual files, as it's exercises are way more complex than this previous chapters.
#! Challenge Coin Toss [page 228]: Create a program that calculates the average number of flips to have both tails and heads in a sequence (ex: heads, heads, tails// 3 flips for this trial) with 100 trials
import random;
def Cointoss():
    """This Function flips a coin until both heads and tails appear, than it sums the number of flips and start a new trial, after all trials, give the average number of flips"""
    flips = 0;
    for trials in range(1000):
        heads,tails = 0,0; #& turple method 'packing 'to declare multiple variables.
        while(tails < 1 or heads < 1):
            if random.randint(0,1) == 0:
                flips += 1; #& the variable unpacks without a problem. thank GOD :D
                heads += 1;
            else:
                flips += 1;
                tails += 1;
    average = flips/1000;
    return print(f"{average} is the number of average flips to have both heads and tails in a trial."); #* finished~
Cointoss();