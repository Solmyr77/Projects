user_input_a = int(input('Adj meg egy számot! '))
user_input_b = int(input('Adj meg egy másik számot! '))


if user_input_a > user_input_b:
    print(f'A nagyobb érték: {user_input_a}')
elif user_input_a < user_input_b:
    print(f'A nagyobb érték: {user_input_b}')
elif user_input_a == user_input_b:
    print('A két szám egyenlő')
