# All the codes presented below were developed by:
#   Dr. Gerardo Tinoco Guerrero
#   Universidad Michoacana de San Nicolás de Hidalgo
#   gerardo.tinoco@umich.mx
#
# With the funding of:
#   National Council of Science and Technology, CONACyT (Consejo Nacional de Ciencia y Tecnología, CONACyT). México.
#   Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH). México
#   Aula CIMNE-Morelia. México
#
# Date:
#   November, 2022.
#
# Last Modification:
#   January, 2023.

import numpy as np
 
def Mesh(x, y, L):
    # 2D Meshes Gammas Computation.
    # 
    # This routine computes the Gamma values for logically rectangular meshes.
    # 
    # Input parameters
    #   x           m x n           Array           Array with the coordinates in x of the nodes.
    #   y           m x n           Array           Array with the coordinates in y of the nodes.
    #   L           5 x 1           Array           Array with the values of the differential operator.
    # 
    # Output parameters
    #   Gamma       m x n x 9       Array           Array with the computed gamma values.

    me       = x.shape                                                              # The size of the mesh is found.
    m        = me[0]                                                                # The number of nodes in x.
    n        = me[1]                                                                # The number of nodes in y.
    Gamma    = np.zeros([m,n,9])                                                    # Gamma initialization with zeros.

    for i in range(1,m-1):                                                          # For each of the nodes in x.
        for j in range(1,n-1):                                                      # For each of the nodes in y.
            dx = np.array([x[i + 1, j]   - x[i, j], x[i + 1, j + 1] - x[i, j], \
                           x[i, j + 1]   - x[i, j], x[i - 1, j + 1] - x[i, j], \
                           x[i - 1, j]   - x[i, j], x[i - 1, j - 1] - x[i, j], \
                           x[i, j - 1]   - x[i, j], x[i + 1, j - 1] - x[i, j]])     # dx is computed.
            
            dy = np.array([y[i + 1, j]   - y[i, j], y[i + 1, j + 1] - y[i, j], \
                           y[i, j + 1]   - y[i, j], y[i - 1, j + 1] - y[i, j], \
                           y[i - 1, j]   - y[i, j], y[i - 1, j - 1] - y[i, j], \
                           y[i, j - 1]   - y[i, j], y[i + 1, j - 1] - y[i, j]])     # dy is computed.
            
            M = np.vstack([[dx], [dy], [dx**2], [dx*dy], [dy**2]])                  # M matrix is assembled.
            M = np.linalg.pinv(M)                                                   # The pseudoinverse of matrix M.
            YY = M@L                                                                # M*L computation.
            Gem = np.vstack([-sum(YY), YY])                                         # Gamma values are found.
            for k in range(9):                                                      # For each of the Gamma values.
                Gamma[i,j,k] = Gem[k]                                               # The Gamma value is stored.

    return Gamma

def Cloud(p, vec, L):
    # Unstructured Clouds of Points and Triangulations Gammas Computation.
    # 
    # This routine computes the Gamma values for unstructured clouds of points and triangulations.
    # 
    # Input parameters
    #   p           m x 3           Array           Array with the coordinates of the nodes and a flag for the boundary.
    #   vec         m x o           Array           Array with the correspondence of the o neighbors of each node.
    #   L           5 x 1           Array           Array with the values of the differential operator.
    # 
    # Output parameters
    #   Gamma       m x n x o       Array           Array with the computed gamma values.

    nvec  = len(vec[0,:])                                                           # The maximum number of neighbors.
    m     = len(p[:,0])                                                             # The total number of nodes.
    Gamma = np.zeros([m, nvec+1])                                                   # Gamma initialization with zeros.

    for i in np.arange(m):                                                          # For each of the nodes.
        if p[i,2] == 0:                                                             # If the node is not in the boundary.
            nvec = sum(vec[i,:] != -1)                                              # The total number of neighbors of the node.
            dx = np.zeros([nvec])                                                   # dx initialization with zeros.
            dy = np.zeros([nvec])                                                   # dy initialization with zeros.

            for j in np.arange(nvec):                                               # For each of the neighbor nodes.
                vec1 = int(vec[i, j])                                               # The neighbor index is found.
                dx[j] = p[vec1, 0] - p[i,0]                                         # dx is computed.
                dy[j] = p[vec1, 1] - p[i,1]                                         # dy is computed.

            M = np.vstack([[dx], [dy], [dx**2], [dx*dy], [dy**2]])                  # M matrix is assembled.
            M = np.linalg.pinv(M)                                                   # The pseudoinverse of matrix M.
            YY = M@L                                                                # M*L computation.
            Gem = np.vstack([-sum(YY), YY]).transpose()                             # Gamma values are found.
            for j in np.arange(nvec+1):                                             # For each of the Gamma values.
                Gamma[i,j] = Gem[0,j]                                               # The Gamma value is stored.
    
    return Gamma

def K_Mesh(x, y, L, phi, f):
    me = x.shape
    m = me[0]
    n = me[1]
    K = np.zeros([(m-2)*(n-2), (m-2)*(n-2)])
    R  = np.zeros([(m-2)*(n-2), 1])

    for i in np.arange(1,m-1):
        for j in np.arange(1,n-1):
            u = np.array(x[i-1:i+2, j-1:j+2])
            v = np.array(y[i-1:i+2, j-1:j+2])
            dx = np.hstack([u[0,0] - u[1,1], u[1,0] - u[1,1], \
                            u[2,0] - u[1,1], u[0,1] - u[1,1], \
                            u[2,1] - u[1,1], u[0,2] - u[1,1], \
                            u[1,2] - u[1,1], u[2,2] - u[1,1]])
            dy = np.hstack([v[0,0] - v[1,1], v[1,0] - v[1,1], \
                            v[2,0] - v[1,1], v[0,1] - v[1,1], \
                            v[2,1] - v[1,1], v[0,2] - v[1,1], \
                            v[1,2] - v[1,1], v[2,2] - v[1,1]])
            M = np.vstack([[dx], [dy], [dx**2], [dx*dy], [dy**2]])
            M = np.linalg.pinv(M)
            YY = M@L
            Gamma = np.vstack([-sum(YY), YY])
            p = m*(j) + i
            K[p, p-1]   = Gamma[4]
            K[p, p]     = Gamma[0]
            K[p, p+1]   = Gamma[5]
            K[p, p-1-m] = Gamma[1]
            K[p, p-m]   = Gamma[2]
            K[p, p+1-m] = Gamma[3]
            K[p, p-1+m] = Gamma[6]
            K[p, p+m]   = Gamma[7]
            K[p, p+1+m] = Gamma[8]

            temp     = (i-1) + (m-2)*(j-1)                                      # Se buscan los nodos que son frontera.
            R[temp] += Gamma[0]*f(x[i,j], y[i,j])                              # Se agrega f al lado derecho.
    
    for j in np.arange(n):
        K[m*j, m*j] = 0
    
    for i in np.arange(1,m-1):
        p       = i+(n-1)*m
        K[i, i] = 0
        K[p, p] = 0

        temp       = i-1                                                        # Se asigna el valor de temp como los nodos de la primera frontera en x.
        R[temp] += phi(x[i,0], y[i,0])                                          # Se guarda la condición de frontera en el lado derecho.
        temp       = (i-1) + (m-2)*((m-1)-2)                                    # Se asigna el valor de temp como los nodos de la última frontera en x.
        R[temp] += phi(x[i,m-1], y[i,m-1])                                      # Se guarda la condición de frontera en el lado derecho.
        temp       = (m-2)*(i-1)                                                # Se asigna el valor de temp para los nodos de la primera frontera en y.
        R[temp] += phi(x[0,i], y[0,i])                                          # Se guarda la condición de frontera en el lado derecho.
        temp       = ((m-1)-2) + (m-2)*(i-1)                                    # Se asgina el valor de temp para los nodos de la última frontera en y.
        R[temp] += phi(x[m-1,i], y[m-1,i])                                      # Se guarda la condición de frontera en el lado derecho.                
    
    return K, R

def Cloud_K(p, vec, L):
    """
    2D Clouds of Points Gammas Computation.
     
    This function computes the Gamma values for clouds of points, and assemble the K matrix for the computations.
     
    Input:
        p           m x 3           Array           Array with the coordinates of the nodes and a flag for the boundary.
        vec         m x nvec        Array           Array with the correspondence of the 'nvec' neighbors of each node.
        L           5 x 1           Array           Array with the values of the differential operator.
     
     Output:
        K           m x m           Array           K Matrix with the computed Gammas.
    """
    # Variable initialization
    nvec  = len(vec[0,:])                                                           # The maximum number of neighbors.
    m     = len(p[:,0])                                                             # The total number of nodes.
    K     = np.zeros([m,m])                                                         # K initialization with zeros.
    
    # Gammas computation and Matrix assembly
    for i in np.arange(m):                                                          # For each of the nodes.
        if p[i,2] == 0:                                                             # If the node is an inner node.
            nvec = sum(vec[i,:] != -1)                                              # The total number of neighbors of the node.
            dx   = np.zeros([nvec])                                                 # dx initialization with zeros.
            dy   = np.zeros([nvec])                                                 # dy initialization with zeros.
            for j in np.arange(nvec):                                               # For each of the neighbor nodes.
                vec1  = int(vec[i, j])                                              # The neighbor index is found.
                dx[j] = p[vec1, 0] - p[i,0]                                         # dx is computed.
                dy[j] = p[vec1, 1] - p[i,1]                                         # dy is computed.
            M     = np.vstack([[dx], [dy], [dx**2], [dx*dy], [dy**2]])              # M matrix is assembled.
            M     = np.linalg.pinv(M)                                               # The pseudoinverse of matrix M.
            YY    = M@L                                                             # M*L computation.
            Gamma = np.vstack([-sum(YY), YY]).transpose()                           # Gamma values are found.
            K[i,i] = Gamma[0,0]                                                     # The corresponding Gamma for the central node.
            for j in np.arange(nvec):                                               # For each of the neighbor nodes.
                K[i, vec[i,j]] = Gamma[0,j+1]                                       # The corresponding Gamma for the neighbor node.
            
        if p[i,2] == 1:                                                             # If the node is in the boundary.
            K[i,i] = 0                                                              # Central node weight is equal to 0.
            for j in np.arange(nvec):                                               # For each of the neighbor nodes.
                K[:, i] = 0                                                         # Neighbor node weight is equal to 0.
                K[i,i] = 1
    return K