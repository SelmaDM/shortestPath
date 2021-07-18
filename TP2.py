
fichier_arcs = 'graphe_tp2.txt'
LesArcs = open(fichier_arcs,"r")
Touslesarcs = LesArcs.readlines()
LesArcs.close()

Origine = []
Destination = []

for un_arc in Touslesarcs:
    cet_arc = un_arc.split("\t")
    Orig = int (cet_arc[0])
    Origine.append(Orig)
    Dest = int(cet_arc[1].strip("\n"))
    Destination.append(Dest)

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

#exo 2 parcours 

def insert_debut(liste,j):
   liste.insert(0,j) 

def insert_fin(liste,j):
    liste.append(j)

parcours = 'Profondeur' # 'Largeur'
Liste_sommets = []   
Marque = [False for j in range (NbSommets)] 
Dans_Liste =[False for j in range (NbSommets)]
Liste_sommets.append(0)
Marque[0]= Dans_Liste[0]=True
while Liste_sommets!=[]:
    k= Liste_sommets.pop(0)
    print(k)
    Marque[k]= True
    for l in Succ[k]:
        if not Marque[l] and not Dans_Liste[l]:
            if parcours =='Profondeur': 
                 insert_debut(Liste_sommets,l)
            else : insert_fin(Liste_sommets,l)
            Dans_Liste[l]=True


""" fonction chercher chemin dans un graphe
def cherche_chemin(i,j):
    P = []
    Liste_sommets = []
    Marque = [False for j in range(nbSommets)]
    Dans_Liste = [False for j in range(nbSommets)]
    Liste_sommets.append(0)
    Marque[0] = True
    Dans_liste[0] = True
    trouve = false
    while Liste_sommets and trouve:
        f = Liste_sommets.pop(0)
        Marque [f] = True
        if f ==j:
            trouve = true
            for l in successeurs[f]:
                if not Marque[l] and not Dans_liste[l]:
                    insere_debut(Liste_sommets,l)
                    Dans_liste[l] = True
                    p[l]=f
                    trouve = true
            Return trouve
"""
