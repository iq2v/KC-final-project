import random
class Animal:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
        self.health = random.randint(0, 10)
            
    def feed(self):
        self.hunger -= 2
        self.happiness += 1
        self.health += 1
    
    def play(self):
        self.hunger += 1
        self.happiness += 2
        self.health += 1
    
    def check_status(self):
        print(f"{self.name} - Hunger: {self.hunger}, Happiness: {self.happiness}, Health: {self.health}")

def main():
    print("Welcome to the Animal Care Game!")
    animal_name = input("Enter your animal's name: ")
    animal = Animal(animal_name)
    
    while True:
        print("\nOptions:")
        print("1. Feed your animal")
        print("2. Play with your animal")
        print("3. Check animal's status") 
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            animal.feed()
            print(f"You fed {animal.name}.")
        elif choice == "2":
            animal.play()
            print(f"You played with {animal.name}.")
        elif choice == "3":
            animal.check_status()
        elif choice == "4":
            print("well done you took good care of your animal today!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


