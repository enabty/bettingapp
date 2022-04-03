from gspread.worksheet import ValueRange

from auth import pd
from auth import gspread
from auth import sh


def clean_cell(cell: str):
    sh.update(cell, "")
    print(f"cleaned cell: {cell}")


def get_cell_lst(cell: str) -> ValueRange:
    return sh.get(cell)


def get_cell_val(cell: str) -> str:
    return sh.acell(cell).value


def get_cell_format(cell: str) -> str:
    return sh.acell(cell, value_render_option='FORMULA').value


def get_col_val(col: int) -> list:
    return sh.col_values(col)


def get_row_val(row: int) -> list:
    return sh.row_values(row)


if __name__ == '__main__':
    print(get_row_val(14))



