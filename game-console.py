high_score = 1299

while True:
    print("========= Game Console =========")
    print(" ")
    print("1- Start Game")
    print("2- Instructions")
    print("3- High Score")
    print("4- Settings")
    print("5- Exit")
    print(" ")
    print("=================================")

    command = input("Enter your command: ").title()

    match command:
        case "Start Game":
            print("Game Started!")
            print("Good luck!")
        case "Instructions":
            print("W- Move up")
            print("S- Move down")
            print("D- Move right")
            print("A- Move left")
            print("Avoid enemies and collect points")
        case "High Score":
            print(f"High Score: {high_score}")
        case "Settings":
            setting = input("Enter the setting: ").title()

            match setting:
                case "Sound":
                    print("Volume Up")
                    print("Volume Down")
                case "Difficulty":
                    print("Easy")
                    print("Medium")
                    print("Hard")
                case "Back":
                    print("Good-bye")
        case "Exit":
            print("Good-Bye!")
            break
        case _:
            print("Invalid command!")