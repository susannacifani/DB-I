import copy

def chiusura(R, F, X):
    F_copy = copy.deepcopy(F)
    X = set(X)
    
    Z = X
    S = set()
    added = False
    
    # caricamento di S all'inizio
    # scorro il dizionario contenente le dipendenze funzionali
    for left_side in list(F):
        # se la parte sinistra è un sottoinsieme di X
        # allora vado a vedere le parti destre e me le salvo in S 
        if set(left_side).issubset(set(X)):
            for el in F_copy[left_side]:
                S.add(el)
                added = True
            F_copy.pop(left_side)
    
    
    # se ho aggiunto qualcosa di nuovo continuo
    while (added):
        added = False
        Z = Z.union(S)
        for left_side in list(F_copy):
            
        # se la parte sinistra è un sottoinsieme di S
            # allora vado a vedere le parti destre e me le salvo in S 
            
            # nel caso di dipendenze composte
            arr_left = []
            for v in left_side:
                arr_left.append(v)
            
            
            if set(arr_left).issubset(set(Z)) and len(set(arr_left)) != 0:
                for el in F_copy[left_side]:    # ogni elemento a destra lo aggiungo in F
                    S.add(el)
                    added = True
                F_copy.pop(left_side)   # cancello da F_Copy, cosi non lo devo riesaminare la prossima volta
    
    print(sorted(list(Z)))
    return sorted(list(Z))
            
   
    
chiusura("ABCDE", {"A":"BC",
                   "B":"D",
                   "C":"E",
                   "D":"A",
                   "E":"A"},
         "E")
# =============================================================================
# chiusura("ABCDEH", {"A" : "B",
#                     "A" : "C",
#                     "D" : "E",
#                     "CD" : "E",
#                     "CD" : "H"},
#          "A")     
# =============================================================================
   
    
   
    
   
# =============================================================================
# chiusura("ABCDEHL", {"AB" : "C",
#                      "B" : "D",
#                      "AD" : "E",
#                      "CE" : "H"},
#          "AB")            
# =============================================================================
      
        
      
        
# chiusura("ABCDEH", 
#          {"AB" : "CD",
#           "EH" : "D",
#           "D" : "H"}, 
#          "AB")   
            
    
# =============================================================================
# chiusura("ABCDEH", 
#          {"AB" : "CD",
#           "EH" : "D",
#           "D" : "H"}, 
#          "D")
# DH
# =============================================================================
        
        
