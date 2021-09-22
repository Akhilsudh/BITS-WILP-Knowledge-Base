
import copy

# This class is to hold matrix data
class Matrix:
    def __init__(self, row: int, col: int, listOfList: list):
        self.n: int = row
        self.m: int = col
        self.data: list = listOfList


# This class has functions for different operations on a matrix
class MatrixOperations:
    def print(self, message:str, matrix:Matrix):
        '''Print Matrix
        Input:  message (A string to print before the matrix), matrix (A Matrix Object)
        Output: A multi line string of the Matrix data
        '''
        print()
        print(message)
        for row in matrix.data:
            line: str = ""
            for element in row:
                line += str(element) + "\t"
            print(line)
        print()

    def REF(self, matrix:Matrix):
        '''Calculate the Row Echelon Form for a Matrix
        Input:  matrix (A Matrix Object)
        Output: REF (A Matrix Object holding the REF form for matrix)
        '''
        REF:Matrix = Matrix(matrix.n, matrix.m, matrix.data)
        for i in range(REF.n):
            # Pivot the row when the pivot element is 0
            if (REF.data[i][i] == 0):
                for j in range(i, REF.n):
                    # Find the row with greatest value below pivot element and swap with that row 
                    if abs(REF.data[j][i]) > abs(REF.data[i][i]):
                       REF.data[j], REF.data[i] = REF.data[i], REF.data[j]
            for j in range(i + 1, REF.n):
                # Doing this once so that I minimize the number of divisions
                ratio: float = REF.data[j][i] / REF.data[i][i]
                # Assign 0 hence reducing multiplication and addition by one for elements under the pivot
                REF.data[j][i] = 0
                for k in range(i + 1, REF.m):
                    REF.data[j][k] = REF.data[j][k] - ratio * REF.data[i][k]
        return REF

    def augment(self, matrixA:Matrix, matrixB:Matrix):
        '''Augments two matrices
        Input:  matrixA (A Matrix Object), matrixB (B Matrix Object)
        Output: matrix (A Matrix Object holding the REF form for matrix)
        '''
        listOfList: list = copy.deepcopy(matrixA.data)
        for i in range(matrixA.n):
            listOfList[i].extend(matrixB.data[i])
        matrix: Matrix = Matrix(matrixA.n, matrixA.m + matrixB.m, listOfList)
        return matrix
    
    def rank(self, matrix:Matrix, isREF:bool=False):
        '''Calculate rank of matrix
        Input:  matrix (Matrix Object), isREF (A boolean flag that denotes if the given matrix is in REF form)
        Output: rank (Rank of matrix)
        '''
        if not ref:
            matrix = self.REF(matrix)
        rank: int = matrix.n
        while (rank - 1 >= 0):
            flag: bool = False
            for element in matrix.data[rank - 1]:
                print(element)
                if element == 0:
                    continue
                flag = True
            if flag:
                break
            rank -= 1
        return rank

    def backSubstitute(self, matrix:Matrix, isREF:bool=False):
        '''Solve set of linear equations given as an augmented matrix
        Input:  matrix (Augmented Matrix Object), isREF (A boolean flag that denotes if the given matrix is in REF form)
        Output: x (Matrix object of the result x)
        '''
        if not isREF:
            matrix = self.REF(matrix)
        n = matrix.n
        data = matrix.data
        x: list = [0] * n
        x[n-1] = data[n-1][n] / data[n-1][n-1]
        for i in range(n-2, -1, -1):
            x[i] = matrix.data[i][n]
            for j in range(i+1, n):
                x[i] = x[i] - data[i][j] * x[j]
            x[i] = x[i] / data[i][i]
        return Matrix(1, n, [x])

def main():
    print('=======================================================================')
    print('This commandline utility accepts two matrices is Ax = b format')
    print('Enter details for A: ')
    print('Enter number of rows: ')
    n: int = int(input())
    print('Enter number of columns: ')
    m: int = int(input())
    listOfList: list = []
    i: int = 0
    while(i < n):
        print('Enter the '+ str(i) +' row elements')
        row: list = list(map(float, input().split()))
        if len(row) > m:
            print('number of elements in row greater than column count hence truncating')
        del row[m:]
        print(row)
        listOfList.append(row)
        i += 1
    matrixA: Matrix = Matrix(n, m, listOfList)
    print('=======================================================================')
    print('Enter details for b: ')
    listOfList: list = []
    i: int = 0
    while(i < n):
        print('Enter the '+ str(i) +' row element')
        row: list = list(map(float, input().split()))
        if len(row) > 1:
            print('number of elements in row greater than 1 truncating')
        del row[1:]
        print(row)
        listOfList.append(row)
        i += 1
    matrixB: Matrix = Matrix(n, 1, listOfList)
    print('=======================================================================')
    operation: MatrixOperations = MatrixOperations()
    operation.print('Input Matrix A is:', matrixA)
    operation.print('Input Matrix B is:', matrixB)
    matrix:  Matrix = operation.augment(matrixA, matrixB)
    operation.print('Augmented Matrix is:', matrix)
    matrix:Matrix = operation.REF(matrix)
    operation.print('REF for Matrix is:', matrix)
    x:Matrix = operation.backSubstitute(matrix, True)
    operation.print('Solution Matrix x is:', x)
    print('=======================================================================')

if __name__ == '__main__':
    main()





global:
  scrape_interval:     15s # By default, scrape targets every 15 seconds.

  # Attach these labels to any time series or alerts when communicating with
  # external systems (federation, remote storage, Alertmanager).
  external_labels:
    monitor: 'codelab-monitor'

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # Override the global default and scrape targets from this job every 5 seconds.
    scrape_interval: 5s

    static_configs:
      - targets: ['localhost:9090']




num = 1
sum = 1
i = 1
while i <= n
    num = num * 3
    sum = sum + num
    i = i + 1
return sum

Analysis:
=> 1 + 1 + 1 + n + n (1 + 1 + 1) + 1
=> 4 + n (4)
=> 4n + 4
=> 4n


First iteration:
num = 1
sum = 1
num_new = 3
sum_new = 1 + 3

Second iteration:
num = 3
sum = 1 + 3
num_new = 3 * 3 = 9
sum_new = 1 + 3 + 9

Third iteration:
num = 9
sum = 1 + 3 + 9
num_new = 9 * 3 = 27
sum_new = 1 + 3 + 9 + 27