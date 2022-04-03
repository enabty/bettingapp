import sheet_funcs

header_dict = sheet_funcs.generate_col_dict()


def fill_cell(row: str, col_name: str, ip_str: str):
    cell = f'{header_dict[col_name]}{row}'

    # Placing date in B col
    if col_name == "Date":
        sheet_funcs.new_cell(cell, ip_str)

    # Placing Match in D col
    elif col_name == "Match":
        sheet_funcs.new_cell(cell, ip_str)

    # Placing Bet in F col
    elif col_name == "Bet":
        sheet_funcs.new_cell(cell, ip_str)

    # Placing type in G col
    elif col_name == "Type":
        sheet_funcs.new_cell(cell, ip_str)

    # Placing Stake in I col
    elif col_name == "Stake":
        sheet_funcs.new_cell(cell, ip_str)

    # Placing Odds in J col
    elif col_name == "Odds":
        sheet_funcs.new_cell(cell, ip_str)

    # Placing current in E col
    elif col_name == "Current":
        sheet_funcs.new_cell(cell, ip_str)

    # Placing Time in H col
    elif col_name == "Time":
        sheet_funcs.new_cell(cell, ip_str)

    else:
        return None


