from queens import *
import sys
import time

# We could call this function for N = 4,5,...,14 and log the runtime
# After that we can optimize the code and visualize the speed improvements.
def main():
    if (len(sys.argv) <= 2):
        print('Usage: python queens-main.py <N> <M>')
        exit(0)
    # main()
    N1 = int(sys.argv[1])
    N2 = int(sys.argv[2])

    computation_times = dict()

    for N in range(N1, N2+1):
        start_time = time.time()
        printOne(N)
        end_time = time.time()
        print('---{}: {:.3f} seconds ---'.format(N, end_time - start_time))
        computation_times[N] = round(1000*(end_time - start_time))

    with open('computation_times2.txt', 'a') as file_object:
        file_object.write('N,milliseconds\n')
        for N in range(N1, N2+1):
            file_object.write("{},{}\n".format(N, computation_times[N]))


if __name__ == '__main__':
    printAll(8)
    #main()
