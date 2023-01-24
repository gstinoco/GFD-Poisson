# GFD-Poisson
Generalized Finite Differences Methods for numerically solve Poisson Equation on highly irregular regions.

All the codes are distributed under MIT License on [GitHub](https://github.com/gstinoco/GFD-Poisson) and are free to use, modify, and distribute giving the proper copyright notice.

![Approximate and Theoretical solutions of the problem on ENG region](/Results/Clouds/ENG_3.png)

## Description :memo:
This repository proposes a way to make an approximation to the Poisson Equation in two dimensions over regions that can range from regular (CUA) to highly irregular (ENG).

For this, the proposed solution uses a Generalized Finite Differences Method for the numerical solution over all the regions on:<br>
1. Logically Rectangular Meshes.
2. Triangulations.
3. Irregular clouds of points.

![CUI region](/Notebook_Figures/fig01.png)
![CUI region, structured mesh](/Notebook_Figures/fig02.png)
![CUI region, triangulation](/Notebook_Figures/fig03.png)
![CUI region, cloud of points](/Notebook_Figures/fig04.png)

It is possible to find all test data in the "Data" folder and some sample results in the "Results" folder.

## Researchers :scientist:
All the codes presented were developed by:
    
  - Dr. Gerardo Tinoco Guerrero<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    gerardo.tinoco@umich.mx<br>
    https://orcid.org/0000-0003-3119-770X

  - Dr. Francisco Javier Domínguez Mota<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    francisco.mota@umich.mx<br>
    https://orcid.org/0000-0001-6837-172X
  
  - Dr. José Gerardo Tinoco Ruiz<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    jose.gerardo.tinoco@umich.mx<br>
    https://orcid.org/0000-0002-0866-4798

  - Dr. José Alberto Guzmán Torres<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    jose.alberto.guzman@umich.mx<br>
    https://orcid.org/0000-0002-9309-9390

## Details :books:
More details on the Methods presented in these codes can be found in the following [Jupyter Notebook](Poisson_2D.ipynb)
  

## Funding :dollar:
With the financing of:

  - National Council of Science and Technology, CONACyT (Consejo Nacional de Ciencia y Tecnología, CONACyT), México.
  
  - Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH), México.
  
  - Aula CIMNE-Morelia, México.
