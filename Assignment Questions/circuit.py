a = bool(int(input("A")))
b = bool(int(input("B")))
c = bool(int(input("C")))

ab = bool(0)
ac = bool(0)

# compute d
if (a and not b == bool(1)):
    ab == bool(1)

if (not a and c == bool(1)):
    ac == bool(1)

if ab or ac == bool(1):
    d = 1
else:
    d = 0

print("D is", d)