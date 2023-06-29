#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 12/16/2022
#Project: Final Project, Password Hash Cracker
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"In this project, you will create a Python program that can "crack" a password by guessing-and
#checking all possible combinations of letters and numbers (i.e., "strings"). When users run your 
#program, they will input the name of a file that contains one or more username and password 
#hashes (i.e., encrypted passwords). For each hash, your program will generate all possible 
#combinations of letters and numbers (up to 8 characters; upper/lower case letters and numbers) in 
#order to find a string that produces an identical hash value. Your program will save these "cracked" 
#passwords and write them to an output file."
#--------------------------------------------------------------------------------------------
#ALGORYTHM
#-----------------
#Step 1) Display explanation of program.
#Step 2) Get input file name from user.
#Step 3) Get output file name from user.
#Step 4) Create a list of the contents within the input file.
#Step 5) Sort the information in the list and crack the stored hash values.
#Step 6) Print the results to the screen and to a file.
#Step 7) Prompt user to enter if they would like to go again.
#--------------------------------------------------------------------------------------------
import final_helper

# The display_greeting function is used to display an explanation of the purpose of the program.
# This function uses formatted f string to display a heading.
def display_greeting():
    line_1 = 'This program takes the name of a file that contains usernames and password hashes.'
    line_2 = 'After getting the name of the file the user wishes to crack the contents of, the'
    line_3 = 'program will proceed to crack the contents of the file. The program will output'
    line_4 = 'the results to a file and display to the results to the screen.'
    print()
    print('-' * 90)
    print('|' + f'{"Password Cracking Program":^88}' + '|')
    print('-' * 90)
    print('|' + f'{line_1:<88}' + '|')
    print('|' + f'{line_2:<88}' + '|')
    print('|' + f'{line_3:<88}' + '|')
    print('|' + f'{line_4:<88}' + '|')
    print('-' * 90)

# The create_heading function is used to print a heading inside of the output file.
# This function uses formatted f string to display a heading.
def create_heading(output_file_name):
    output_file = open(output_file_name, 'w')
    print('-' * 90, file = output_file)
    print('|' + f'{"Password Cracking Program Results":^88}' + '|', file = output_file)
    print('-' * 90, file = output_file)
    output_file.close()

# The get_input_input_file_name function is used to get the name of the file that the user wishes
# to crack the contents of. This function validates that the input file name is not an empty string.
# Finally it returns the input file name.
def get_input_input_file_name(title, ext = '.txt'):
    not_done = True
    iterations = 0
    while not_done:
        try:
            input_file_name = input(title)
            print('-' * 90)
            if input_file_name != '':
                if not ext in input_file_name:
                    input_file_name += ext
                input_file = open(input_file_name, 'r')
                input_file.close()
                not_done = False
            else:
                print('File names cannot be blank. Please re-enter.')
                print('-' * 90)
            iterations += 1
        except FileNotFoundError:
            print('No such file or directory: ' + input_file_name)
    return input_file_name

# The get_output_file_name function is used to get the name of the file that the user wishes
# to store the cracked contents of the input file. This function validates that the input file
# name is not an empty string. Also, this function varifies that the file can be overwritten
# if it already exist.
def get_output_file_name(title, ext = '.txt'):
    not_done = True
    iterations = 0
    while not_done:
        output_file_name = input(title)
        print('-' * 90)
        if output_file_name != '':
            not_done = False
            if not ext in output_file_name:
                output_file_name += ext
                try:
                    output_file = open(output_file_name, 'r')
                    line = output_file.readline()
                    output_file.close()
                    if line != '':
                        print('Warning! File already exists and contains content.')
                        print('Press "Y" to continue and over write or ENTER to choose another name.')
                        overwrite = input('Do you wish to continue and overwrite the contents? ')
                        print('-' * 90)
                        if overwrite.capitalize() != 'Y':
                            not_done = True
                except FileNotFoundError:
                    return output_file_name
        else:
            print('File names cannot be blank. Please re-enter.')
            print('-' * 90)
        iterations += 1
    return output_file_name

# The read_file function is used to read the input file and store its contents inside of a list.
# This function sorts out the value that has no purpose for this program and excludes it from the list.
# This function returns the created list.
def read_file(input_file_name):
    username_password_hash_list = []
    input_file = open(input_file_name, 'r')
    line = input_file.readline()
    while line != '':
        try:
            username = line.rstrip()
            line = input_file.readline()
            if line != '':
                line = line.rstrip()
                password_hash, trash_value = line.split(':')
            elif line == '':
                password_hash, trash_value = 'No password hash input.', 'No trash input.'
            username_password_hash_list.append(username)
            username_password_hash_list.append(password_hash)
            line = input_file.readline()
        except ValueError:
            print('ERROR: This file does not contain the correct content or the content is out of order.')
            line = ''
    input_file.close()
    return username_password_hash_list

# The crack_list function is used to decide if the item in the list is a username or hash value
# and print a formatted header of what user name and hash it is working on. When this function
# finds a hash value, it calls the hash_cracker function. This function also prints the results
# to the output file.
def crack_list(username_password_hash_list, output_file_name):
    iterations = 2
    create_heading(output_file_name)
    output_file = open(output_file_name, 'a')
    for element in username_password_hash_list:
        if iterations % 2 == 0:
            print('|' + f'{"Attempting to Crack":^88}' + '|')
            print('-' * 90)
            print('|' + f'{"Username: " + element:^88}' + '|')
            print('-' * 90)
            iterations += 1
            print('-' * 90, file = output_file)
            print('|' + f'{"Username: " + element:^88}' + '|', file = output_file)
            print('-' * 90, file = output_file)
        else:
            unknown_password_hash = element
            print('|' + f'{"Unknown Hash: " + element:^88}' + '|')
            print('-' * 90)
            cracked_password = hash_cracker(unknown_password_hash)
            print('-' * 90)
            print('|' + f'{"Cracked Password: " + cracked_password:^88}' + '|')
            print('-' * 90)
            iterations += 1
            print('|' + f'{"Unknown Hash: " + element:^88}' + '|', file = output_file)
            print('-' * 90, file = output_file)
            print('|' + f'{"Cracked Password: " + cracked_password:^88}' + '|', file = output_file)
            print('-' * 90, file = output_file)
    output_file.close()

# The hash_cracker function is used to create all possible hash values for passwords containing character
# and numbers up to eight characters long. The function uses nested for loops to generate the hashes and
# compares the hashes to the unknown password hash. The function returns the cracked password.
def hash_cracker(unknown_password_hash):
    iterations = 1
    all_possible_characters = [' ']
    for char in range(97, 123):
        all_possible_characters.append(chr(char))
    for char in range(65, 91):
        all_possible_characters.append(chr(char))
    for num in range(48, 58):
        all_possible_characters.append(chr(num))

    padding = 'Computing'
    reset = ' ' * 10

    for letter_8 in all_possible_characters:
        for letter_7 in all_possible_characters:
            for letter_6 in all_possible_characters:
                for letter_5 in all_possible_characters:
                    for letter_4 in all_possible_characters:
                        print(f"{padding}{'.':.>{iterations}}{reset}", end = '\r')
                        iterations += 1
                        if iterations > 10:
                            iterations = 1
                        for letter_3 in all_possible_characters:
                            for letter_2 in all_possible_characters:
                                for letter_1 in all_possible_characters:
                                    possible_password = letter_1 + letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter_7 + letter_8
                                    possible_password_hash = final_helper.get_password_hash(possible_password)
                                    if possible_password_hash == unknown_password_hash:
                                        cracked_password = possible_password
                                        print()
                                        return cracked_password

# The again function is used to determine if the user would like to run another frequency count.
def go_again():
    print('Your results have been printed to a file.')
    print('Enter "yes" to go again or "no" to quit.')
    yes_no = input('Do you want to do this again? ')
    return yes_no.lower() == 'yes'

# The display_good_bye_message is used to display good bye.
def display_good_bye_message():
    print('-' * 90)
    print('|' + f'{"Good-Bye!":^88}' + '|')
    print('-' * 90)
    
# The main function is used to call all the function neccassary for completing the programming task.
def main():
    display_greeting()
    again = True
    while again == True:
        input_file = get_input_input_file_name('What is the name of the file that you wish to crack the contents of? ')
        output_file = get_output_file_name('What is the name of the file that you wish to store the cracked contents within? ')
        username_password_hash_list = read_file(input_file)
        crack_list(username_password_hash_list, output_file)
        again = go_again()
    display_good_bye_message()

# Call the main function if name == '__main__'
if __name__ == '__main__':
    main()