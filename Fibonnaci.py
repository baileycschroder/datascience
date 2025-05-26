def fibonacci_sequence(n):
    result = []
    a = 0
    b = 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# This implementation contains several bugs
def calculate_fibonacci_stats(sequence_length):
    sequence = fibonacci_sequence(sequence_length)
    if len(sequence) == 0:
        stats = {
            'sequence': sequence,
            'average': None,
            'maximum': None,
            'minimum': None,
            'length': 0
        }
    else:
        stats = {
            'sequence': sequence,
            'average': sum(sequence) / len(sequence),
            'maximum': max(sequence),
            'minimum': min(sequence),
            'length': len(sequence)
        }
    return stats