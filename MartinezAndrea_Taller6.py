########### Punto 2 ########
#Paquetes Basicos------------------------------
import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt

#Para el manejo de algebra lineal---------------
from numpy.linalg import *
from scipy.linalg import expm,inv

#Para los plots 3D -----------------------------
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


N=1000

x=uniform(0,9,N)
ruido=uniform(-2,2,N)#+np.sin(x1)
y=x+ruido*np.exp(-0.1*(x-5)**2)
z=x+y+uniform(-3,3,N)*np.exp(0.05*(-(x-np.mean(x))**2-(y-np.mean(y))**2))
######### Punto 3 #######
promx=(x-np.mean(x))/(np.sqrt(np.var(x)))
promy=(y-np.mean(y))/(np.sqrt(np.var(y)))
promz=(z-np.mean(z))/(np.sqrt(np.var(z)))

px=np.mean(promx)
py=np.mean(promy)
pz=np.mean(promz)
vx=np.var(promx)
vy=np.var(promy)
vz=np.var(promz)
print px,py,pz,vx,vy,vz
###### punto 4 ######
datos=np.array([promx,promy,promz])
covA=np.cov(datos)

print covA
###### punto 5 ######
vecpro=np.linalg.eig(covA)
print vecpro
###### punto 6 #######

