from datetime import date


def get_today_date() -> str:
    return date.today().strftime("%d/%m/%Y")


