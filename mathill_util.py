"""
Para calcular el inverso de una matriz
Step 1: Key^(-1) = (Det(key))^(-1) * Adj(Key)
>>> Adj(key) = 
Step 2: Transpose Key
Step 3: Find minor
Step 4: Find cofactor
"""
# DIVIDIR TEXTO EN VECTOR DE n POSICIONES
def divide_str(l, n, pad):
    for i in range(0, len(l), n):
        yield l[i:i + n] + (pad * (n - len(l[i:i + n])))

def divide_num(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

# MULTIPLICAR MATRIZ x VECTOR
# http://code.activestate.com/recipes/121574-matrix-vector-multiplication/
def mat_x_vec(m, v):
    rows = len(m)
    w = [0] * rows
    irange = range(len(v))
    suma = 0
    for j in range(rows):
        r = m[j]
        for i in irange:
            suma += r[i] * v[i]
        w[j], suma = suma, 0
    return w

# GENERAR MATRIZ DE CEROS
# https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module
def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M

# GENERAR MATRIZ IDENTIDAD
# https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module
def identity_matrix(n):
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1
    return I

# COPIAR UN MATRIZ
# https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module
def copy_matrix(M):
    # Section 1: Get matrix dimensions
    rows = len(M)
    cols = len(M[0])
    # Section 2: Create a new matrix of zeros
    MC = zeros_matrix(rows, cols)
    # Section 3: Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]
    return MC

# DETERMINANTE DE UNA MATRIZ
# https://integratedmlai.com/find-the-determinant-of-a-matrix-with-pure-python-without-numpy-or-scipy/
def determinant_fast(A):
    # Section 1: Establish n parameter and copy A
    n = len(A)
    AM = copy_matrix(A)
 
    # Section 2: Row ops on A to get in upper triangle form
    for fd in range(n): # A) fd stands for focus diagonal
        for i in range(fd+1,n): # B) only use rows below fd row
            if AM[fd][fd] == 0: # C) if diagonal is zero ...
                AM[fd][fd] == 1.0e-18 # change to ~zero
            # D) cr stands for "current row"
            crScaler = AM[i][fd] / AM[fd][fd] 
            # E) cr - crScaler * fdRow, one element at a time
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
     
    # Section 3: Once AM is in upper triangle form ...
    product = 1.0
    for i in range(n):
        # ... product of diagonals is determinant
        product *= AM[i][i] 
 
    return round(product)

# INVERSO MODULAR
# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def inv_mod_mul(a, mod):
	for i in range(mod):
		if (a*i)%mod is 1:
			return i

# MATRIZ TRANSPUESTA
# https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
def transpose_mat(m):
	t = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
	return t

# OBTENER MATRIZ MENOR
# https://stackoverflow.com/questions/53934405/find-minor-matrix-in-python
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

# MATRIZ DE MENORES
def minor_mat(m):
	m_min = []
	for i in range(len(m)):
		m_min.append([])
		for j in range(len(m[0])):
			m_min[i].append(round(determinant_fast(getMatrixMinor(m,i,j))))
	return m_min

# COFACTORES DE UNA MATRIZ
def cof_mat(mat):
	coef = 1
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			mat[i][j] *= (coef)
			coef *= -1
	return mat

# CALCULO DE LA MATRIZ INVERSA MODULAR
def inv_key(key, mod):
    determinant = determinant_fast(key) % mod
    det_inverse = inv_mod_mul(determinant, mod)
    transpuesta = transpose_mat(key)
    menores = minor_mat(transpuesta)
    cofactores = cof_mat(menores)
    inversa = []
    for i in range(len(cofactores)):
        inversa.append([])
        for j in range(len(cofactores[0])):
            inversa[i].append([])
            inversa[i][j] = (cofactores[i][j] * det_inverse) % mod
    return inversa

# REDONDEO POR ENCIMA
# https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module
def round_up(n):
    res = int(n)
    return res if res == n or n < 0 else res+1

# RAIZ CUADRADA MODULAR
def mod_sqrt(x):
    res = round_up(x ** (1/2))
    return res

# MATRIZ DE CLAVE
def mat_key(key, abc):
    k_mat = []
    k = 0
    l = len(key)
    d_mat = mod_sqrt(l)
    while k < l:
        for i in range(d_mat):
            k_mat.append([])
            for j in range(d_mat):
                if k < l:
                    k_mat[i].append(abc.index(key[k]))
                    k += 1
                else:
                    k_mat[i].append(0)
    return k_mat

def mat_key_ascii(key):
    padding = '0'
    k_mat = []
    k = 0
    l = len(key)
    d_mat = mod_sqrt(l)
    while k < l:
        for i in range(d_mat):
            k_mat.append([])
            for j in range(d_mat):
                if k < l:
                    k_mat[i].append(ord(key[k]))
                    k += 1
                else:
                    k_mat[i].append(ord(padding))
    return k_mat