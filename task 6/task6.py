import numpy as np

def testfun1(n):
    funtype = 2
    a = -1
    b = 1
    h = (b-a)/n
    xi = np.arange(a,b,h)
    pi = 1/(2+xi)
    qi = np.cos(xi)
    ri = xi * 0
    fi = 1 + xi 
    boundary = np.array([[1,0,0],
                        [1,0,0]])

def testfun2(n):
    funtype = 1
    a = -1
    b = 1
    h = (b-a)/n
    xi = np.arange(a, b, h)
    pi = 1/(xi-3)
    qi = 1+xi/2
    ri = np.exp(xi/2)
    fi = 2 - xi
    boundary = np.array([[1, 0, 0],
                      [1, 0, 0]])

def testfun3(n):
    funtype = 1
    a = 0
    b = 3.14/2
    h = (b-a)/n
    xi = np.arange(a, b, h)
    pi = xi*0-1
    qi = xi*0
    ri = xi*0+1
    boundary = np.array([[1, 0, 0],
                         [-1, 1, 2]])

    
    

def difapp(pi,qi,ri,fi,boundary,h,funtype,n):
    ai, bi, ci = (np.zeros(n) for i in range(3))
    
    if funtype == 1:
        ai = (-pi/(h**2) + qi/(2*h))
        bi = (2*pi/(h**2) + ri)
        ci = (-pi/(h**2) + qi/(2*h))
        matrix = np.column_stack((ai, bi, ci, fi))
        matrix[0], matrix[-1] = 0, 0
    else:
        for i in range(1,n-1):
            ai[i] = -pi[i-1]/(h**2)-qi[i]/(2*h)
            bi[i] = (pi[i+1] - pi[i-1])/(h**2) + ri[i]
            ci[i] = -pi[i+1] - qi[i]/(2*h)
            matrix = np.column_stack((ai, bi, ci, fi))
    matrix[0], matrix[-1] = 0, 0

    matrix[0][1] = boundary[0][0]+boundary[0][2]/h
    matrix[0][2] = -1*boundary[0][1]/h
    matrix[0][3] = boundary[0][2]
    matrix[n-1][0] = -1*boundary[1][1]/h
    matrix[n-1][1] = boundary[1][0]+boundary[1][2]/h
    matrix[n-1][3] = boundary[1][2]

    tridiag(matrix,n)


def tridiag[matrix,n]:
    ti, si, y = (np.zeros(n) for i in range(3))
    si[0] = -1*matrix[0][2]/matrix[0][1]
    ti[0] = matrix[0][3]/matrix[0][1]
    si[0] = 0
    for i in range(1,n):
        si[i] = matrix[i][2]/(matrix[i][1]-matrix[i][0]*si[i-1])
        ti[i] = (matrix[i][0]*ti[i-1] - matrix[i][3])/(matrix[i][1]-matrix[i][0]*si[i-1])
    y[n-1] = ti[n-1]
    for i in range(n-2,-1, -1):
        y[i] = si[i]*y[i+1]+ti[i]
    print(y)

    
