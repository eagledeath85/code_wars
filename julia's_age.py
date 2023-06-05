def age_of_julia(x_old: float, y_times: float) -> int:
    return round((-(x_old/(1-y_times))) + x_old)



print(age_of_julia(6, 3))