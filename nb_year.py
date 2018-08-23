def nb_year(p0, percent, aug, p):
    # your code
    current_pop = p0
    year_count = 0
    while current_pop <= p:
        current_pop = current_pop + (current_pop * (percent / 100.0)) + aug
        year_count += 1
    return year_count

nb_year(1500, 5, 100, 5000)
nb_year(1500000, 2.5, 10000, 2000000)
nb_year(1500000, 0.25, 1000, 2000000)
