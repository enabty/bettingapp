no_match = "No match, try again!"


def match_name() -> str:
    return input("Enter match name: ")


def current_stats() -> str:
    return input("Enter current stats: ")


def over_under() -> str:
    print("Enter (Ö) as ö")
    print("Enter (U) as u")
    answer = input()
    if answer.upper() in "Ö":
        return "Ö"
    elif answer.upper() in "U":
        return "U"
    else:
        print(no_match)
        over_under()


def ht_ft() -> str:
    print("Enter (HT) as ht")
    print("Enter (FT) as ft")
    answer = input()
    if answer.upper() in "HT":
        return "HT"
    elif answer.upper() in "FT":
        return "FT"
    else:
        print(no_match)
        ht_ft()


def bet() -> str:
    over_under_var = over_under()
    num = input(f"{over_under_var} how much: ")
    ht_ft_var = ht_ft()

    return f"{over_under_var}{num} {ht_ft_var}"


def bet_type() -> str:
    print("Enter Goal (G) as g")
    print("Enter Corner (C) as c")
    answer = input()
    if answer.upper() in ["G", "GOAL"]:
        return "G"
    elif answer.upper() in ["C", "CORNER"]:
        return "C"
    else:
        print("No match, try again!")
        bet_type()


def bet_time() -> str:
    return input("Enter time when bet was places: ")


def stake() -> str:
    return input("Enter amount staked: ")


def odds() -> str:
    return input("Enter odds: ")


