def list_o_matic():
    animals = ['cat', 'goat', 'cat']
    
    while True:
        if not animals:
            print("Goodbye!")
            break
        
        print("Welcome, William. Look at all the animals " + str(animals))
        user_input = input("enter the name of an animal: ")
        
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        
        if user_input == "":
            if animals:
                popped_item = animals.pop()
                print(str(popped_item) + " popped from list")
            else:
                print("List is empty")
        else:
            if user_input in animals:
                animals.remove(user_input)
                print("1 instance of " + user_input + " removed from list")
            else:
                animals.append(user_input)
                print("1 instance of " + user_input + " appended to list")

list_o_matic()