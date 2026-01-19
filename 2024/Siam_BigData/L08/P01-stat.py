import statistics as s

voti = [4,7,8,6,9,5,7,8,6,6]

somma = 0
for n in voti:
    somma += n
media = somma / len(voti)

print(somma, media)

print("media:", s.mean(voti))
print("min: ", min(voti))
print("max: ", max(voti))
print("mediana: ", s.median(voti))
print("moda: ", s.mode(voti))
print("varianza: ", s.variance(voti))
print("dev standard: ", s.stdev(voti))

voti = [2,2,2,2,2,2,2,2,2,2]
print("\n")
print("media:", s.mean(voti))
print("min: ", min(voti))
print("max: ", max(voti))
print("mediana: ", s.median(voti))
print("moda: ", s.mode(voti))
print("varianza: ", s.variance(voti))
print("dev standard: ", s.stdev(voti))

voti = [2,2,3,3,4,3,3,2,2,2]
print("\n")
print("media:", s.mean(voti))
print("min: ", min(voti))
print("max: ", max(voti))
print("mediana: ", s.median(voti))
print("moda: ", s.mode(voti))
print("varianza: ", s.variance(voti))
print("dev standard: ", s.stdev(voti))





