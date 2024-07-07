print("Welcome to the quiz game!")


def start_quiz():
    """
    Starts the quiz game by asking the user questions and checking their answers.
    Restarts the quiz if the user answers any question incorrectly.
    """
    while True:
        start = input("Do you want to start the quiz? (yes/no) ")

        if start.lower() != "yes":
            print("Thanks for playing!")
            return
        else:
            print("Great! Let's start")

            # Question 1
            answer1 = input("What does CPU stand for? ")
            if answer1.lower() != "central processing unit":
                print("Wrong! Do you want to start again?")
                continue  # Restart the quiz
            else:
                print("Correct! :)")

            # Question 2
            answer2 = input("What does ALU stand for? ")
            if answer2.lower() != "arithmetic logic unit":
                print("Wrong! Do you want to start again?")
                continue  # Restart the quiz
            else:
                print("Correct! :)")

            # Question 3
            answer3 = input("What does GPU stand for? ")
            if answer3.lower() != "graphics processing unit":
                print("Wrong! Do you want to start again?")
                continue  # Restart the quiz
            else:
                print("Correct! :)")

            # Question 4
            answer4 = input("What does RAM stand for? ")
            if answer4.lower() != "random access memory":
                print("Wrong! Do you want to start again?")
                continue  # Restart the quiz
            else:
                print("Correct! :)")

            # Question 5
            answer5 = input("What does ROM stand for? ")
            if answer5.lower() != "read-only memory":
                print("Wrong! The quiz is over. Do you want to play again?")
                continue  # Restart the quiz
            else:
                print("Correct! You did very well :)")
                break  # End the quiz if all answers are correct


if __name__ == "__main__":
    while True:
        start_quiz()
        play_again = input("Do you want to start again? (yes/no) ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break
