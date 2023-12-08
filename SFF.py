print("Smallest Factor Finder!")
while True:
    n = int(input("Enter Integer >=2: "))
    if n >= 2:
        factor = 0
        
        for i in range(2, n+1):
            if n % i == 0:
                factor = i
                print(f"The Smallest factor of {n} other than 1 is {factor}")
                break
            
        
            

        choice = input("Continue? [Y/N]: ")
        while choice.lower() not in ['y', 'n']:
            print("Invalid Input. Enter Y or N only")
            choice = input("Continue? [Y/N]: ")
        
        if choice.lower() == 'n':
            print("Thank you for using SFF <3")
            break
    else:
        print("Invalid Number. Enter a number greater than 2.")