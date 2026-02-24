A = True
B = False
O = A and B
print(f"{A} and {B} = {O}")

A = [0,0,1,1]
B = [0,1,0,1]
print("OR TABLE")
print("A B | O")
print("-------")
for i in range(4):
    O = A[i] or B[i]
    print(f"{A[i]} {B[i]} | {O}")
    
print("\nAND TABLE")
print("A B | O")
print("-------")
for i in range(4):
    O = A[i] and B[i]
    print(f"{A[i]} {B[i]} | {O}")

A = [0,0,0,0,1,1,1,1]
B = [0,0,1,1,0,0,1,1]
C = [0,1,0,1,0,1,0,1]
print("\nLOGIC TABLE")
print("A B C | O")
print("---------")
for i in range(len(A)):
    O = bool((A[i] and B[i]) or (not C[i] or B[i]))
    print(f"{A[i]} {B[i]} {C[i]} | {O}")

    