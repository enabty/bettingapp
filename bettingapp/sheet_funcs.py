from gspread.worksheet import ValueRange
from auth import sh
import string


def clear_cell(cell: str):
    sh.update(cell, "")
    print(f"Cleared cell [{cell}]")


def get_cell_lst(cell: str) -> ValueRange:
    return sh.get(cell)


def get_cell_val(cell: str) -> str:
    return sh.acell(cell).value


def get_cell_formula(cell: str) -> str:
    return sh.acell(cell, value_render_option='FORMULA').value


def get_col_val(col: int) -> list:
    return sh.col_values(col)


def get_row_val(row: int) -> list:
    return sh.row_values(row)


def update_cell(cell: str, new_string: str):
    """Updates a cell with a new value. Ex: update_cell('A1', 'foo') """
    old_val = get_cell_val(cell)
    sh.update(cell, new_string)
    print(f'Updated cell [{cell}] from "{old_val}" --> "{new_string}"')


def new_cell(cell: str, new_string: str):
    """Creates a new cell with a value. Ex: new_cell('A1', 'foo') """
    sh.update(cell, new_string)
    print(f'"{new_string} --> {cell}"')


def cell_isempty(cell: str) -> bool:
    return get_cell_val(cell) == "" or get_cell_val(cell) is None


def get_next_cell_row() -> str:
    return str(len(get_col_val(2)) + 1)


def generate_col_dict() -> dict:
    alphabet_list = list(string.ascii_uppercase)
    col_lst = get_row_val(1)
    header_dict = {}

    for i, header in enumerate(col_lst):
        header_dict[header] = alphabet_list[i]

    return header_dict


if __name__ == '__main__':
    print(generate_col_dict())







