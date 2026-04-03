# flames.py

def calculate_flames(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    for letter in name1[:]:
        if letter in name2:
            name1 = name1.replace(letter, '', 1)
            name2 = name2.replace(letter, '', 1)

    count = len(name1 + name2)

    flames = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemies', 'Siblings']

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames = flames[:len(flames) - 1]

    return flames[0]
