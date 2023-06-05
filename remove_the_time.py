
def shorten_to_date(long_date):
    return long_date.split(",")[0]


date_to_shorten = "Monday February 2, 8pm"
shorten_to_date(date_to_shorten)
