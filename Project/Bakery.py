def Bakery():

     print('Toast(1)  Baguette(2)  Lavash(3)')
     def Toast():
          Price = 4000
          int(Price)
          Num_Bread = 0
          int(Num_Bread)
          print('Hello!')
          Num_Bread = int(input('    Number of bread: '))
          Payment = Price * Num_Bread
          print('    Payment: ', Payment)
          print('Loading Cart...')
          for c in range(2):
               Pass_Cart = input('    Password: ')
               if Pass_Cart =='1382':
                    print('Successful transaction ')
                    break
               else:
                    print('The password is incorrect ')
          print('Bay')

     def Baguette():
          Price = 5000
          int(Price)
          Num_Bread = 0
          int(Num_Bread)
          print('Hello!')
          Num_Bread = int(input('    Number of bread: '))
          Payment = Price * Num_Bread
          print('    Payment: ', Payment)
          print('Loading Cart...')
          for c in range(2):
               Pass_Cart = input('    Password: ')
               if Pass_Cart == '1382':
                    print('Successful transaction ')
                    break
               else:
                    print('The password is incorrect ')
          print('Bay')

     def Lavash():
          Price = 1500
          int(Price)
          Num_Bread = 0
          int(Num_Bread)
          print('Hello!')
          Num_Bread =int(input('    Number of bread: '))
          Payment = Price * Num_Bread
          print('    Payment: ', Payment)
          print('Loading Cart...')
          for c in range(2):
               Pass_Cart = input('    Password: ')
               if Pass_Cart == '1382':
                    print('Successful transaction ')
                    break
               else:
                    print('The password is incorrect ')
          print('Bay')

     nameN='Toast','Baguette','Lavash','Exit'
     while True:
          nameN = input('Enter the desired Bread: ')
          if nameN == '1':
               Toast()
          elif nameN == '2':
               Baguette()
          elif nameN == '3':
               Lavash()
          elif nameN == 'Exit':
               break
          else:
               print('Toast(1)  Baguette(2)  Lavash(3)')

Bakery()