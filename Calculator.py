print("AS Calculator V2.01")

while(True):
    n1 = float(input("Enter your Fist Valu:"))
    op = input("Enter your Operator[+,-,*,/]:")
    n2 = float(input("Enter your Second Valu:"))
    if op=="+":
        print("Your Result=>", n1+n2)
    elif op=="-":
        print("Your Result=>", n1-n2)
    elif op=="*":
        print("Your Result=>", n1*n2)
    elif op=="/":
        print("Your Result=>", n1/n2)
    else:
        print("Note-Wrong Operator,Pls Try Again")
    data1 = str(input("Again Calculatione (y/n):"))
    if data1=="y":
        continue
    elif data1=="n":
        print("Good Bay  [YouTube:-INDIAN TECHNICAL MASTER]")
        break

