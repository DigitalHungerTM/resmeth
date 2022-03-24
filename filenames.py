# this program generates a list of filenames, it generates 24 filenames for 12 random days in the year 2021
# the output is saved to filenames.txt
import random


def format_numbers(number):
    """this function converts a number to a string and prefixes a 0 if needed"""
    string = str(number)
    if len(string) == 1:
        string = "0" + string
    return string


def gen_filenames_less():
    days = random.sample(range(1, 32), 12)
    hours = [str(i) for i in range(24)]

    print(days, hours)
    # print([i + 1 for i in range(31)])

    days = [format_numbers(day) for day in days]
    hours = [format_numbers(hour) for hour in hours]

    filenames = []
    for i in range(len(days)):
        for hour in hours:
            filenames.append("/net/corpora/twitter2/Tweets/2021/" + format_numbers(i + 1) + "/2021" + format_numbers(i + 1) + days[i] + ":" + hour + ".out.gz")

    print(filenames)
    print(len(filenames))

    with open("filenames.txt", 'w') as f:
        for filename in filenames:
            print(filename, file=f)


def main():
    gen_filenames_less()


if __name__ == "__main__":
    main()
