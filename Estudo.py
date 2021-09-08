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
            #for i in range(0, len(word)): // for char in word;
                #new_word += word[i] + "_"; // new_word += word + "-";  #* Corrected Operation
        #return new_word;
        #phrase = "hello";
        #print(add_underscores(phrase)); #* Finished~
    #! Challenge Coin Toss page 228
    #! Challenge Randomization of a String using random