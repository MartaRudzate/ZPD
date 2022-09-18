import matplotlib.pyplot as plt
import numpy as np
import math


hilbert_lists = dict()

# Mazo kvadrātiņu apstaigāšanas secības dažādām Hilberta līknēm:
# hilbert_lists[1] = [(0,0), (0,1), (1,1), (1,0)]
# hilbert_lists[2] = [(0,0), (1,0), (1,1), (0,1), (0,2), (0,3), (1,3), (1,2),
#    (2,2), (2,3),(3,3),(3,2), (3,1), (2,1),(2,0), (3,0)]
# Šie izsaukumi ir rekursīvi un laikietilpīgi, tāpēc tos līdz vajadzīgajai vērtībai
# rēķina tikai vienu reizi - izsauc no main()
def recursive_hilbert(NN):
    global hilbert_lists
    for k in range(1,NN+1):
        if k == 1:
            hilbert_lists[1] = [(0,0), (0,1), (1,1), (1,0)]
        else:
            L1 = list([(y,x) for (x,y) in hilbert_lists[k-1]])
            L2 = list([(x,y+2**(k-1)) for (x,y) in hilbert_lists[k-1]])
            L3 = list([(x+2**(k-1),y+2**(k-1)) for (x,y) in hilbert_lists[k-1]])
            L4 = list([(2**(k-1) - 1 - y + 2**(k-1), 2**(k-1) - 1 - x) for (x,y) in hilbert_lists[k-1]])
            hilbert_lists[k] = (L1+L2+L3+L4)



# Atgriež j-to locekli no hilbert_lists[k]
def dh(j,k):
    global hilbert_lists
    if j < 0:
        j == 0
    if j >= 2**(2*k):
        j = 2**(2*k) - 1
    if k < 1:
        return (0,0)
    else:
        return hilbert_lists[k][j]


def hh(k,t):
    # delta ir 1/3, 1/15 utt. - cik gabalos sagriezts [0;1] nogrieznis
    delta = 1/(2**(2*k) - 1)
    j_t = math.floor(t/delta)
    # atrod mazo kvadrātiņu centrus (veselo skaitļu koordinātēs)
    (x0,y0) = dh(j_t, k)
    (x1,y1) = dh(j_t + 1, k)
    # Mazo kvadrātiņu centru x koordinātes, starp kurām kustas mūsu punkts
    xx0 = (2*x0 + 1)/2**(k+1)
    xx1 = (2*x1 + 1)/2**(k+1)
    # atrod "svērtu vidējo", kas savienotu xx0, xx1 ar taisnu nogriezni
    x = (2**(2*k) - 1)*((j_t*delta + delta - t)*xx0 + (t - j_t*delta)*xx1)
    return x


def main():
    # Sabūvē Hilberta sarakstus līdz H7 (H7 ir jau 2**14 mazo kvadrātiņu koordinātes)
    recursive_hilbert(7)
    step = 0.00001 # how often we sample the points to draw the graph.
    t = np.arange(0,1+step,step)  # generate numpy array [0, step, 2*step, ...]

    x7 = np.array([hh(7,t_i) for t_i in t])

    x1 = np.array([hh(1,t_i) for t_i in t])
    x2 = np.array([hh(2,t_i) for t_i in t])
    x3 = np.array([hh(3,t_i) for t_i in t])


    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('Hilbert Curve on x-axis: 3 Iterations and their Limit')

    ax1.plot(t,x1,t,x2,t,x3)
    ax1.grid(color='lightgray', linestyle='dashed', linewidth=0.5)
    ax1.legend(['H1(t)', 'H2(t)', 'H3(t)'])

    ax2.plot(t,x7,color='r',linewidth=0.2)
    ax2.grid(color='lightgray', linestyle='dashed', linewidth=0.5)

    plt.xlabel('Curve parameter t in [0,1]')
    plt.show()


if __name__ == '__main__':
    main()
