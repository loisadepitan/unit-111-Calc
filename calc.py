# METHOD ON THE TOP
def separator():
    print(40 * '_')

def menu():
        separator()
        print('Welcome to PyCalc')
        separator()
        print('[1] - add')
        print('[2] = Subtraction')
        print('[3]- Multiply')
        print('[4] - Divide')
        print('[x] - Exit')

#instruction on the buttom

opc = ''
while (opc != 'x'):
    menu()
    opc = input('Select an option: ')
    if(opc == 'x'):
        break # break finish with the loop

    num1 = float(input('First Number: '))
    num2 = float(input('Second Number: '))

    if(opc == '1'):
        res = num1 + num2
        print('Addition = ' + str(res))

    elif(opc == '2'):
        res = num1 - num2
        print('Subtraction = ' + str(res))

    elif(opc =='3'):
        res = num1 * num2
        print('Multiplication = ' + str(res))

    elif(opc == '4'):
        if(num2 == 0):
            print('Error: Dividing by 0 is not allowed')
        else:
            res = num1 / num2
            print('Division = ' + str(res))

    input('press Enter to continue...')
print('Thank you!!')

"""
this is a comment
"""


   




    


