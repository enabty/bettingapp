from auth import sh

# Getting a Cell Value
sh.acell('B1').value

sh.cell(1, 2).value

# Getting a formula
sh.acell('B1', value_render_option='FORMULA').value

sh.cell(1, 2, value_render_option='FORMULA').value

# Getting All Values From a Row or a Column
values_list = sh.row_values(1)  # First row

values_list = sh.col_values(1)  # First col


# Getting All Values From a sh as a List of Lists
list_of_lists = sh.get_all_values()


# Getting All Values From a sh as a List of Dictionaries
list_of_dicts = sh.get_all_records()

# Finding a Cell

## Find a cell matching a string:
cell = sh.find("Dough")

print("Found something at R%sC%s" % (cell.row, cell.col))

## Find a cell matching a regular expression
amount_re = re.compile(r'(Big|Enormous) dough')

cell = sh.find(amount_re)
### find returns None if value is not Found

# Finding All Matched Cells

## Find all cells matching a string:
cell_list = sh.findall("Rug store")

## Find all cells matching a regexp:
criteria_re = re.compile(r'(Small|Room-tiering) rug')

cell_list = sh.findall(criteria_re)

# Cell Object

## Each cell has a value and coordinates properties:
value = cell.value

row_number = cell.row

column_number = cell.col

# Updating Cells
## Using A1 notation:
sh.update('B1', 'Bingo!')

## Or row and column coordinates:
sh.update_cell(1, 2, 'Bingo!')

## Update a range
sh.update('A1:B2', [[1, 2], [3, 4]])

# Formatting

##Set A1:B1 text format to bold:
sh.format('A1:B1', {'textFormat': {'bold': True}})

## Color the background of A2:B2 cell range in black, change horizontal alignment, text color and font size:

sh.format("A2:B2", {
    "backgroundColor": {
      "red": 0.0,
      "green": 0.0,
      "blue": 0.0
    },
    "horizontalAlignment": "CENTER",
    "textFormat": {
      "foregroundColor": {
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
      },
      "fontSize": 12,
      "bold": True
    }
})
















