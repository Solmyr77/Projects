def main(numbers=[]):
    while 1:
        try:
            array_size = int(input('Hány számot szeretne megadni? '))
            break
        except Exception:
            print('Hibás adat!')

    for _ in range(array_size):
        while 1:
            try:
                numbers.append(int(input('Adjon meg egy egész számot: ')))
                break
            except Exception:
                print('Hibás adat!')
    
    while 1:
        try:
            number = int(input('Melyik számot keressük?: '))
            break
        except Exception:
            print('Hibás adat!')
    print(f'A "{number}" szám {numbers.count(number)}-szer(szor) szerepel a listában.')


if __name__ == "__main__":
    main()
