S = input()

c = False
for i in range(3):
    if (S[i] == S[i + 1]):
        c = True
        break
if (c):
    print("Bad")
else:
    print("Good")
