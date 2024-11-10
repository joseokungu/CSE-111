"""
Program: Receipt
Author: Jose Okitandende
Purpose: Writing functions to print a customers receipt
Date: 01/11/2024
"""
import csv
from itertools import product
from datetime import datetime

PRODUCT_NUM = 0
QUANTITY = 1
NAME = 1
PRICE = 2

def main():
    try:
        date_time = datetime.now()
        
        products_dict = read_dict("products.csv", 0)
        print(f"Inkom Emporium \n")
        total = 0
        subtotal=0
        sales=0
        final=0
        with open ("request.csv", mode = "r" ) as read_obj:
            reader = csv.reader(read_obj)
            header = next(reader)
            print(f"Requested Items:")

            if header != None:
                for row in reader:
                    quantity = row[QUANTITY]
                    key = row[PRODUCT_NUM]
                    total += int(quantity)
                    value = products_dict[key]
                    price = value[2]
                    name = value[1]
                    subtotal += float(price)*int(quantity)
                    sales=subtotal*0.06
                    final = subtotal+sales
                    print(f"{name}: {quantity} @ ${price}")

            print(f"\nNumber of Items: {total}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: ${sales:.2f}")
            print(f"Total: ${final:.2f}")
            print(f"\nThank you for shopping at the Inkom Emporium.")
            print(f"{date_time:%A %B %d, %H:%M:%S %Y}")
    except FileNotFoundError as file_error:
        print(f"Error: missing file")
        print(f"{file_error}")
    except (KeyError) as key_error:
        print(f"Error: unknown Product ID in the request.csv file\n{key_error}")
    except (PermissionError) as permission_error:
        print(permission_error)


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:

            key = row_list[key_column_index]
            dictionary[key] = row_list

    return dictionary


if __name__ == "__main__":
    main()