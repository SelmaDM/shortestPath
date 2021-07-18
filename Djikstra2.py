# -*- coding: utf-8 -*-


import math
from os import times
from tkinter import Tk, Canvas
import time


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
#longeur des arcs successeurs
Long_Arc_Succ = [[]for j in range (NbSommets)]
Prec = [[] for j in range(NbSommets)]
Num_Arc_Prec= [[] for j in range(NbSommets)]

for u in range(0,NbArcs):
    orig = Origine[u]
    dest = Destination[u]
    Succ[orig].append(dest)
    Prec[dest].append(orig)
    Num_Arc_Prec[dest].append(u)
    Long_Arc_Succ[orig].append(Longueur[u])

#Q1.1

composantes_connexes = [[]]
Nb_composantes_connexes = 0

              



#nombre max composantes connexes 
NbMax_composantes_connexe = max(len(Nb_composantes_connexes))+1


########################################################
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
sommet_destination = 22279
time_start = time.time()
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
    ind_i= Succ[sommet_depart].index(i)
    pi[i] = Long_Arc_Succ[sommet_depart][ind_i]
    LePere[i] = sommet_depart

nb_sommets_explores = 0
fini = False

candidat=Succ[sommet_depart]        

while (nb_sommets_explores < NbSommets and not fini):
    minPi = math.inf
    #sommet_retenu = -1
    for j in candidat:
        if(Piprime[j]== math.inf and pi[j] < minPi):
            sommet_retenu = j
            minPi = pi[j]
    marque[sommet_retenu] = 1
    Piprime[sommet_retenu] = pi[sommet_retenu]
    TraceCercle(sommet_retenu,'yellow',1)
    if (sommet_retenu == sommet_destination):
        fini = True
    for k in Succ[sommet_retenu]:
        indxk = Succ[sommet_retenu].index(k)
        if(pi[k] >= pi[sommet_retenu] + Long_Arc_Succ[sommet_retenu][indxk]):
           pi[k]   = pi[sommet_retenu] + Long_Arc_Succ[sommet_retenu][indxk]
           LePere[k] = sommet_retenu
           if k not in candidat: candidat.append(k)
   
#on part du sommet destination et on remonte jusqu'au sommet premier sommet et on afffiche le pere de k
#on part du sommet destination

k= sommet_destination
#Fonction met à jour les successeurs de k
while(k is not sommet_depart):
    k = LePere[k]
    TraceCercle(k,'maroon',2)

time_end = time.time()
print(time_end - time_start)
fen.mainloop()



