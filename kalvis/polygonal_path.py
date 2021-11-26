# -*- coding: utf-8 -*-

# Operatoru pārdefinēšanas piemēri
# https://www.programiz.com/python-programming/operator-overloading
# https://www.mdpi.com/2073-8994/11/2/191/pdf-vor

class Point3d:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point3d(x, y, z)

    def abs(self):
        return max(abs(self.x), abs(self.y), abs(self.z))

def main():
    lis = [[0, 1], [2, 1.0], [3, -1.5], [4, 2.0], [5, -2.5], [6, 3.0], [7, -3.5], [8, 4.0], [9, -4.5], [10, 5.0],
            [11, -5.5], [12, 6.0], [13, -6.5], [14, 7.0], [15, -7.5], [16, 8.0], [17, -8.5], [18, 9.0], [19, -9.5],
            [20, 10.0], [21, -10.5], [22, 11.0], [23, -11.5], [24, 12.0], [25, -12.5], [26, 13.0], [27, -13.5],
            [28, 14.0], [29, -14.5], [30, 15.0], [31, -15.5], [32, 16.0], [0, 33], [34, -17.0], [35, 17.5], [36, -18.0],
            [37, 18.5], [38, -19.0], [39, 19.5],
            [40, -20.0], [41, 20.5], [42, -21.0], [43, 21.5], [44, -22.0], [45, 22.5], [46, -23.0], [47, 23.5],
            [48, -24.0], [49, 24.5], [50, -25.0], [51, 25.5], [52, -26.0], [0, -53], [-54, 27.0], [-55, -27.5],
            [-56, 28.0], [-57, -28.5], [-58, 29.0], [-59, -29.5], [-60, 30.0], [-61, -30.5], [-62, 31.0], [-63, -31.5],
            [-64, 32.0], [-65, -32.5], [-66, 33.0], [-67, -33.5], [-68, 34.0], [-69, -34.5], [-70, 35.0], [-71, -35.5],
            [-72, 36.0], [-73, -36.5], [-74, 37.0]]

    ######################################
    # Piemēri punktiem un pārvietojumiem.
    ######################################
    p0 = Point3d(0, 0, 0)
    # 1 solis uz austrumiem; tas pats kas [0,1]
    d1 = Point3d(1, 0, -1)
    # 2 solis uz ziemeļaustrumiem; tas pats kas [2, 1.0]
    d2 = Point3d(2, -2, 0)
    # 3 soļi uz ziemeļrietumiem; tas pats, kas [3, -1.5]
    d3 = Point3d(0, -3, 3)



    dlist = []
    for ll in lis:
        LL0 = int(round(ll[0]))
        LL1 = int(round(ll[1]))
        if LL0 == 0:
            dlist.append(Point3d(LL1, 0, -LL1))
        elif LL0*LL1 > 0:
            dlist.append(Point3d(LL0, -LL0, 0))
        elif LL0*LL1 < 0:
            dlist.append(Point3d(0, -LL0, LL0))


    p = p0
    lengths = []
    print('p = {}'.format(p))
    for delta in dlist:
        lengths.append(delta.abs())
        p += delta
        print('p = {}'.format(p))

    if lengths == list(range(1, len(dlist)+1)):
        print('Polimonds apmierina Cibuļa nosacījumu; posmu garumi: {}'.format(lengths))
    else:
        print('Polimonds NEapmierina Cibuļa nosacījumu; posmu garumi: {}'.format(lengths))


if __name__ == '__main__':
    main()
