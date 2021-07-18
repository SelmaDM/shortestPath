import math
from os import times
from tkinter import Tk, Canvas
import time


# Disjkstra V1 non optimisé

Noeuds = 'Noeuds.csv'
Noeuds = open(Noeuds,"r")
Noeuds = Noeuds.readlines()

Longitude = []
Latitude = []


for un_arc in Noeuds:
    cet_arc = un_arc.split("\t")
    num_arc = float (cet_arc[0])
    Long = float(cet_arc[1].strip("\n"))
    longt = Long * math.pi / 180
    Longitude.append(longt)
    Lat = float(cet_arc[2].strip("\n"))
    lat = Lat * math.pi / 180
    Latitude.append(lat)
    
minLat = min(Latitude)
maxLat = max(Latitude)
minLong = min(Longitude)
maxLong = max(Longitude)

# Lecture des données 
Origine = []
Destination = []
Longueur = []
Dangerosité = []


Arcs = 'Arcs.csv'
Arcs = open(Arcs,"r")
Arcs = Arcs.readlines()

for un_arc in Arcs:
    cet_arc = un_arc.split("\t")
    Orig = int (cet_arc[0])
    Origine.append(Orig)
    Dest = int(cet_arc[1].strip("\n"))
    Destination.append(Dest)
    Long = int(cet_arc[2].strip("\n"))
    Longueur.append(Long)
    Dang = int(cet_arc[2].strip("\n"))
    Dangerosité.append(Dang)

NbSommets = max(max(Origine),max(Destination))+1
NbArcs = len(Origine) 

# Costruction des sucesseurs
Succ = [[] for j in range(NbSommets)]
Prec = [[] for j in range(NbSommets)]
Num_Arc_Prec= [[] for j in range(NbSommets)]
for u in range(0,NbArcs):
    orig = Origine[u]
    dest = Destination [u]
    Succ[orig].append(dest)
    Prec[dest].append(orig)
    Num_Arc_Prec[dest].append(u)

# Routine qui renvoie numero Arc 
def Arc(i, j):
    for numero_arc in range(NbArcs):
        if Origine[numero_arc] == i and Destination[numero_arc] == j:
            return numero_arc
val = Arc(1817,6208)
print(val)


# ########################################################
# Dessin du graphe
# ########################################################

print('*****************************************')
print('* Dessin du graphe                      *')
print('*****************************************')

def cercle(x,y,r,couleur):
    can.create_oval(x-r, y-r, x+r, y+r, outline = couleur, fill = couleur)

def TraceCercle(j,couleur,rayon):
    x=(Longitude[j]-minLong)*ratioWidth + border
    y=((Latitude[j]-minLat)*ratioHeight) + border
    y=winHeight-y
    cercle(x,y,rayon,couleur)

fen = Tk()
fen.title('Graphe')
coul = "dark green"   #['purple','cyan','maroon','green','red','blue','orange','yellow']

Delta_Long = maxLong-minLong
Delta_Lat = maxLat-minLat
border = 20         # taille en px des bords
winWidth_int = 800
winWidth = winWidth_int+2*border     # largeur de la fenetre
winHeight_int = 800
winHeight = winHeight_int+2*border     # hauteur de la fenetre : recalculee en fonction de la taille du graphe
#ratio= 1.0          # rapport taille graphe / taille fenetre
ratioWidth = winWidth_int/(maxLong-minLong)       #  rapport largeur graphe/ largeur de la fenetre
ratioHeight = winHeight_int/(maxLat-minLat)       #  rapport hauteur du graphe hauteur de la fenetre

can = Canvas(fen, width = winWidth, height = winHeight, bg ='dark grey')
can.pack(padx=5,pady=5)

#  cercles
rayon = 1               # rayon pour dessin des sommets
rayon_od = 5           # rayon pour sommet origine et destination
# Affichage de tous les sommets
for i in range(0,NbSommets):
    TraceCercle(i,'black',rayon)

sommet_depart = 3000
sommet_destination = 11342

TraceCercle(sommet_depart,'green',rayon_od) #Sommet de départ
TraceCercle(sommet_destination,'red',rayon_od) #Sommet destination

inf = math.inf 
pi = [inf for j in range (NbSommets)] #intialisation d'une liste à l'infini
Piprime = [inf for j in range (NbSommets)]
LePere = [-1 for i in  range (NbSommets)]
marque = [0 for i in  range (NbSommets)]

pi[sommet_depart] = 0
Piprime[sommet_depart] = 0


for i in  Succ[sommet_depart]:
    #Le cout de l'Arc
    pi[i]= Longueur[Arc(sommet_depart,i)]
    LePere[i] = sommet_depart

nb_sommets_explores = 0
fini = False


#Q1.1
time_start = time.time()

composantes_connexes = [[]]
Nb_composantes_connexes = 0

while (nb_sommets_explores < NbSommets and not fini):
    minPi = math.inf

    for j in range(NbSommets):
        m=0
        if(Piprime[j]== math.inf and pi[j] < minPi):
            sommet_retenu = j
            minPi = pi[j]
    marque[sommet_retenu] = 1
    Piprime[sommet_retenu] = pi[sommet_retenu]
    TraceCercle(sommet_retenu,'yellow',1)
    if (sommet_retenu == sommet_destination):
        fini = True
    for k in Succ[sommet_retenu]:
        if(pi[k] >= pi[sommet_retenu]+ Longueur[Arc(sommet_retenu, k)]):
           pi[k] = pi[sommet_retenu]+ Longueur[Arc(sommet_retenu, k)]
           LePere[k] = sommet_retenu
           composantes_connexes.insert(m,k) 
    Nb_composantes_connexes = Nb_composantes_connexes+1
    
print( "Le nombre de sommets qui sont dans la plus grande composante")

print (Nb_composantes_connexes )

#Q2.1 Composante maximale 

taille_composante =[]

taille = len (composantes_connexes)
for k in  composantes_connexes:
    taille1 =0
    for i in range (taille):
        taille1=taille1+1

    taille_composante.append(taille1)

nombre_sommets_maximal = max(taille_composante)
print("nombre sommet maximal")
print(nombre_sommets_maximal)

time_end = time.time()
print("temps de calcul")
print(time_end - time_start)



#on part du sommet destination et on remonte jusqu'au sommet premier sommet et on afffiche le pere de k
#on part du sommet destination
k= sommet_destination
#Fonction met à jour les successeurs de k
while(k is not sommet_depart):
    Arcs = Arc(LePere[k], k)
    k = LePere[k]
    #TraceCercle(k,'maroon',2)

fen.mainloop()



