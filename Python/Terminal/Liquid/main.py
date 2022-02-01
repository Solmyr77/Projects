import os
import csv


def clear():
    os.system('cls')


def pretty_input_float(input_name):
    while 1:
        try:
            var_to_return = float(input(f'{input_name}'))
            break
        except Exception:
            print('Hibás adat')
    return var_to_return


def pretty_input_str(input_name):
    while 1:
        try:
            var_to_return = str(input(f'{input_name}'))
            break
        except Exception:
            print('Hibás adat')
    return var_to_return


def list_recipes():
    flag = 0
    with open('recipes.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if flag > 0:
                print(f'\n{row[0]}: {row}')
            else:
                print(f'\n{row}\n')
        flag += 1


def persistant():
    mix_name = pretty_input_str('Recept neve: ')
    total_amount = pretty_input_float('Add meg hogy összesen hány ml liquidet szeretnél keverni: ')
    vg_percentage = pretty_input_float('Add meg a VG százalékot: ')
    pg_percentage = pretty_input_float('Add meg a PG százalékot: ')
    flavor_percentage = pretty_input_float('Add meg az aroma százalékot: ')
    flavor_name = pretty_input_str('Aroma neve: ')
    nicotine_amount = pretty_input_float('Add meg hogy hanyas legyen a liquid: ')


    if nicotine_amount > 0:
        nicotine_base = pretty_input_float('Add meg a nikotin booster erősségét: ')
        nicotine_result = round(((nicotine_amount / nicotine_base) * total_amount), 2)
    else:
        nicotine_result = 0


    flavor_ml = round(total_amount * flavor_percentage/100, 2)
    base_total = total_amount - nicotine_result - flavor_ml
    vg_ml = round(base_total * vg_percentage/100, 2)
    pg_ml = round(base_total * pg_percentage/100, 2)
    
    
    pg_gram = round(pg_ml * 1.04, 2)
    vg_gram = round(vg_ml * 1.27, 2)
    total_weight = round(total_amount * 1.155, 2)


    print(f'\nFőzet mérete: {total_amount} ml, kb. {total_weight} g\n--------------------------------')
    print(f'VG: {vg_ml} ml, {vg_gram} g')
    print(f'PG: {pg_ml} ml, {pg_gram} g')


    if nicotine_result > 0:
        print(f'Aroma: {flavor_ml} ml\n--------------------------------')
        print(f'Nikotin booster szükséges mennyisége: {nicotine_result} ml\n--------------------------------\n')
    else:
        print(f'Aroma: {flavor_ml} ml\n--------------------------------\n')

    with open('recipes.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([mix_name, flavor_name, total_amount, vg_ml, pg_ml, nicotine_result])


def starting_point():
    print('Mentés: (1)\nMentett receptek: (2)\n')
    user_input = str(input('Opció: '))
    if user_input == '1':
        persistant()
    elif user_input == '2':
        list_recipes()


def build():
    clear()
    starting_point()


if __name__ == '__main__':
    build()
