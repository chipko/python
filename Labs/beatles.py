beatles = []
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range(1):
    beatles.append(input("Enter another beatle: "))
    beatles.append(input("Enter another beatle: "))
print("Step 3:", beatles)

del beatles[len(beatles)-1]
del beatles[len(beatles)-1]
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

