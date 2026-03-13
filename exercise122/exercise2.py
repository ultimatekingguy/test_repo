# from personaMethods import persona
#
# persona1 = persona('Jack Frost','magician',10,3027)
#
# print(persona1.register_persona())
#
# print(persona1.level_up(2))
# print(persona1.level_up(5))
# print(persona1.level_up(1))
#
#
from personaAttrib import persona
persona1 = persona('Jack Frost','magician',10,3027)

# print(persona1._obtainable) # protected warning

print(persona1.get_persona_id())

print(persona1.set_obtainable(True))