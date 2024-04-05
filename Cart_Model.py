from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_description(self):
        pass


class GroceryItem(Item):
    def __init__(self, name, price, category):
        super().__init__(name, price)
        self.category = category

    def get_description(self):
        return f"{self.name} ({self.category})"


class ElectronicsItem(Item):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def get_description(self):
        return f"{self.name} ({self.brand})"


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        else:
            return None

    def clear_cart(self):
        self.items.clear()

    def calculate_total_price(self):
        return sum(item.price for item in self.items)


def display_cart(cart):
    if not cart.items:
        print("Your cart is empty.")
    else:
        print("Shopping Cart:")
        total_price = 0
        for index, item in enumerate(cart.items, start=1):
            print(f"{index}. {item.get_description()}: ${item.price}")
            total_price += item.price
        print(f"Total: ${total_price:.2f}")


def main():
    cart = Cart()
    while True:
        print("\nShopping Cart Model")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Remove item from cart")
        print("4. Sign out (Empty cart)")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item_category = input("Enter item category (optional): ")
            if item_category:
                item = GroceryItem(item_name, item_price, item_category)
            else:
                item_brand = input("Enter item brand (optional): ")
                item = ElectronicsItem(item_name, item_price, item_brand)
            cart.add_item(item)
            print('Item added to cart!')
        elif choice == '2':
            display_cart(cart)
        elif choice == '3':
            if not cart.items:
                print("Your cart is already empty.")
            else:
                display_cart(cart)
                item_index = int(input("Enter the item number to remove: ")) - 1
                removed_item = cart.remove_item(item_index)
                if removed_item:
                    print(f"Removed item: {removed_item.get_description()}")
                else:
                    print("Invalid item number.")
        elif choice == '4':
            if not cart.items:
                print("Your cart is already empty.")
            else:
                cart.clear_cart()
                print("Cart signed out successfully. Your cart is now empty.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Choose a valid option.")


if __name__ == "__main__":
    main()
