# this program generates date values to be used with counter.sh

import sys


def main():

    with open("filename.txt", "w") as filenames:

        date = sys.argv[1]
        dates = []
        for year in range(2011, 2022):
            year = str(year)
            
            # for hour in range(24):
            #     hour = str(hour)
            #     if len(hour) != 2:
            #         hour = "0" + hour
            #     hour_date = hour + "/" + date + "/" + year
            #     dates.append(hour_date)

            hour = "00"
            hour_date = hour + "/" + date + "/" + year
            dates.append(hour_date)

        for date in dates:
            print(date, file=filenames)

if __name__ == "__main__":
    main()
