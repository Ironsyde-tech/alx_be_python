# shopping_list_manager.py

shopping_list = []

def display_menu():
    print("===== Shopping List Menu =====")
    print("1. Add Item")
    print("2. View Shopping List")
    print("3. Exit")
    print("==============================")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("❌ Please enter a valid number.\n")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' added to your shopping list.\n")
            else:
                print("❌ Item cannot be empty.\n")
        elif choice == 2:
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
                print("")
            else:
                print("🛒 Your shopping list is empty.\n")
        elif choice == 3:
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
