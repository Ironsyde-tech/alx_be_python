# daily_reminder.py

# Prompt the user for task input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority level
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unrecognized priority level"

# Add time-sensitive note
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

elif priority in ["low", "medium", "high"]:
    reminder += ". Consider completing it when you have free time."

# Print the final reminder
print(reminder)
