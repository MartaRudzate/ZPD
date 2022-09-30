from queens import *
import sys

# We could call this function for N = 4,5,...,14 and log the runtime
# After that we can optimize the code and visualize the speed improvements.
def main(N):
    printOne(N)

if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        print('Usage: python queens-main.py <N>')
        exit(0)
    # main()
    aa = sys.argv[1]
    main(int(aa))
