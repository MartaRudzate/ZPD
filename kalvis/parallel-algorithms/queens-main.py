from queens import *
import sys
import time


# Call this for N = 4,5,...,14 (find the first valid queen placement) and log the runtime in milliseconds.
def main():
    if len(sys.argv) <= 2:
        print('Usage: python queens-main.py <n1> <n2>')
        exit(0)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    computation_times = dict()

    for n in range(n1, n2+1):
        start_time = time.time()

        # Find the first valid position on n*n chessboard
        qp = QueenPosition(n)
        qp.findNextPosition(0)
        qp.printLatestSolution()

        end_time = time.time()
        print('---{}: {:.3f} seconds ---'.format(n, end_time - start_time))
        computation_times[n] = round(1000*(end_time - start_time))

    with open('computation_times3.txt', 'a') as file_object:
        file_object.write('N,milliseconds\n')
        for n in range(n1, n2+1):
            file_object.write("{},{}\n".format(n, computation_times[n]))

# This function prints all valid queen placements on a N*N chessboard in a compact form
def outputAllQueenPositions(N):
    qp2 = QueenPosition(N)
    all_boards = []
    while qp2.findNextPosition(0):
        all_boards.append(qp2.latestSolution)
    for bb in all_boards:
        print(bb)
    print('all_boards count: {}'.format(len(all_boards)))

if __name__ == '__main__':
    # Find only the first solution for n*n chessboard (where "n" changes from n1(inclusive) to n2(non-inclusive))
    # Also log the time spent for finding each solution (depending on the chessboard size "n").
    main()

    # Unlike main() - find only the first solution for n*n chessboard, the following line finds all valid solutions
    # outputAllQueenPositions(4)



