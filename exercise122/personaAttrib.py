"""
2.2 - Hidden Attributes and Getters/Setters

Goal: You will modify your existing class from previous lessons.

STEP-BY-STEP:
    STEP 1 — Add a Protected Attribute
        Choose one attribute that the object should not be changed directly by outside code (but can still be read if needed).
        Add it using one underscore:
            For example:
                self._protected_value = 10

    STEP 2 - Add a Private Attribute
        Choose another attribute that should be fully hidden from users, because it affects internal logic.
            Add it using two underscores:
            For example:
                self.__private_value = 100

    STEP 3 - Write a Getter Method (for one of your protected or private methods)

    STEP 4 - Write a Setter Method and include a validation check before the return (for one of your protected or private methods)

    STEP 5 — Demonstrate Your Getter and Setter Methods

        After you finish the class:
        - Create an object
        - Try printing the protected attribute
        - Use your getter to read the private attribute
        - Use your setter to change the private attribute
        - Print the private value again to confirm it changed
"""
class persona:
    def __init__(self,name,arcana,baseLVL,compendium_price,registered = False):
        self._obtainable = False
        self.__internal_id = 0

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

    def get_persona_id(self):
        return f'This persona ID is {self.__internal_id}'

    def set_obtainable(self,status : bool):
        self._obtainable = status
        if status == True:
            return 'This persona is now obtainable'
        elif not status:
            return 'This persona is now not obtainable'
        return None
