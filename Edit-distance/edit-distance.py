import sys

a=sys.stdin.readline()  # string 1
b=sys.stdin.readline()  # string 2

def editDist(str1, str2):
    m=len(str1)
    n=len(str2)

    # D is an (m+1)x(n+1) matrix that stores the edit distances.
    # D[i,j] denotes the edit distance between str1[0...i-1] and str2[0...j-1]
    # The edit distance between the two strings is stored in D[m][n]
    D = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # op is an (m+1)x(n+1) matrix that stores the "backtrace" of the performed operations
    # The elements in this matrix can be "left", "up", "d" (diagonal), and "none".
    # E.g., if op[i][j]=="up" this means that the cell (i,j) came from the cell above (deletion)
    # op[0][0] is the only cell that will contain "none" at the end
    op = [["none" for x in range(n+1)] for x in range(m+1)]

    # We compute D[i][j] for each i in (0,m) and for each j in (0,n)
    # by first computing D[i][j] for small i,j and then computing larger D[i][j]
    # based on previosly computed smaller values
    for i in range(m + 1):
        for j in range(n + 1):

            # If the first string is empty, we have to insert all characters
            # from the second string. Thus, each cell in the first row has
            # edit distance equal to its column position in the matrix
            if i == 0:
                D[i][j] = j
                if j!=0:
                    op[i][j]="left"

            # If the second string is empty, we have to remove all characters
            # from the first string. Thus, each cell in the first column has
            # edit distance equal to its row position in the matrix
            elif j == 0:
                D[i][j] = i
                if i!=0:
                    op[i][j]="up"

            # If the two strings have the same character at the corresponding
            # positions, we don't perform any operations and simply go to the
            # next position in both strings. Thus, the edit distance doesn't
            # increase and the cell gets the value of the cell in the uppper-left diagonal
            elif str1[i-1] == str2[j-1]:
                D[i][j] = D[i-1][j-1]
                op[i][j]="d"

            # If the two strings have different characters at the corresponding
            # positions, we need to perform an operation. We choose the operation
            # that will decrease the edit distance the least.
            # Each operation costs 1 unit
            else:
                minimum = min(D[i][j-1], D[i-1][j], D[i-1][j-1])

                if minimum == D[i-1][j]:   # Deletion
                    op[i][j]="up"
                elif minimum == D[i][j-1]: # Insertion
                    op[i][j]="left"

                else:                      # Substitution
                    op[i][j]="d"
                D[i][j] = 1 + minimum

    # Once we filled the matrices D and op, we have to trace the path
    # from the lower right corner of the matrices to read off the alignment
    # We store the directions in which we moved in the array A
    A=[]
    i=m
    j=n
    while (i>0 or j>0):
        direction = op[i][j]
        A.append(direction)
        if direction=="up":
            i=i-1
        elif direction=="left":
            j=j-1
        elif direction=="d":
            i=i-1
            j=j-1

    # We have to reverse the order of the directions so that we know how we
    # move across the matrix strating from cell (0,0)
    A.reverse()

    al1=""  # The first line of the output (allignment)
    al2=""  # The second line of the output (allignment)
    l1=0    # Keeps track of the position of the next character in string1 to be alligned
    l2=0    # Keeps track of the position of the next character in string2 to be alligned

    # Now we apply the directions stored in A to the two strings to get the allignment
    for op in A:
        if op=="left":          # Insertion
            al1=al1+" "
            al2=al2+str2[l2]
            l2=l2+1
        elif op=="up":          # Deletion
            al1=al1+str1[l1]
            l1=l1+1
            al2=al2+" "

        elif op=="d":           # Substitution/no operation
            al1=al1+str1[l1]
            l1=l1+1
            al2=al2+str2[l2]
            l2=l2+1

    print(str(D[m][n])+"\n"+al1+al2, end="")


editDist(a,b)
