import matplotlib.pyplot as plt
import copy
import sys

queen_list = []
found_solution = False

def place_queen(li, n, h):
    global queen_list
    global found_solution
    result = []
    if h == n:
        found_solution = True
        queen_list = copy.deepcopy(li)
    elif not found_solution:
        feasible_v = []
        for v in range(n):
            feasible = True
            for queen in li:
                if queen[1] == v:
                    # apdraudēts pa vertikāli
                    feasible = False
                    break
                if abs(queen[0] - h) == abs(queen[1] - v):
                    # apdraudēts pa diagonāli
                    feasible = False
                    break
            if feasible:
                feasible_v.append(v)
        for v in feasible_v:
            lii = copy.deepcopy(li)
            lii.append([h, v])
            place_queen(lii, n, h + 1)


def main():
    NN = 12
    global queen_list
    place_queen([], NN, 0)
    print("queen_list = {}".format(queen_list))

    for i in range(0, NN+1):
        plt.axhline (y = i, xmin=0, xmax=NN, color='gray', linestyle='solid', linewidth=1)
        plt.axvline (x = i, ymin=0, ymax=NN, color='gray', linestyle='solid', linewidth=1)

    for (i,j) in queen_list:
        cc = plt.Circle((j+0.5, NN - (i+0.5)), 0.2, color='blue')
        plt.gca().add_patch(cc)

    plt.xlim([0,NN])
    plt.ylim([0,NN])
    plt.axis('equal')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()
