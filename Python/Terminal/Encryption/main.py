import string


alphabet = string.ascii_lowercase
numbers = string.digits
passw = 'asdasd123'


def encrypt(passw):
    for index, data in enumerate(passw):

        try:
            data/1
            offset_digit_index = (numbers.find(data))-3
            print(numbers[offset_digit_index])
        except:
            offset_index = (alphabet.find(data))-3
            print(alphabet[offset_index])

encrypt('asdasd22')

def decrypt(passw):
    raise NotImplementedError
