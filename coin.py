import random


def coin_toss():
    # Generate a random number (0 or 1) to represent heads or tails
    result = random.choice(["Heads", "Tails"])
    return result


def main():
    print("Welcome to the Heads or Tails game!")

    while True:
        user_choice = input("Enter 'H' for Heads or 'T' for Tails (or 'Q' to quit): ").upper()

        if user_choice == 'Q':
            break
        elif user_choice == 'H':
            user_choice = 'Heads'
        elif user_choice == 'T':
            user_choice = 'Tails'
        else:
            print("Invalid choice. Please enter 'H' for Heads, 'T' for Tails, or 'Q' to quit.")
            continue

        result = coin_toss()
        print(f"The coin landed on {result}!")

        if user_choice == result:
            print("Congratulations! You guessed correctly.")
        else:
            print("Sorry, you guessed wrong.")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
