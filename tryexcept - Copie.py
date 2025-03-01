try:
    n = int(input("Donnez un nombre : "))  
    def factorie(n): 
        s = 1  
        if n==0:
            s=1
        else:
            for i in range(1, n + 1):  
                s = s * i  
        return s  

    print(f'Le factorielle est {factorie(n)}') 
except ValueError:  
    print("Veuillez entrer un entier valide.")