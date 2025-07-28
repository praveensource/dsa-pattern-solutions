def construct2DArray(original, m, n):
    if len(original) != m * n:
        return []

    result = []
    for i in range(m):
        # Slice n elements for the current row
        start = i * n
        end = start + n
        row = original[start:end]
        result.append(row)

    return result
