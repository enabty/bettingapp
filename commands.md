from auth import sh

# Getting a Cell Value
sh.acell('B1').value

sh.cell(1, 2).value

# Getting a formula
worksheet.acell('B1', value_render_option='FORMULA').value

worksheet.cell(1, 2, value_render_option='FORMULA').value

# Getting All Values From a Row or a Column
values_list = worksheet.row_values(1)  # First row

values_list = worksheet.col_values(1)  # First col


# Getting All Values From a Worksheet as a List of Lists
list_of_lists = worksheet.get_all_values()


# Getting All Values From a Worksheet as a List of Dictionaries
list_of_dicts = worksheet.get_all_records()

# Finding a Cell

## Find a cell matching a string:
cell = worksheet.find("Dough")

print("Found something at R%sC%s" % (cell.row, cell.col))

## Find a cell matching a regular expression
amount_re = re.compile(r'(Big|Enormous) dough')

cell = worksheet.find(amount_re)
### find returns None if value is not Found

# Finding All Matched Cells

## Find all cells matching a string:
cell_list = worksheet.findall("Rug store")

## Find all cells matching a regexp:
criteria_re = re.compile(r'(Small|Room-tiering) rug')

cell_list = worksheet.findall(criteria_re)

# Cell Object

## Each cell has a value and coordinates properties:
value = cell.value

row_number = cell.row

column_number = cell.col

# Updating Cells
## Using A1 notation:
worksheet.update('B1', 'Bingo!')

## Or row and column coordinates:
worksheet.update_cell(1, 2, 'Bingo!')

## Update a range
worksheet.update('A1:B2', [[1, 2], [3, 4]])

# Formatting

##Set A1:B1 text format to bold:
worksheet.format('A1:B1', {'textFormat': {'bold': True}})

## Color the background of A2:B2 cell range in black, change horizontal alignment, text color and font size:

worksheet.format("A2:B2", {
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
















