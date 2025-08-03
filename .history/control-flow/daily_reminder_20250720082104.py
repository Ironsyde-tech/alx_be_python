# daily_reminder.py

# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the base reminder
reminder = ""

# Match on priority
match priority:
    case "high":
        reminder += f"🔥 Urgent Task: '{task}' (High Priority)"
    case "medium":
        reminder += f"📌 Task: '{task}' (Medium Priority)"
    case "low":
        reminder += f"📝 Task: '{task}' (Low Priority)"
    case _:
        reminder += f"⚠️ Task: '{task}' (Unspecified Priority)"

# Add time-sensitive message
if time_bound == "yes":
    reminder += " — ⚠️ This task requires **immediate attention today!**"
else:
    reminder += " — You can schedule this for later."

# Final output
print(reminder)
