def isMarkovMatrix(m):
    n = len(m)
    if n != len(m[0]):
        return False
    for row in m:
        for element in row:
            if element < 0:
                return False
    for j in range(n):
        col_sum = sum(m[i][j] for i in range(n))
        if abs(col_sum - 1) > 1e-10:
            return False
    return True

def main():
    for _ in range(2):  
        print("Enter a 3 by 3 matrix row by row:")
        matrix = []
        for i in range(3):
            row = input().split()
            row = [float(x) for x in row]
            matrix.append(row)
        if isMarkovMatrix(matrix):
            print("It is a Markov matrix")
            print()
        else:
            print("It is not a Markov matrix")
            print()

if __name__ == "__main__":
    main()