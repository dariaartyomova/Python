mat = [[2,3,-1],[-4,0,2],[-2,4,1]]
def fun(mtx):
    return 0 == ((mtx[0][0] * mtx[1][1] * mtx[2][2] +
            mtx[0][1] * mtx[1][2] * mtx[2][0] +
            mtx[0][2] * mtx[1][0] * mtx[2][1] -
            mtx[0][2] * mtx[1][1] * mtx[2][0] -
            mtx[0][1] * mtx[1][0] * mtx[2][2] -
            mtx[0][0] * mtx[1][2] * mtx[2][1]))
print(fun(mat))