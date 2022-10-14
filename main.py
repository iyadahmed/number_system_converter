from convert import to_base_10, from_base_10
from parse import parse_base_n_string

if __name__ == "__main__":
    source_base = int(input("Enter source base: "))
    target_base = int(input("Enter target base: "))

    number = parse_base_n_string(input("Enter source number: "), source_base)
    print("\nResults\n")
    print(number)
    base_10 = to_base_10(number)

    target_number = from_base_10(base_10, target_base, 4)
    print(target_number)
