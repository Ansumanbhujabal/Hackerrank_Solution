

def permutationEquation(p):
    output = []

    for num in range(1, max(p)+1):
        output.append(p.index(p.index(num)+1)+1)

    return output


print(permutationEquation([2, 3, 1]))
