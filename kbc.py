questions = [
    ["Q1","OP1","OP2","OP3","OP4",1],
    ["Q2","OP1","OP2","OP3","OP4",2],
    ["Q3","OP1","OP2","OP3","OP4",3],
    ["Q4","OP1","OP2","OP3","OP4",2],
    ["Q5","OP1","OP2","OP3","OP4",4]
]

prices = [10,100,1000,10000,100000]
i = 0
print("Welcome to Kab banega karore pati?")
print("Let's play the game!")
print(f"First Question on your screen for {prices[i]} rupees.\n\n")

for question in questions:
    
    print(f"Question : {question[0]}")
    print(f"Option 1: {question[1]}")
    print(f"Option 2: {question[2]}")
    print(f"Option 3: {question[3]}")
    print(f"Option 4: {question[4]}")
    
    answer = int(input("Enter Answer : "))
    if (question[5] == answer):
        print("This is right answer.")
    else:
        print("Opps, Your answer is wrong!")
        break
    
    print(f"You won {prices[i]} rupees.\n\n")
    i+=1 
    if (len(prices) < i):
        print(f"Next question in your screen for {prices[i]} rupees.")
    
