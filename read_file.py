from printer import Printer


def read_file(printers):
    with open(printers) as file:
        printers_list = []
        for row in file:
            row = row.split(",")
            printers_list.append(Printer(row[0], row[1], row[2]))
        return printers_list
