import random

# -------------------
# NUMBER GUESSING GAME - LEVEL 6
# ----------------------

def choose_difficulty():
    print("\nChoose Difficulty")
    print("1. Easy   (1-50, 10 lives)")
    print("2. Medium (1-100, 7 lives)")
    print("3. Hard   (1-500, 5 lives)")

    while True:
        choice = input("Enter choice: ")

        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 500, 5
        else:
            print("❌ Invalid choice!")


def get_hint(number, guess):
    difference = abs(number - guess)

    if difference == 0:
        return "🎯 Perfect guess!"

    if difference <= 5:
        return "🔥 Very close!"
    elif difference <= 15:
        return "🙂 Close!"
    elif difference <= 30:
        return "😐 Far!"
    else:
        return "🥶 Very far!"


def one_player():
    print("\n========== 1 PLAYER MODE ==========")

    maximum, lives = choose_difficulty()

    number = random.randint(1, maximum)
    score = 100
    attempts = 0

    print("\n🎲 I have selected a number!")
    print("Guess a number between 1 and", maximum)

    while lives > 0:

        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        attempts += 1

        if guess == number:
            bonus = lives * 10
            score += bonus

            print("\n🎉 CONGRATULATIONS!")
            print("The number was:", number)
            print("Attempts:", attempts)
            print("Bonus:", bonus)
            print("🏆 Final Score:", score)
            return score

        lives -= 1
        score -= 10

        if guess < number:
            print("📈 Too LOW!")
        else:
            print("📉 Too HIGH!")

        print(get_hint(number, guess))
        print("❤️ Lives remaining:", lives)

    print("\n💀 GAME OVER!")
    print("The correct number was:", number)
    print("Final Score:", max(score, 0))

    return max(score, 0)


def two_player():
    print("\n========== 2 PLAYER MODE ==========")

    maximum, lives = choose_difficulty()

    print("\n👤 Player 1: Enter a secret number.")

    while True:
        try:
            number = int(input("Player 1, enter number: "))

            if 1 <= number <= maximum:
                break
            else:
                print("Enter a number between 1 and", maximum)

        except ValueError:
            print("❌ Enter a valid number.")

    print("\n" * 30)

    print("👤 Player 2: Guess the number!")
    print("Range: 1 to", maximum)

    attempts = 0

    while lives > 0:

        try:
            guess = int(input("\nPlayer 2 guess: "))
        except ValueError:
            print("❌ Enter a valid number.")
            continue

        attempts += 1

        if guess == number:
            score = lives * 20

            print("\n🎉 PLAYER 2 WINS!")
            print("Correct number:", number)
            print("Attempts:", attempts)
            print("🏆 Score:", score)

            return score

        lives -= 1

        if guess < number:
            print("📈 Too LOW!")
        else:
            print("📉 Too HIGH!")

        print(get_hint(number, guess))
        print("❤️ Lives remaining:", lives)

    print("\n🏆 PLAYER 1 WINS!")
    print("The secret number was:", number)

    return 0


def game():
    print("\n" + "=" * 40)
    print("       🎮 NUMBER GUESSING GAME")
    print("=" * 40)

    best_score = 0
    games_played = 0

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. 👤 1 Player")
        print("2. 👥 2 Players")
        print("3. 🏆 View Best Score")
        print("4. ❌ Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            score = one_player()
            games_played += 1

            if score > best_score:
                best_score = score
                print("🔥 NEW HIGH SCORE!")

        elif choice == "2":
            two_player()
            games_played += 1

        elif choice == "3":
            print("\n========== STATISTICS ==========")
            print("🎮 Games Played:", games_played)
            print("🏆 Best Score:", best_score)

        elif choice == "4":
            print("\n👋 Thanks for playing!")
            print("See you next time! 🎮")
            break

        else:
            print("❌ Invalid choice!")

        again = input("\nDo you want to continue? (yes/no): ")

        if again.lower() != "yes":
            print("\n👋 Game ended. Thanks for playing!")
            break


# Start Game
game()
