import random
import string


# Function for Snake Water Gun game
def snake_water_gun():
    a = "snake"
    b = "water"
    c = "gun"
    choices = [a, b, c]

    print("--Welcome to Snake Water Gun Game---")

    while True:
        computer = random.choice(choices)
        userinput = int(input("Enter 1 for snake, 2 for water, 3 for gun, 0 to exit: "))

        if userinput == 0:
            print("Game exits")
            break

        if userinput == 1:
            if computer == a:
                print("User choice:", a)
                print("Computer choice:", computer)
                print("Same choice draw", a, ":", a)
            elif computer == b:
                print("User choice:", a)
                print("Computer choice:", computer)
                print("User wins:", a)
            elif computer == c:
                print("User choice:", a)
                print("Computer choice:", computer)
                print("Computer wins:", c)

        elif userinput == 2:
            if computer == a:
                print("User choice:", b)
                print("Computer choice:", computer)
                print("Computer wins:", computer)
            elif computer == b:
                print("User choice:", b)
                print("Computer choice:", computer)
                print("Same choice draw:", b, ":", b)
            elif computer == c:
                print("User choice:", b)
                print("Computer choice:", computer)
                print("User wins:", b)

        elif userinput == 3:
            if computer == a:
                print("User choice:", c)
                print("Computer choice:", computer)
                print("User wins:", c)
            elif computer == b:
                print("User choice:", c)
                print("Computer choice:", computer)
                print("Computer wins:", computer)
            elif computer == c:
                print("User choice:", c)
                print("Computer choice:", computer)
                print("Same choice draw:", c, ":", c)

        else:
            print("Invalid input, please try again.")

        print("\n---Game starts again---")

    print("\n---Game ends---")


# Function for Secret Language Maker game
def secret_language_maker():
    print("Welcome user to Secret Language Maker game")

    user_str = input("Enter your string: ")
    if len(user_str) <= 3:
        reversed_str = ''
        for char in user_str:
            reversed_str = char + reversed_str
        print(reversed_str)
    else:
        first_letter = user_str[0]
        print("abcddfr", end='')
        print(user_str, end='')
        print("fdgdfgd", end='')
        print(first_letter)
    print(
        "If the length is less than 3, the string will be reversed. Otherwise, the first letter will be appended to the end.")


# Function for Kon Banega Crorepati (KBC) game
class KBC:
    def options(self):
        print("Welcome to Kon Banega Crorepati")
        self.options_list = ["Python", "C++", "JavaScript", "HTML"]

    def question(self):
        print("Which is the most used programming language around the globe?")
        print("Option a)", self.options_list[0], end="\t")
        print("Option b)", self.options_list[1], end="\n")
        print("Option c)", self.options_list[2], end="\t")
        print("Option d)", self.options_list[3], end="\n")
        print("You have to choose an option from 1 to 4 and 5 for lifelines")
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            print("Your answer is right:", self.options_list[0], "\n1 crore apka hua!")
            return
        elif user_choice == 2:
            print("Galat jawab! Ghar jayein, option a) Python correct")
            return
        elif user_choice == 3:
            print("Galat jawab! Ghar jayein, option a) Python correct")
            return
        elif user_choice == 4:
            print("Galat jawab! Ghar jayein, option a) Python correct")
            return
        elif user_choice == 5:
            self.lifeline()

    def lifeline(self):
        print("1) Phone a friend", end='\t')
        print("2) Audience poll", end='\t')
        print("3) 50/50")
        user_choice1 = int(input("Enter the lifeline you want: "))
        if user_choice1 == 1:
            print("Calling Talha Tabish...")
            print("Umer baway option a choose kr le")
            self.question()
        elif user_choice1 == 2:
            print("Audience poll started...")
            print("60% option a)")
            print("5% option b)")
            print("15% option d)")
            print("20% option c)")
            self.question()
        elif user_choice1 == 3:
            print("Which is the most used programming language around the globe?")
            print("Option a)", self.options_list[0], end="\t")
            print("Option c)", self.options_list[2], end="\n")
            user_choice2 = int(input("Enter the option (1 for a or 3 for c): "))
            if user_choice2 == 1:
                print("Your answer is right:", self.options_list[0], "\n1 crore apka hua!")
            else:
                print("Galat jawab! Ghar jayein, option a) Python correct")


# Function for Random Password Generator
def random_password_generator():
    pass_len = 12
    strval = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(pass_len):
        password = password + random.choice(strval)
    print("Your random password is: ", password)


# Function for Guess the Number game
def guess_the_number():
    print("---Welcome to Guess the Number game---")
    target = random.randint(1, 100)
    while True:
        userchoice = int(input("Enter the number you guess is right or press 0 to quit: "))
        if userchoice == 0:
            break
        if userchoice == target:
            print("You found the number!")
            break
        elif userchoice < target:
            print("Less than the target, try again.")
        else:
            print("Greater than the target, try again.")
    print("Game over.....")


# Main function to choose and run games
def main():
    print("Welcome to UMER'S GAME GALAXY!")

    while True:
        print("---Game Menu---")
        print("1. Snake Water Gun")
        print("2. Secret Language Maker")
        print("3. Kon Banega Crorepati (KBC)")
        print("4. Random Password Generator")
        print("5. Guess the Number")
        print("0. Exit")

        choice = int(input("Choose a game to play (0 to exit): "))

        if choice == 0:
            print("Exiting the program. Goodbye!")
            break
        elif choice == 1:
            snake_water_gun()
        elif choice == 2:
            secret_language_maker()
        elif choice == 3:
            kbc = KBC()
            kbc.options()
            kbc.question()
        elif choice == 4:
            random_password_generator()
        elif choice == 5:
            guess_the_number()
        else:
            print("Invalid choice. Please try again.")

main()
