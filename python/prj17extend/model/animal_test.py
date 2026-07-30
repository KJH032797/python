from model.animal import Dog, Cat, Sparrow, Squirrel

print("\n===== Test about Animal =====")

a1 = Dog()
a2 = Cat()
a3 = Sparrow()
a4 = Squirrel()

print(f"\n{a1}")
print(a2)
print(a3)
print(f"{a4}\n")

a1.sounds()
a2.sounds()
a3.sounds()
a4.sounds()