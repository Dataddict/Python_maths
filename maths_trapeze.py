import numpy as np
import csv
from matplotlib import pyplot as plt
import scipy.integrate as sci

# Read file
def readFile(fil):
    ''' Reading the file '''
    with open(fil, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        lst=[row for row in spamreader]
    print("Nb ligne %d "%(len(lst)))
    return lst

class point(object):
    ''' Class point, two parameters x, y '''
    def __init__(self,x,y): self._x, self._y=x,y
    # Define property
    def _getx( self ): return self._x
    def _setx(self, a): self._x = float(a)
    x = property(_getx, _setx, doc=u"Abscisse")
    def _gety( self ): return self._y
    def _sety(self, a): self._y = float(a)
    y = property(_gety, _sety, doc=u"Ordonnee")
    # Overload some specific method
    def __str__(self): return "("+str(self._x)+","+str(self._y)+")"
    def __lt__(self, other):
        ''' Define lower than on x only '''
        return self._x < other._x
    # Retrieving the coordinates
    def getCOO(self): return np.array([self._x,self._y])
    
def initListPoint(ID):
    ''' Manage datas '''
    lst=readFile("exo001.csv")
    lstPts=[]
    for pts in lst:
        if int(pts[0])==ID:
            lstPts.append(point(float(pts[1]),float(pts[2])))
    print("Nombre de points pour l'ID %d"%(len(lstPts)))
    # Sort directly the object list
    sortLst=sorted(lstPts)
    # Getting back the coordinates
    xx = np.array([pt.x for pt in sortLst])
    yy = np.array([pt.y for pt in sortLst])
    print("Somme des yy %f"%(yy.sum()))
    return xx,yy

def plotF( xx, yy, ID):
    ''' Plot '''
    plt.plot( xx, yy, label=str(ID))
    plt.legend()

def trapeze( xx, yy):
    ''' Integrate '''
    I=((xx[1:]-xx[:-1])*(yy[1:]+yy[:-1])/2.0).sum()
    print("Integrale I=%f"%(I))
    Isc=sci.trapz( yy, xx)
    print("Scipy integrale Isc=%f"%(Isc))
    return I, Isc
    
if __name__=="__main__":
    for ID in range(14):
        print("=====================================> ID %d"%(ID))
        xx, yy = initListPoint(ID)
        plotF(xx, yy, ID)
        trapeze(xx, yy)
    plt.show()
    
