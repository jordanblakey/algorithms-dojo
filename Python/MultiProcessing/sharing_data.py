import multiprocessing
result = []


def calc_square(numbers, result, value):
    value.value = 5.67
    for i, n in enumerate(numbers):
        result[i] = n*n
    print('inside process ' + str(result))


if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = multiprocessing.Array('i', 3)
    value = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, value))
    p.start()
    p.join()

    print(result[:])
    print(value.value)
