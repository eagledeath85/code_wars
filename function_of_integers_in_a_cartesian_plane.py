
def sumin(n):
    x_values = [i for i in range(1, n + 1)]
    y_values = [j for j in range(n, 0, -1)]

    table = [[min(x, y) for x in x_values] for y in y_values]

    # for y in y_values:
    #     row = []
    #     for x in x_values:
    #         row.append(min(x, y))
    #     tables.append(row)

    # total_sum = 0
    # for table in tables:
    #     sum_table = 0
    #     for item in table:
    #         sum_table += item
    #     total_sum += sum_table
    total_sum = sum(cell for row in table for cell in row)
    return total_sum


def sumax(n):
    x_values = [i for i in range(1, n + 1)]
    y_values = [j for j in range(n, 0, -1)]

    table = [[max(x, y) for x in x_values] for y in y_values]

    total_sum = 0
    for table in tables:
        sum_table = 0
        for item in table:
            sum_table += item
        total_sum += sum_table
    return total_sum


def sumsum(n):
    x_values = [i for i in range(1, n + 1)]
    y_values = [j for j in range(n, 0, -1)]

    table = [[(x + y) for x in x_values] for y in y_values]

    total_sum = 0
    for table in tables:
        sum_table = 0
        for item in table:
            sum_table += item
        total_sum += sum_table
    total_sum = ((sum(x) for x in x_values) for y in y_values)

    return total_sum


print(sumin(5))
# print(sumax(8))
# print(sumsum(8))
# print(sumin(15))