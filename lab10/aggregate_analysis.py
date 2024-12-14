def aggregate_analysis(operations):
    total_cost = 0
    for i, op in enumerate(operations, 1):
        if i == 2 ** int(i.bit_length() - 1):  # Powers of 2 (i.e., 1, 2, 4, 8, 16, ...)
            total_cost += 2 ** (i.bit_length() - 1)  # Cost of powers of 2
        else:
            total_cost += 1  # Cost for other operations
    return total_cost

# Жишээ
operations = ['op1', 'op2', 'op3', 'op4', 'op5', 'op6']
print(aggregate_analysis(operations))  # Үр дүнг харна
