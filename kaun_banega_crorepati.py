questions = [
    ["who is president of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "pratibha patil", "None", 3],
    ["who is prime minister of india?" , "apj kalam", "narendra modi", "dropadi murmu", "pratibha patil", "None", 2],
    ["who is missile man of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "pratibha patil", "None", 1],
    ["who is first president of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "rajendra prasad", "None", 4],
    ["who is first prime minister of india?" , "apj kalam", "pranab mukharji", "jawaharlal nehru", "pratibha patil", "None", 3],
    ["who is president of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "pratibha patil", "None", 3],
    ["who is prime minister of india?" , "apj kalam", "narendra modi", "dropadi murmu", "pratibha patil", "None", 2],
    ["who is missile man of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "pratibha patil", "None", 1],
    ["who is first president of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "rajendra prasad", "None", 4],
    ["who is first prime minister of india?" , "apj kalam", "pranab mukharji", "jawaharlal nehru", "pratibha patil", "None", 3],
    ["who is president of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "pratibha patil", "None", 3],
    ["who is prime minister of india?" , "apj kalam", "narendra modi", "dropadi murmu", "pratibha patil", "None", 2],
    ["who is missile man of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "pratibha patil", "None", 1],
    ["who is first president of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "rajendra prasad", "None", 4],
    ["who is first prime minister of india?" , "apj kalam", "pranab mukharji", "jawaharlal nehru", "pratibha patil", "None", 3],
    ["who is missile man of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "pratibha patil", "None", 1],
    ["who is first president of india?" , "apj kalam", "pranab mukharji", "dropadi murmu", "rajendra prasad", "None", 4],
    
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000, 75000000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"{i+1}",question[0])
    print(f"a. {question[1]}         b. {question[2]}")
    print(f"c. {question[3]}         d. {question[4]}")
    
    reply = int(input("Enter the answer(1-4) or press 0 for quit : "))
    if(reply == 0):
        money = levels[i-1]    
        break
    if(reply == question[-1]):
        print(f"Correct answer! you are won Rs. {levels[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break 
    
print(f"Your take home money is {money}")    