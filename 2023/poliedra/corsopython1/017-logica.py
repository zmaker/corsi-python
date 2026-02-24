A = True
B = False
O = A and B
print(f"{A} and {B} = {O}")

O = A or B
print(f"{A} or {B} = {O}")

C = True
O = (A and B) or (not A and C)
print(f"O = {O}")

A = [0,0,1,1]
B = [0,1,0,1]
print("A B | O")
print("-------")
for i in range(4):
    O = A[i] and B[i]
    print(f"{A[i]} {B[i]} | {O}")
    
print("A B | O")
print("-------")
for i in range(4):
    O = A[i] or B[i]
    print(f"{A[i]} {B[i]} | {O}")
    
A = [0,0,0,0,1,1,1,1]
B = [0,0,1,1,0,0,1,1]
C = [0,1,0,1,0,1,0,1]
print("A B C | O")
print("---------")
for i in range(8):
    O = bool((A[i] and B[i]) or (not A[i] and C[i]))
    print(f"{A[i]} {B[i]} {C[i]} | {O}")

