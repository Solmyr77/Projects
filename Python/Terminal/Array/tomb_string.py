def main(students=[]):
    user_input = int(input('Hány tanuló jár az osztályba?: '))

    for _ in range(user_input):
        students.append(str(input('Diák keresztneve: ')))

    student = str(input('Melyik keresztnevet keressük: '))

    print(f'{students.count(student)} {student} keresztnevévvel rendelkező diák jár az osztályba.')


if __name__ == "__main__":
    main()