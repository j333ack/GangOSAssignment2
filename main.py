import sys

def main():

    print("Banker's algorithm demonstration")
    n = 5   # Numbers of processe
    r = 3   # Number of resources
    alloc = [[0, 1, 0],
             [2, 0, 0],
             [3, 0, 2],
             [2, 1, 1],
             [0, 0, 2]]
    print("Allocation resources:")
    for row in alloc:
        print(*row)
    print()

    max = [[7, 5, 3],
           [3, 2, 2],
           [9, 0, 2],
           [2, 2, 2],
           [4, 3, 3]]
    print("Max resources:")
    for row in max:
        print(*row)
    print()

    avail = [3, 3, 2]  # Request granted
#    avail = [1, 1, 1]  # Request denied
    print("Available resources:")
    print(*avail, sep=' ')
    print()

    f = [0] * n     # Intialize finished array to 0
    ans = [0] * n
    ind = 0
    need = [[0] * r for _ in range(n)]
    #unsafe = False

    for i in range(n):
        for j in range(r):
            need[i][j] = max[i][j] - alloc[i][j]

    y = 0
    for k in range(n):
        for i in range(n):
            if f[i] == 0:
                flag = 0
                for j in range(r):
                    if need[i][j] > avail[j]:
                        flag = 1
#                        print("No guaranteed safe sequence!")
                        #unsafe = True
                        break

                if flag == 0:
                    ans[ind] = i
                    ind += 1
                    for y in range(r):
                        avail[y] += alloc[i][y]
                    f[i] = 1

    print("Need matrix:")
    for row in need:
        print(*row)
    print()
    
    if ind < n:
        print("No guaranteed safe sequence!")
        print()
        sys.exit()

    #if unsafe:
    #    print("No guaranteed safe sequence!")
    #    print()
    #    sys.exit()

    print("The safe sequence is as follows")
    for i in range(n - 1):
        print(f' P{ans[i]} ->', end='')
    print(f' P{ans[n - 1]}\n')

    return

if __name__ == "__main__":
    main()
