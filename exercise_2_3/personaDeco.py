"""
2.3 Class Methods and Property Decorators

Use vehicle5.py and dealership.py as a model to cmplete this

Goal: Modify the existing class from the previous exercise to include a class attribute/method and a property decorator

STEP-BY-STEP:
    STEP 1 - Add a property decorator
        Choose one attribute, it could be the one you wrote a getter/setter method for previously or another one.
        Write a property decorator for it that allows you to return its value
            See the @property in vehicle5.py for an example

    STEP 2 - Add a setter decorator
        Use property decorator you wrote in STEP 1 to to create a setter decorator.
        The decorator should accept at least one parameter similar to the setter method you wrote previously.
        The decorator should validate some data or condition then set a new value or reject the request with a message.
        See the  @price.setter decorator in vehicle5.py for an example

    STEP 3 - Demonstrate the use of your decorators.
        Create an instance from your class.
        Use the property decorator to display an attribute.
            For example we used car1.price in vehicle5.py

        Use the setter decorator to:
            1) Set a value that will be accepted and set,
                For example, we used car1.price = 35000 in vehicle5.py
            2) Set another value that will be rejected

    STEP 4 - Create a class attribute
        Create an attribute that will be applied to every instance created from the class. It DOES NOT have to be private or protected.
            For example we used __CAR_COUNT = 0 in vehicle5.py

    STEP 5 - Create a class method
        Create a class method decorator that will apply to every instance from a class in the same way.
        Call the class method from your constructor (__init__) when the object is created
            For example, we created:
                    @classmethod
                    def increase_car_count(cls)
                Then called it using: Car.increase_car_count()

    STEP 6 - Demonstrate that your class attribute works by calling it from your main code
        For example, we used:
            print(Car._Car__CAR_COUNT)
        ...to show that the car count goes up after every car instance is created
"""
class persona:
    PERSONA_COUNT = 0
    @classmethod
    def increase_count(cls):
        cls.PERSONA_COUNT +=1

    @classmethod
    def get_persona_count(cls):
        return cls.PERSONA_COUNT
    def __init__(self,name,arcana,baseLVL,compendium_price,registered = False):
        persona.increase_count()
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

    @property
    def level_up(self):
        return f'{self.name} is currently level {self.current_lvl}'

    @level_up.setter
    def level_up(self,lvl):
        new_lvl = self.current_lvl + lvl
        if new_lvl > self.current_lvl:
            self.current_lvl += lvl
            print(f"{self.name} is now level {self.current_lvl}")
        else:
            print( "You cannot regress a persona!")
        # self.current_lvl += lvl
        # return f"{self.name} has leveled up! Their current level is now {self.current_lvl}"

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
