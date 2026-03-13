"""
Exercise 2.1 - Implementing Methods

Goal: Implement at least TWO methods in the class you previously designed in the previous exercises.

STEP-BY-STEP:
    STEP 1 — Choose AT LEAST TWO Methods You Wrote Earlier and Implement It (you can do more)
        Your method MUST:
            Receive at least one parameter (besides self)
            Modify at least one attribute
            return a message or result

            For example:
                If your class was a GameCharacter a simple method could:
                    def take_damage(self, amount):
                        self.health -= amount
                        return f"{self.name} now has {self.health} HP."

    STEP 2 — Create an instance of the object and Call Your Methods separately

    STEP 3 — Test Your Methods Thoroughly
        Write at least three test cases - for example:

            obj = MyClass("A", "B", "C", 10)
            print(obj.take_damage(5))
            print(obj.take_damage(10))
            print(obj.take_damage(3))
"""
class persona:
    def __init__(self,name,arcana,baseLVL,compendium_price,registered = False):
        self.name = name
        self.arcana = arcana
        self.compendium_price = compendium_price
        self.current_lvl = baseLVL
        self.baseLVL = baseLVL
        self.exp = 0
        self.registered = registered
        self.weakness = []
        self.resistance = []
        self.base_skills = []
        self.learnable_skills = []

    def level_up(self,lvl):

        self.current_lvl += lvl
        return f"{self.name} has leveled up! Their current level is now {self.current_lvl}"

    def skill_learned(self,skills):
        pass

    def skill_card_use(self,new_skill):
        pass

    def register_persona(self):
        self.registered = True
        return f"{self.name} has been added to the Compendium."
