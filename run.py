import json


def save_sessions(sessions):
    with open("sessions.json", "w") as file:
        json.dump(sessions, file)


def load_sessions():
    try:
        with open("sessions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


sessions = load_sessions()


def show_menu():
    print("\nStudy Tracker Menu")
    print("1. Add Session")
    print("2. View Sessions")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            subject = input("Enter subject: ")
            duration = input("Enter duration (minutes): ")

            session = {
                "subject": subject,
                "duration": duration
            }

            sessions.append(session)
            save_sessions(sessions)
            print("Session added successfully!")

        elif choice == "2":
            if not sessions:
                print("No sessions found.")
            else:
                for i, session in enumerate(sessions, start=1):
                    subject = session["subject"]
                    duration = session["duration"]
                    print(f"{i}. {subject} - {duration} mins")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
