def main():
    answer = input('What is the time now? ')
    time = convert(answer)
    if 7 <= time <=8:
        print('Breakfast')
    if 12 <= time <= 13:
        print('Lunch')
    if 18 <= time <= 19:
        print('Dinner')


def convert(time):
    hours, minutes = time.split(':')
    minutes = float(minutes) / 60
    return float(hours)+minutes

if __name__ == "__main__":
    main()