# -*- coding: utf-8 -*-

import sys
import copy

# novieto jaunu dāmu uz horizontāles h (0, 1, ..., n-1)
def place_queen(li, n, h):
    #print('h = {}'.format(h))
    if h == n:
        print('Iegūts pirmais atrisinājums: ')
        print(li)
        sys.exit()
    feasible_v = []
    for v in range(n):
        #print('v = {}'.format(v))
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
    #if len(feasible_v) == 0:
    #    print('Strupceļš izvietojumam {}'.format(li))
    for v in feasible_v:
        lii = copy.deepcopy(li)
        lii.append([h, v])
    #    print('Pievieno dāmu [{},{}] izvietojumam {})'.format(h, v, li))
        place_queen(lii, n, h + 1)


def main():
    n = int(input('Ievadiet kvadrāta izmēru: '))
    li = []
    place_queen(li, n, 0)



if __name__ == '__main__':
    main()