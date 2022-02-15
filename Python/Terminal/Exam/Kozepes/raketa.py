user_input_total = int(input('Hány órás visszaszámlálst tervezünk? '))
total_time = user_input_total
steps = 0


while total_time > 0:
    print(f'Visszaszámlálás: {total_time}')
    user_input_suspend = str(input('Fel kell függeszteni a visszaszámlálást? (i/n)? '))
    if user_input_suspend == 'i':
        steps += 1
        continue
    elif user_input_suspend == 'n':
        total_time -= 1
        steps += 1


if total_time == 0:
    print(f'A rakéta a visszaszámlálást követően ennyi órával indult: {steps}')
