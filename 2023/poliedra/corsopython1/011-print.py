print("nome", 123, "mela")

print("nome", end="#")
print("mela", end=".")
print("pera", end=".")
print("\n")

for i in range(5):
    if (i < 4):
        print(i, end="-")
    else:
        print(i)

print("\n")

n = "paolo"
i = 23
print(f"mi chiamo {n} ho {(i+1)} euro in tasca")

ll = ["a", "b", "c"]
i = 0
for el in ll:
    print(f"{(i+1)}: {el}")
    i += 1

