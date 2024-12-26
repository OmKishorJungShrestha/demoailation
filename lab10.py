#lab10 
# Rule-based system
def rule_based_system(facts):
    rules = [
        ("if it is raining, then take an umbrella", lambda facts: "raining" in facts),
        ("if it is cold, then wear a coat", lambda facts: "cold" in facts),
        ("if you are going outside and it is raining, then take an umbrella", lambda facts: "going_outside" in facts and "raining" in facts),
    ]
    
    actions = []
    for rule, condition in rules:
        if condition(facts):
            actions.append(rule)
    
    return actions

# Semantic network and Animal class
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
        self.network = {}
    
    def add_relationship(self, parent, child):
        if parent not in self.network:
            self.network[parent] = []
        self.network[parent].append(child)
    
    def display(self):
        for parent, children in self.network.items():
            for child in children:
                print(f"{parent} → {child}")
    
    def make_sound(self):
        return self.sound

class SemanticNetwork:
    def __init__(self):
        self.network = {}
    
    def add_relationship(self, parent, child):
        if parent not in self.network:
            self.network[parent] = []
        self.network[parent].append(child)
    
    def display(self):
        for parent, children in self.network.items():
            for child in children:
                print(f"{parent} → {child}")

if __name__ == "__main__":
    # Rule-based system test
    facts = ["raining", "going_outside"]
    actions = rule_based_system(facts)
    print("Rule-based Actions:", actions)

    # Adding a predicate logic action print
    if "if it is raining, then take an umbrella" in actions:
        print("Predicate Logic Action: Take an umbrella")
    elif "if it is cold, then wear a coat" in actions:
        print("Predicate Logic Action: Wear a coat")
    elif "if you are going outside and it is raining, then take an umbrella" in actions:
        print("Predicate Logic Action: Take an umbrella")
    else:
        print("Predicate Logic Action: No action needed")

    # Semantic network implementation
    print("\nSemantic Network Relationships:")
    dog = Animal("Buddy", "dog", "woof")
    cat = Animal("Whiskers", "cat", "meow")
    
    print(f"{dog.name} says: {dog.make_sound()}")
    print(f"{cat.name} says: {cat.make_sound()}")
    
    # Semantic network relationships
    semantic_net = SemanticNetwork()
    semantic_net.add_relationship("Animal", "Dog")
    semantic_net.add_relationship("Animal", "Cat")
    semantic_net.add_relationship("Dog", "Barks")
    semantic_net.add_relationship("Cat", "Meows")
    
    print("\nSemantic Network:")
    semantic_net.display()

