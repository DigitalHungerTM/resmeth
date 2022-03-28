import sys


def open_file(filename):
    with open(filename, "r") as inp:
        data = inp.read()
        data = data.strip()  # strip trailing and leading spaces to prevent errors

    return data


def split_to_chunks(data):
    chunks = data.split("\n\n")
    return chunks


def split_into_values(chunk):
    values = chunk.split("\n")
    values[0] = values[0].split("/")[0]
    values[1] = int(values[1].split(" ")[0])
    values[2] = int(values[2].split(" ")[0])
    return values


def main():
    data = open_file(sys.argv[1])
    chunks = split_to_chunks(data)
    value_list_list = [split_into_values(chunk) for chunk in chunks]
    print(value_list_list)

    for i in range(24):
        i = str(i)
        if len(i) != 2:
            i = "0" + i

        total_tweets = 0
        laughter_tweets = 0
        for value_list in value_list_list:
            if value_list[0] == i:
                total_tweets += value_list[2]
                laughter_tweets += value_list[1]

        print(f"hour {i}")
        # print(f"total:    {total_tweets}")
        # print(f"laughter: {laughter_tweets}")
        print(f"ratio:    {laughter_tweets/total_tweets*100:.2f}%")
        print()


if __name__ == "__main__":
    main()
