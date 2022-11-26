def get_freq_map(nested_list, element):
    freq_map = []
    entries = 0
    for el in nested_list:
        if el == element:
            entries += 1
    freq_map.append(entries / len(nested_list))
    for el in nested_list:
        if isinstance(el, list):
            freq_map.append(get_freq_map(el, element))
    return freq_map
