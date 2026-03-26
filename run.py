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
    print("3. Update Session")
    print("4. Delete Session")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            while True:
                subject = input("Enter subject: ").strip()
                if subject == "":
                    print("Subject cannot be empty.")
                else:
                    break

            while True:
                duration = input("Enter duration (minutes): ").strip()
                if not duration.isdigit():
                    print("Please enter a valid number.")
                else:
                    break

            session = {"subject": subject, "duration": duration}
            sessions.append(session)
            save_sessions(sessions)
            print("Session added successfully!")

        elif choice == "2":
            if not sessions:
                print("No sessions found.")
            else:
                total_time = 0

                for i, session in enumerate(sessions, start=1):
                    subject = session["subject"]
                    duration = int(session["duration"])
                    total_time += duration
                    print(f"{i}. {subject} - {duration} mins")

                print(f"\nTotal study time: {total_time} mins")

        elif choice == "3":
            if not sessions:
                print("No sessions to update.")
            else:
                for i, session in enumerate(sessions, start=1):
                    print(f"{i}. {session['subject']} - {session['duration']} mins")

                index = input("Enter session number to update: ")

                if not index.isdigit() or int(index) < 1 or int(index) > len(sessions):
                    print("Invalid selection.")
                else:
                    index = int(index) - 1

                    new_subject = input("Enter new subject: ").strip()
                    new_duration = input("Enter new duration: ").strip()

                    if new_subject == "" or not new_duration.isdigit():
                        print("Invalid input. Update cancelled.")
                    else:
                        sessions[index]["subject"] = new_subject
                        sessions[index]["duration"] = new_duration
                        save_sessions(sessions)
                        print("Session updated successfully!")

        elif choice == "4":
            if not sessions:
                print("No sessions to delete.")
            else:
                for i, session in enumerate(sessions, start=1):
                    print(f"{i}. {session['subject']} - {session['duration']} mins")

                index = input("Enter session number to delete: ")

                if not index.isdigit() or int(index) < 1 or int(index) > len(sessions):
                    print("Invalid selection.")
                else:
                    index = int(index) - 1

                    confirm = input("Are you sure? (y/n): ").lower()

                    if confirm == "y":
                        sessions.pop(index)
                        save_sessions(sessions)
                        print("Session deleted successfully!")
                    else:
                        print("Deletion cancelled.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
