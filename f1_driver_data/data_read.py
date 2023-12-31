from .Driver import Driver
import csv

def read_all():
    drivers = []
    with open('f1_driver_data/data/F1Drivers_Dataset.csv', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')

        # skip first line with column names
        next(reader, None)

        for l in reader:
            drivers.append(Driver(
                l[0],
                l[1],
                l[2],
                l[3],
                l[4],
                l[5],
                l[6],
                l[7],
                l[8]
            ))
    
    return drivers


if __name__=="__main__":
    for i in read_all():
        print(i)
            

