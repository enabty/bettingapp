from gspread.worksheet import ValueRange

from auth import pd
from auth import gspread
from auth import sh


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


def cell_isempty(cell: str) -> bool:
    return get_cell_val(cell) == "" or get_cell_val(cell) is None


def testing(cell):
    print(cell_isempty(cell))
    print(get_cell_val(cell))


if __name__ == '__main__':
    testing("D17")






