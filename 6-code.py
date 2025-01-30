while True:
    name=input("Enter customers name:")
    total=0
    quantity=0
    while True:
        print("Enter the amount and quantity")
        amount=float (input("Enter amount:"))
        total+=amount*quantity
        repeat=input("do go want to add more items?(yes/no)")
        if repeat=="no" or repeat=="No":
            break
        print("--" *40)
        print("Name:",name)
        print("Amount to be paid:",total)
        print("--" *40)
        print("HAPPY SHOPPING")
    repeat1=input("do you want to go to next customer?(yes/no):")
    if repeat1=="no" or repeat=="No":
        break