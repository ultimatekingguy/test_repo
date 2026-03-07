from persona2 import persona
''''Persona 3 Reload Stats. Use the site below for reference
# https://aqiu384.github.io/megaten-fusion-tool/p3r/personas'''

coolGuy = persona('Jack Frost', 'magician',8,3024,True)
print(dir(coolGuy))

number = int(input("How many personas are you entering in the Compendium? "))
persona_compendium = []

for sona in range(number):
    name = input('Enter the name of the Persona: ')
    arcana = input("Enter the persona's arcana: ")
    baseLVL = int(input("Enter the persona's base level: "))
    price = int(input("Enter the Persona's price in the Compendium: "))

    new_entry = persona(name,arcana,baseLVL,price)
    persona_compendium.append(new_entry)

print(persona_compendium)



print(persona_compendium[0].name)

if persona_compendium[0]['baseLVL'] > 30: # I dont know why, but this keeps erroring out for me, even though its close to what we did in class
    print("This persona is too powerful for you to handle")
else:
    print("The persona is within your power")