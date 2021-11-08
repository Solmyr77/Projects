class Nyitvatartas():

    def __init__(self,time):
        self.time = 0

    def bolt():

        while True:

            time = int(input('Hány óra van?: '))

            if 10 <= time <= 16:
                print('A bolt nyitva van.')
                break

            if time >= 25:
                print('Érvénytelen idő.')

            elif time < 10:
                print(str(10-time) + ' Óra múlva lesz nyitva.')
                break

            elif time > 16:
                print(str(time-16) + ' Órával ezelőtt bezárt.')
                print(str(24-time+10) + ' Óra múlva nyit.')
                break

if __name__ == "__main__":
    Nyitvatartas.bolt()
