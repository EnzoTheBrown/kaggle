
havecabin(line):



compute_proba(data_set, condition):
    total = 0
    for line in data_set:
        if condition(line):
            total += 1
    return total/(len(data_set))


