names=[]

for _ in range(3):
    names.append(input(" what's your name ?"))

print(sorted(names))

for name in sorted(names):
    print(f"Hello {name}") 