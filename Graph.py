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
#   November, 2022.
#
# Last Modification:
#   December, 2022.

# Graphics
# Some routines are defined in here in order to correctly Graph different kinds of results.

import matplotlib.pyplot as plt
from matplotlib import cm

def Mesh_Static(x, y, u_ap, u_ex):
    min  = u_ex.min()
    max  = u_ex.max()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={"projection": "3d"}, figsize=(8, 4))
    
    ax1.set_title('Approximation')
    ax1.set_zlim([min, max])
    ax1.plot_surface(x, y, u_ap, cmap=cm.coolwarm)
    
    ax2.set_title('Theoretical Solution')
    ax2.set_zlim([min, max])
    ax2.plot_surface(x, y, u_ex, cmap=cm.coolwarm)

    plt.show()

def Cloud_Static(p, tt, u_ap, u_ex):
    if tt.min() == 1:
        tt -= 1
    
    min  = u_ex.min()
    max  = u_ex.max()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    
    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:], triangles=tt, cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:], triangles=tt, cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')

    plt.show()

def Mesh_Static_sav(x, y, u_ap, u_ex, nom):
    min  = u_ex.min()
    max  = u_ex.max()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={"projection": "3d"}, figsize=(16, 8))
    
    ax1.set_title('Approximation')
    ax1.set_zlim([min, max])
    ax1.plot_surface(x, y, u_ap, cmap=cm.coolwarm)
    
    ax2.set_title('Theoretical Solution')
    ax2.set_zlim([min, max])
    ax2.plot_surface(x, y, u_ex, cmap=cm.coolwarm)

    plt.savefig(nom)

def Cloud_Static_sav(p, tt, u_ap, u_ex, nom):
    if tt.min() == 1:
        tt -= 1
    
    min  = u_ex.min()
    max  = u_ex.max()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(16, 8))
    
    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:], triangles=tt, cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:], triangles=tt, cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')

    plt.savefig(nom)