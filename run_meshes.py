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
#   January, 2023.
#
# Last Modification:
#   January, 2023.

import numpy as np
from scipy.io import loadmat
import Scripts.Errors as Errors
import Scripts.Graph as Graph
import Poisson_2D

# Region data is loaded.

regions = ['CAB','CUA','CUI','DOW','ENG','GIB','HAB','MIC','PAT','ZIR']
sizes = ['21', '41','81']

for reg in regions:
    region = reg

    for me in sizes:
        mesh = me

        # All data is loaded from the file
        mat  = loadmat('Data/Meshes/' + region + mesh + '.mat')
        nomm = 'Results/Meshes/' + region + mesh + '.png'

        # Node data is saved
        x  = mat['x']
        y  = mat['y']

        # Boundary conditions
        # The boundary conditions are defined as
        #   \phi = 2e^{2x+y}
        #
        #   f = 10e^{2x+y}

        def phi(x,y):
            fun = 2*np.exp(2*x+y)
            return fun

        def f(x,y):
            fun = 10*np.exp(2*x+y)
            return fun

        # Poisson 2D computed in a logically rectangular mesh
        phi_ap, phi_ex = Poisson_2D.Mesh(x, y, phi, f)
        er = Errors.Mesh_Static(x, y, phi_ap, phi_ex)
        print('The mean square error in the mesh', region, 'with', mesh, 'points per side is: ', er)
        #Graph.Mesh_Static_sav(x, y, phi_ap, phi_ex, nomm)
        Graph.Mesh_Static(x, y, phi_ap, phi_ex)