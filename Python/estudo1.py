#Write a script named first_letter.py that first prompts the user for
#input by using the string "Tell me your password:" The script should
#then determine the first letter of the user’s input, convert that letter
#to upper-case, and display it back

prompt = "Tell me your password: ";
password = input(prompt);
password[0] = password.upper();

print(password[0]);