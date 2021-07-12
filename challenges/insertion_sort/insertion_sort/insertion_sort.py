def insertion_sort(input):
    for i in range(1, len(input)):
        j = i - 1
        temp = input[i]

        while j >= 0 and temp < input[j]:
            input[j + 1] = input[j]
            j -= 1
        input[j + 1] = temp
        print(input)
    return input