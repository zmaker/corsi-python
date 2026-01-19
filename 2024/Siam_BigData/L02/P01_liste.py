#reference: https://docs.python.org/3/tutorial/datastructures.html

numeri = [12,23,34,45,56,67]

print(numeri)

print(numeri[0])
print(numeri[1])

numeri[0] = 99
print(numeri)

n = len(numeri)
print("elementi di numeri: ", n)

amici = []
print(amici)
amici.append("Mario")
amici.append("Luigi")
print(amici)
amici.insert(1, "Anna")
print(amici)

amici.extend(["Alberto", "Vincenzo"])
print(amici)

amici.remove("Luigi")
print(amici)

amici.pop()
print(amici)

amici.pop(1)
print(amici)


