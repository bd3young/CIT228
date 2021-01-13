print("------------------------------------------")
print("Exercise 1")
name = "beau deyoung"
print(name.title())
print(name.upper())
print(name.lower())
print("My first initial is: ", name[0].upper())

print("------------------------------------------")
print("Exercise 2")
noun = "cat"
adj = "fat"
verb = "sat"
ending = "on the hat"
sentence1 = "the " + adj + " " + noun + " " + verb + " " + ending + "."
sentence2 = f"the {adj} {noun} {verb} {ending}."
print(sentence1.upper())
print(sentence2.lower())