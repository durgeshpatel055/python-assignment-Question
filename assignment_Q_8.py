n=int(input("Enter number of testcases: "))  #n<=30
for i in range(1,n+1):
    a= int(input("")) #0<=a<=20 
    b= int(input("")) #0<=b<=10^10
    # for j in range(1,n+1):
    potency=a**b
    last_digit=potency%10
    print("lastdigit",last_digit)
