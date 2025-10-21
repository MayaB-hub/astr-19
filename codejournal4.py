class Animal:
    def __init__(self, name, arm_length, leg_length, num_eyes, has_tail, is_furry):
        # animal's attributes
        self.name = name
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print(f"Animal name: {self.name}")
        print(f"Length of arms in feet: {self.arm_length}")
        print(f"Length of legs in feet: {self.leg_length}")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail: {self.has_tail}")
        print(f"Is furry: {self.is_furry}")

def main():
    cat = Animal("Cat", 0.3, 0.4, 2, True, True)
    cat.describe()

main()