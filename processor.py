import sys
import matplotlib.pyplot as plt


def arg_check(argv):
    usage = f"Usage: python3 {argv[0]} filenames.txt pure|extended|plot"
    if len(argv) != 3:
        print("Error, there are too few/many arguments")
        print(usage)
        exit(-1)
    elif argv[2] != "pure" and argv[2] != "extended" and argv[2] != "plot":
        print("Error: second argument should either be 'pure', 'extended' or 'plot'")
        exit(-1)


def open_filenames(filename):
    with open(filename) as filenames_input:
        filenames = filenames_input.readlines()

    filenames = ["data/" + filename.strip() for filename in filenames]
    return filenames


def split_to_chunks(data):
    """takes a string of data seperated by double newlines and splits it into chunks of data,
       returns a list of strings"""
    chunks = data.split("\n\n")
    return chunks


def open_files(filenames):
    """takes a list of filenames and returns a list of chunks"""
    chunks = []
    for file in filenames:
        with open(file, "r") as inp:
            data = inp.read().strip()

        for chunk in split_to_chunks(data):
            chunks.append(chunk)
        # chunks = [chunk for chunk in split_to_chunks(data)]
    return chunks


def split_into_values(chunk):
    values = chunk.split("\n")
    values[0] = values[0].split("/")[0]
    values[1] = int(values[1].split(" ")[0])
    values[2] = int(values[2].split(" ")[0])
    return values


def combine_values(value_list_list):
    combined_list = []
    for hour in range(24):
        hour = str(hour)
        if len(hour) != 2:
            hour = "0" + hour

        hour_total_tweets = 0
        hour_laughter_tweets = 0
        for value_list in value_list_list:
            if value_list[0] == hour:
                hour_laughter_tweets += value_list[1]
                hour_total_tweets += value_list[2]

        combined_list.append([hour, hour_laughter_tweets, hour_total_tweets])

    return combined_list


def print_pure(combined_list):
    """sums up the values that have the same hour"""
    print("hour,laughter,total,ratio,percentage")
    for value_list in combined_list:
        hour = value_list[0]
        laughter = value_list[1]
        total = value_list[2]
        if total == 0:
            total += 1
        ratio = laughter/total
        percentage = laughter/total*100
        if total == 1:
            total -= 1
        print(f"{hour},{laughter},{total},{ratio:.4f},{percentage:.2f}")


def print_extended(combined_values):
    """prints a pretty summary of the collected data"""
    for value_list in combined_values:
        hour = value_list[0]
        laughter = value_list[1]
        total = value_list[2]
        if total == 0:
            total += 1  # to prevent ZeroDivisionError
        ratio = laughter/total
        percentage = laughter/total*100
        if total == 1:
            total -= 1
        print(f"hour:          {hour}")
        print(f"laughter:      {laughter}")
        print(f"total:         {total}")
        print(f"ratio:         {ratio:.4f}")
        print(f"percentage:    {percentage:.2f}%")
        print()


def plot(combined_list):
    hour_list = [value_list[0] for value_list in combined_list]
    laughter_list = [value_list[1] for value_list in combined_list]
    total_list = [value_list[2] for value_list in combined_list]
    ratio_list = [laughter_list[i]/total_list[i] for i in range(len(laughter_list))]
    percentage_list = [laughter_list[i]/total_list[i]*100 for i in range(len(laughter_list))]
    plt.plot(hour_list, ratio_list)
    plt.xlabel('hour')
    plt.ylabel('ratio')
    plt.title('Ratio of tweets with laughter vs total tweets plotted against time')
    plt.show()


def print_results(combined_list, mode):
    if mode == "pure":
        print_pure(combined_list)
    elif mode == "extended":
        print_extended(combined_list)
    elif mode == "plot":
        plot(combined_list)
    else:
        print("Something went wrong...")
        exit(-1)


def main():
    arg_check(sys.argv)

    filenames = open_filenames(sys.argv[1])

    chunks = open_files(filenames)

    value_list_list = [split_into_values(chunk) for chunk in chunks]

    combined_values = combine_values(value_list_list)

    print_results(combined_values, sys.argv[2])


if __name__ == "__main__":
    main()
