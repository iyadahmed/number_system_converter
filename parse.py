from convert import Base_N_Number, Base_10_Number


def parse_base_n_string(string: str, base: int):
    decimal_point_index = string.find(".")
    if decimal_point_index == -1:
        integer_part_s = string
        fractional_part_s = ""
    else:
        integer_part_s = string[:decimal_point_index]
        fractional_part_s = string[decimal_point_index + 1 :]

    i = []
    for c in integer_part_s:
        i.append(int(c, base=base))

    f = []
    for c in fractional_part_s:
        f.append(int(c, base=base))

    return Base_N_Number(base, i, f)


def parse_base_10_string(string: str):
    n = float(string)
    i = int(n // 1)
    f = n - i
    return Base_10_Number(i, f)
