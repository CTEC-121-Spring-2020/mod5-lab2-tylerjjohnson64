def codeing(age):
    if 0<=age<=1:
        return "I" 
    elif 1<age<13:
         print("C")
    elif 13<=age<18:
        print("T") 
    elif 18<=age<120:
        print("A")  
    else:
        print("U")

def main():
    print(codeing)    

main()

if  __name__ == "__main__":
   codeing(0)
   codeing(1)
   codeing(10)
   codeing(13)
   codeing(18)
   codeing(121) 