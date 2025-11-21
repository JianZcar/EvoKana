def combine_left_right_rows(left, right):
    for i in range(len(left)):
        left[i].extend(right[i])
    return left
