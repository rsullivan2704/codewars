
def format_duration(seconds):
    if seconds == 0:
        return 'now'
    secspermin = 60
    secsperhour = secspermin * 60
    secsperday = secsperhour * 24
    secsperyear = secsperday * 365
    remainingsecs = seconds
    years = seconds // secsperyear
    remainingsecs %= secsperyear
    days = remainingsecs // secsperday
    remainingsecs %= secsperday
    hours = remainingsecs // secsperhour
    remainingsecs %= secsperhour
    minutes = remainingsecs // secspermin
    remainingsecs %= secspermin
    resultformat = '{0} {1}'
    yearname = 'years' if years > 1 else 'year'
    dayname = 'days' if days > 1 else 'day'
    hourname = 'hours' if hours > 1 else 'hour'
    minutename = 'minutes' if minutes > 1 else 'minute'
    secondname = 'seconds' if remainingsecs > 1 else 'second'
    results = []
    if years > 0:
        results.append(resultformat.format(years, yearname))
    if days > 0:
        results.append(resultformat.format(days, dayname))
    if hours > 0:
        results.append(resultformat.format(hours, hourname))
    if minutes > 0:
        results.append(resultformat.format(minutes, minutename))
    if remainingsecs > 0:
        results.append(resultformat.format(remainingsecs, secondname))
    if len(results) > 1:
        result = ', '.join(results[0:len(results)-1])
        result += ' and ' + results[-1]
    else:
        result = results[0]
    print result

# format_duration(62)
# format_duration(120)
# format_duration(3600)
format_duration(3662)
