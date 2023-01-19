# All the codes presented below were developed by:
#   Dr. Gerardo Tinoco Guerrero
#   Universidad Michoacana de San Nicolás de Hidalgo
#   gerardo.tinoco@umich.mx
#
# With the funding of:
#   National Council of Science and Technology, CONACyT (Consejo Nacional de Ciencia y Tecnología, CONACyT). México.
#   Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH). México
#   Aula CIMNE Morelia. México
#
# Date:
#   January, 2023.
#
# Last Modification:
#   January, 2023.

import math
from scipy.io import loadmat
import Errors
import Graph
import Poisson_2D

# Region data is loaded.
# Triangulation or unstructured cloud of points to work in.

regiones = ['CAB','CHA','CUAD','CUIT','CURVA','DOWN','ELE','ENG','GIBR','HA','HAB','MI','MIC','MID','PATZ','SWA','TERRA','TRAP','UC','UCH','UP','ZIRA']
#regiones = ['MIC','MID','PATZ','SWA','TERRA','TRAP','UC','UCH','UP','ZIRA']
sizes = ['1', '2', '3', '4']

for reg in regiones:
    region = reg

    for me in sizes:
        cloud = me

        # All data is loaded from the file
        mat  = loadmat('Data/Clouds/' + region + '_' + cloud + '.mat')
        nomc = 'Results/Clouds/' + region + '_' + cloud + '.png'

        # Node data is saved
        p   = mat['p']
        pb  = mat['pb']
        vec = mat['vec']
        tt  = mat['t']
        if tt.min() == 1:
            tt -= 1

        # Boundary conditions
        # The boundary conditions are defined as
        #   \phi = 2e^{2x+y}
        #
        #   f = 10e^{2x+y}

        def phi(x,y):
            fun = 2*math.exp(2*x+y)
            return fun

        def f(x,y):
            fun = 10*math.exp(2*x+y)
            return fun

        # Poisson 2D computed in an unstructured cloud of points
        phi_ap, phi_ex, vec = Poisson_2D.Cloud(p, pb, phi, f)
        er = Errors.Cloud_Static(p, vec, phi_ap, phi_ex)
        print('The mean square error in the unstructured cloud of points', region, 'with size', cloud, 'is: ', er)
        Graph.Cloud_Static_sav(p, tt, phi_ap, phi_ex, nomc)