from auth import pd
from auth import gspread
from auth import sh


def clean_cell(cell: str):
    sh.update(cell, "")
    print(f"cleaned cell: {cell}")


def get_cell_lst(cell: str) -> str:
    return sh.get(cell)


def get_cell_val(cell: str) -> str:
    return sh.acell(cell).value


if __name__ == '__main__':
    print(get_cell_lst("E6"))
    print(get_cell_val("E6"))




