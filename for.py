import os

files = ["a.jpb", "b.png"]

for i, file in enumerate(files):
    print(f"{i+1}. File name = {os.rename(file)}")

# For else
for j in range(10):
    if j % 5 == 0:
        print("Divisible")
        break
else:
    print("Not Found")
