n = 1
for i in range(1, 3):
    print(40*"__", end="\n\n")
    for k in range(1, 11):
        print("| ",n, "*", k, "=", n*k, "\t| ", n+1, "*", k, "=", (n+1)*k, "\t| ", n+2, "*", k, "=", (n+2)*k, "\t| ", n+3, "*", k, "=", (n+3)*k, "\t| ", n+4, "*", k, "=", (n+4)*k, "\t| ")
    n += 5
print()
print(40*"__", end="\n\n")