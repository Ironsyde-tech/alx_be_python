shopping_list = []

def display_menu():
    print("\n===== Shopping List Menu =====")
    print("1. Add Item")
    print("2. View Shopping List")
    print("3. Exit")
    print("==============================")

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.\n")
        continue

    if choice == 1:
        item = input("Enter the item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"✅ '{item}' added.\n")
        else:
            print("❌ Empty input not allowed.\n")
    elif choice == 2:
        if shopping_list:
            print("\n🛒 Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("🛒 Shopping list is empty.\n")
    elif choice == 3:
        print("👋 Exiting. Goodbye!\n")
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.\n")
