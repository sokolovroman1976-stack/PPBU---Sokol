import random
p = ["умный", "добрый", "талантливый", "замечательный"]
s = ["человек","друг","профессионал","гений"]
def dobrie_slova():
    adj = random.choice(p)
    noun = random.choice(s)
    return f"Ты {adj} {noun}!"
print(dobrie_slova())
print(dobrie_slova())
print(dobrie_slova())
print(dobrie_slova())



