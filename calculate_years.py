def calculate_years(principal, interest, tax, desired):
    if desired == principal:
        return 0
    current = principal
    count = 0
    while current < desired:
        count += 1
        current += ((current * interest) - ((current * interest) * tax))
    return count

calculate_years(1000, 0.05, 0.18, 1100)
