import dict as di
from random import randint
from pytransform import pyarmor_runtime

pyarmor_runtime()

i = 1

generated_list = []
second_generated_list = []

length = (int(input('Adja meg a jelszo hosszat: ')))


while i != length:

    letter_x_gen_index = randint(0, 25)
    symbol_y_gen_index = randint(0, 24)
    letter_z_gen_index = randint(0, 25)

    generated_x_letter = di.lowercase_letter_list[letter_x_gen_index]
    generated_y_symbol = di.symbol_list[symbol_y_gen_index]
    generated_z_letter = di.uppercase_letter_list[letter_z_gen_index]

    generated_list.extend(generated_x_letter)
    generated_list.extend(generated_y_symbol)
    generated_list.extend(generated_z_letter)

    i += 1


print('A jelszo:')
print("".join(generated_list[:length]))
