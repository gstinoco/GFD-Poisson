"""
All the codes presented below were developed by:
    Dr. Gerardo Tinoco Guerrero
    Universidad Michoacana de San Nicolás de Hidalgo
    gerardo.tinoco@umich.mx

With the funding of:
    National Council of Science and Technology, CONACyT (Consejo Nacional de Ciencia y Tecnología, CONACyT). México.
    Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH). México
    Aula CIMNE-Morelia. México

Date:
    November, 2022.

Last Modification:
    March, 2023.
"""

import numpy as np

def PolyArea(x,y):
    """
    PolyArea
    Function to calculate the area of a polygon defined by the vertices whose coordinates are stored in $x$ and $y$.
    
    Input:
        x           m x n           Array           Array with the coordinates in x of the vertices of the polygon.
        y           m x n           Array           Array with the coordinates in y of the vertices of the polygon.
    
    Output:
        area                        Real            Area of the polygon.
    """
    
    area = 0.5*np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    return area
 
def Mesh(x, y, u_ap, u_ex):
    """
    Mesh_Transient
    Function to compute the error in a logically rectangular mesh for a problem that depends on time.
    The polygon used to calculate the area is the one defined by all the immediate neighbors of the central node.
    
    Input:
        x           m x n           Array           Array with the coordinates in x of the nodes.
        y           m x n           Array           Array with the coordinates in y of the nodes.
        u_ap        m x n x t       Array           Array with the computed solution.
        u_ex        m x n x t       Array           Array with the theoretical solution.
    
    Output:
        er          t x 1           Array           Mean square error computed on each time step.
    """

    m = len(x[:,0])                                                                 # The number of nodes in x.
    n = len(x[0,:])                                                                 # The number of nodes in y.
    er   = 0                                                                        # er initialization with 0.
    area = np.zeros([m,n])                                                          # area initialization with zeros.

    for i in np.arange(1,m-1):                                                      # For each of the nodes on the x axis.
        for j in np.arange(1,n-1):                                                  # For each of the nodes on the y axis.
            px = np.array([x[i+1, j], x[i+1, j+1], x[i, j+1], x[i-1, j+1], \
                           x[i-1, j], x[i-1, j-1], x[i, j-1], x[i+1, j-1]])         # The x-values of the polygon are stored.
            py = np.array([y[i+1, j], y[i+1, j+1], y[i, j+1], y[i-1, j+1], \
                           y[i-1, j], y[i-1, j-1], y[i, j-1], y[i+1, j-1]])         # The y-values of the polygon are stored.
            area[i,j] = PolyArea(px,py)                                             # Area computation.

    for i in np.arange(m):                                                          # For each of the nodes on the x axis.
        for j in np.arange(n):                                                      # For each of the nodes on the y axis.
            er = er + area[i,j]*(u_ap[i,j] - u_ex[i,j])**2                          # Mean square error computation.
    
    er = np.sqrt(er)                                                                # The square root is computed.
    
    return er

def Cloud(p, vec, u_ap, u_ex):
    """
    Cloud
    Function to compute the error in a triangulation or an unstructured cloud of points for a problem that depends on time.
    The polygon used to calculate the area is the one defined by all the immediate neighbors of the central node.
    
    Input:
        p           m x 2           Array           Array with the coordinates of the nodes.
        vec         m x nvec        Array           Array with the correspondence of the nvec neighbors of each node.
        u_ap        m x t           Array           Array with the computed solution.
        u_ex        m x t           Array           Array with the theoretical solution.
    
    Output:
        er          t x 1           Array           Mean square error computed on each time step.
    """

    m    = len(p[:,0])                                                              # The total number of nodes is calculated.
    er   = 0                                                                        # er initialization with 0.
    area = np.zeros(m)                                                              # area initialization with zeros.

    for i in np.arange(m):
        nvec = sum(vec[i,:] != -1)                                                  # The number of neighbors of the central node.
        polix = np.zeros([nvec])                                                    # The x-values of the polygon are stored.
        poliy = np.zeros([nvec])                                                    # The y-values of the polygon are stored.
        for j in np.arange(nvec):                                                   # For each of the neighbor nodes.
            vec1 = int(vec[i,j])                                                    # The index of the node is found.
            polix[j] = p[vec1,0]                                                    # The x coordinate of the node is stored.
            poliy[j] = p[vec1,1]                                                    # The y coordinate of the node is stored.
        area[i] = PolyArea(polix, poliy)                                            # Area computation.

    for i in np.arange(m):                                                          # For each of the nodes.
        er = er + area[i]*(u_ap[i] - u_ex[i])**2                                    # Mean square error computation.

    er = np.sqrt(er)                                                                # The square root is computed.
    
    return er