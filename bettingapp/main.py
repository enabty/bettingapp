import user_inputs
import sheet_funcs
from cell_inserting import fill_cell


def new_bet():
    row = sheet_funcs.get_next_cell_row()  # Get next row

    # Placing date in B col
    fill_cell(row, "Date", "NONE")

    # Placing Match in D col
    fill_cell(row, "Match", user_inputs.match_name())

    # Placing Bet in F col
    fill_cell(row, "Bet", user_inputs.bet())

    # Placing type in G col
    fill_cell(row, "Type", user_inputs.bet_type())

    # Placing Stake in I col
    fill_cell(row, "Stake", user_inputs.stake())

    # Placing Odds in J col
    fill_cell(row, "Odds", user_inputs.odds())

    # Placing current in E col
    fill_cell(row, "Current", user_inputs.current_stats())

    # Placing Time in H col
    fill_cell(row, "Time", user_inputs.bet_time())


if __name__ == '__main__':
    new_bet()