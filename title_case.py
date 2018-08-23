def title_case(title, minor_words):
    minors = minor_words.split(' ')
    title = title.title()
    title_list = title.split(' ')
    for minor in minors:
        for i, word in enumerate(title_list[1:]):
            lower_word = word.lower()
            if lower_word == minor.lower():
                title_list[i + 1] = lower_word
    return ' '.join(title_list)

def title_case_comp(title, minor_words):
    title = title.title()
    if not minor_words:
        return title
    minors = minor_words.split(' ')
    title_list = title.split(' ')
    minor_updates = [(i + 1, word.lower()) for minor in minors for (i, word) in enumerate(title_list[1:]) if word.lower() == minor.lower()]
    for i, word in minor_updates:
        title_list[i] = word
    return ' '.join(title_list)


print(title_case_comp('a clash of KINGS', 'a an the of'))
print(title_case_comp('THE WIND IN THE WILLOWS', 'The In'))