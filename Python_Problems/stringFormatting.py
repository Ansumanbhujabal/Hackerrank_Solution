import decimal


def print_formatted(n):
    pattern = '{0:{1}} {0:{1}o} {0:{1}X} {0:{1}b}'
    bits = n.bit_length()

    print('\n'.join(
        pattern.format(i, bits) for i in range(1, n + 1)
    ))
