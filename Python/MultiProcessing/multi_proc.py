import time
import multiprocessing


square_result = []
cube_result = []


def calc_square(numbers):
    for n in numbers:
        # time.sleep(5)
        print('square: ' + str(n * n))
        square_result.append(n*n)


def calc_cube(numbers):
    for n in numbers:
        # time.sleep(5)
        print('cube: ' + str(n*n*n))
        cube_result.append(n*n*n)


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('result ' + str(square_result))
    print('result ' + str(cube_result))
    print("DONE")
