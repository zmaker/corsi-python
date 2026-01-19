nome = input("Come ti chiami? ")
ans = input("anno nascita? ")
anno = int(ans)
eta = 2024 - anno

#print("ciao, ", nome)
#print("eta: ", eta)

print(f"Ciao, {nome} hai {eta}", end="")
print(f"perché sei nato nel {anno}")
