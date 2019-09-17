from read_file import read_file
import sorting

printers_list = read_file("printers_list.txt")
sorting.printing_speed_sort(printers_list)
sorting.price_sort(printers_list)
