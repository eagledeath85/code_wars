import locale


def format_money(amount: float) -> str:
    locale.setlocale(locale.LC_ALL, 'English_United States.1252')
    return locale.currency(amount, grouping=True)


print(format_money(3.1))