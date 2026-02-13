"""
Shopping List Command Line Application
Author: [Your Name]
Description: A persistent shopping list manager with file storage and interactive commands.
"""

class ShoppingList:
    def __init__(self):
        self.items = {}
        self.filename = "shopping_list.txt"
        self.load_items()
    
    def start_menu(self):
        print("What do you want to add to your shopping list?")
        print("Enter 'DONE' to stop adding items.")
        print("Enter 'HELP' for additional info.")
        print("Enter 'SHOW' to see your shopping list.")
        print("Enter 'REMOVE' to remove an item from your shopping list.")
        print("Enter 'CLEAR' to clear all items from your list.")
        print("Enter 'SEARCH' to find items by substring.")
        print("-----------------------------------------")
    
    def add_to_list(self, item):
        quantity = 1
        
        if ' x' in item.lower():
            parts = item.rsplit('x', 1)
            if len(parts) == 2 and parts[1].strip().isdigit():
                item = parts[0].strip()
                quantity = int(parts[1].strip())
        
        normalized_item = item.capitalize()
        
        if normalized_item in self.items:
            print(f"{normalized_item} already exists in your shopping list.")
        else:
            self.items[normalized_item] = quantity
            if quantity > 1:
                print(f"{normalized_item} x{quantity} was added to your shopping list.")
            else:
                print(f"{normalized_item} was added to your shopping list.")
            print(f"You have {len(self.items)} items on your list.")
    
    def remove_item(self, item):
        normalized_item = item.capitalize()
        
        if normalized_item in self.items:
            del self.items[normalized_item]
            print(f"{normalized_item} was removed from your shopping list.")
            print(f"You have {len(self.items)} items on your list.")
        else:
            print(f"{normalized_item} not found in your shopping list.")
    
    def show_shopping_list(self):
        print("My Shopping List:")
        if not self.items:
            print("(empty)")
        else:
            sorted_items = sorted(self.items.items())
            for item, quantity in sorted_items:
                if quantity > 1:
                    print(f"- {item} x{quantity}")
                else:
                    print(f"- {item}")
    
    def clear_list(self):
        if not self.items:
            print("Your shopping list is already empty.")
            return
        
        self.show_shopping_list()
        confirm = input("Are you sure you want to clear all items? (yes/no): ").strip().lower()
        if confirm == 'yes':
            self.items.clear()
            print("All items have been cleared from your shopping list.")
        else:
            print("Clear operation cancelled.")
    
    def search_items(self, query):
        query_lower = query.lower()
        found_items = []
        
        for item in self.items:
            if query_lower in item.lower():
                found_items.append(item)
        
        if found_items:
            print(f"Found {len(found_items)} item(s) matching '{query}':")
            for item in sorted(found_items):
                quantity = self.items[item]
                if quantity > 1:
                    print(f"- {item} x{quantity}")
                else:
                    print(f"- {item}")
        else:
            print(f"No items found matching '{query}'.")
    
    def save_items(self):
        try:
            with open(self.filename, 'w') as file:
                for item, quantity in self.items.items():
                    file.write(f"{item}:{quantity}\n")
        except IOError as e:
            print(f"Error saving shopping list: {e}")
    
    def load_items(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if ':' in line:
                        item, quantity = line.rsplit(':', 1)
                        try:
                            self.items[item] = int(quantity)
                        except ValueError:
                            self.items[item] = 1
                    elif line:
                        self.items[line] = 1
        except FileNotFoundError:
            pass
        except IOError as e:
            print(f"Error loading shopping list: {e}")
    
    def run(self):
        self.start_menu()
        
        try:
            while True:
                try:
                    user_input = input("> ").strip()
                    
                    if not user_input:
                        continue
                    
                    command = user_input.upper()
                    
                    if command == "DONE":
                        print("See you soon!")
                        self.save_items()
                        print("Your shopping list has been saved.")
                        self.show_shopping_list()
                        break
                    
                    elif command == "HELP":
                        self.start_menu()
                    
                    elif command == "SHOW":
                        self.show_shopping_list()
                    
                    elif command == "REMOVE":
                        self.show_shopping_list()
                        item_to_remove = input("What do you want to remove?: ").strip()
                        if item_to_remove:
                            self.remove_item(item_to_remove)
                    
                    elif command == "CLEAR":
                        self.clear_list()
                    
                    elif command == "SEARCH":
                        query = input("Enter search term: ").strip()
                        if query:
                            self.search_items(query)
                    
                    else:
                        self.add_to_list(user_input)
                
                except EOFError:
                    print("\nSee you soon!")
                    self.save_items()
                    print("Your shopping list has been saved.")
                    self.show_shopping_list()
                    break
        
        except KeyboardInterrupt:
            print("\nSee you soon!")
            self.save_items()
            print("Your shopping list has been saved.")
            self.show_shopping_list()


def main():
    shopping_list = ShoppingList()
    shopping_list.run()


if __name__ == '__main__':
    main()
