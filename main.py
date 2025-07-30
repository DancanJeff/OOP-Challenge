from pet import Pet

# Create a new pet
my_pet = Pet("Buddy")

# Initial status
print("Initial Status:")
my_pet.get_status()

# Feed the pet
print("\nFeeding Buddy...")
my_pet.eat()
my_pet.get_status()

# Play with the pet
print("\nPlaying with Buddy...")
my_pet.play()
my_pet.get_status()

# Teach some tricks
print("\nTeaching tricks...")
my_pet.train("Sit")
my_pet.train("Roll over")
my_pet.train("Sit")  # Already knows this trick
my_pet.show_tricks()

# Let the pet sleep
print("\nPutting Buddy to sleep...")
my_pet.sleep()
my_pet.get_status()
