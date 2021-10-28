a = []
n = int(input("Enter number of elements:"))
for i in range(n):
    x = input("Enter word:")
    a.append(x)

print("The list of words:",a)
for q in sorted(a) :
    print(q)

