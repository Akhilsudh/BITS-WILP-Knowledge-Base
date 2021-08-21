# Octave Cheat Sheet

#### Define a 3x3 matrix
```matlab
A = [-1,1,2; 3,-1,1; -1,3,4]
```

#### Matrix properties
```matlab
A = [-1,1,2; 3,-1,1; -1,3,4]

det(A)

```

#### Norms
```matlab
A = [-1,1,2; 3,-1,1; -1,3,4]
norm(A, 1)
norm(A, 2)
norm(A, 'fro')
norm(A, 'inf')
```

#### Inverse of a matrix
```matlab
A = [-1,1,2; 3,-1,1; -1,3,4]
inv(A)
```

#### Determinant of a matrix
```matlab
A = [-1,1,2; 3,-1,1; -1,3,4]
det(A)
```

#### LU decompose a matrix
```matlab

# LU decompose withoput pivot
function [L, U] = lu_nopivot(A)
n = size(A, 1); % Obtain number of rows (should equal number of columns)
L = eye(n); % Start L off as identity and populate the lower triangular half slowly
for k = 1 : n
    % For each row k, access columns from k+1 to the end and divide by
    % the diagonal coefficient at A(k ,k)
    L(k + 1 : n, k) = A(k + 1 : n, k) / A(k, k);

    % For each row k+1 to the end, perform Gaussian elimination
    % In the end, A will contain U
    for l = k + 1 : n
        A(l, :) = A(l, :) - L(l, k) * A(k, :);
    end
end
U = A;
end

# LU decompose
[L, U, I] = lu(A)

```

#### Solve linear system of equations
```matlab

A = [2,1,-2; 1,-1,-1; 1,1,3]
B = [3;0;12]

A\B

%%%%%%%%%%%%%%%%%%%%%
%   ans =           %
%                   %
%       3.5000      %
%       1.0000      %
%       2.5000      %
%%%%%%%%%%%%%%%%%%%%%
```