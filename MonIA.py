import re

print("--------MON IA FITEC---------")



def SearchOp(chaine, flag = 0): ## prend en param une chaine de caractére, analyse l'operation via un mot clé et retourne le résultat
    if re.search('somme', chaine, flag)is not None:
        op = re.findall('\d{1,}',chaine, flag)
        r = 0
        for i in op :
            i=int(i)
            r += i
        return r
    if re.search('soustraction', chaine, flag)is not None:
        op = re.findall('\d{1,}',chaine, flag)
        r = int(op[0])
        for i in range(1, len(op)):
            j = int(op[i])
            r -= j
        return r
    if re.search('multiplication', chaine, flag)is not None:
        op = re.findall('\d{1,}',chaine, flag)
        r = int(op[0])
        for i in range(1, len(op)):
            j = int(op[i])
            r *= j
        return r
    if re.search('division', chaine, flag)is not None:
        op = re.findall('\d{1,}',chaine, flag)
        while len(op)>2:
            chaine = input("Trop d'opérations pour une division. Recommencez svp :   ")
            op = re.findall('\d{1,}',chaine, flag)
        r = int(op[0])
        for i in range(1, len(op)):
            j = int(op[i])
            try:
                r /= j
            except ZeroDivisionError:
                while j == 0 :
                    j = int(input("Division par zéro interdite ! Entrez un autre nombre svp:   "))
                r /= j
        return int(r)    

def SearchMe(chaine, flag = 0):
    if re.search('(aire){1}(.)*(carre){1}', chaine, flag) is not None:
        if re.search('cot+e', chaine, flag)is not None:
            l = re.findall('\d{1,}',chaine, flag)
            cot = int(l[0])
            aire = cot **2
            return print("aire = "+str(aire))
        else :
            cot = int(input("longueur cote ?"))
            aire = cot**2
            return print("aire = "+str(aire))
    if re.search('(aire){1}(.)*(rectangle){1}', chaine, flag) is not None:
        if re.search('(largeur){1}(.)*(longueur){1}', chaine, flag)is not None:
            l = re.findall('\d{1,}',chaine, flag)
            cot1 = int(l[0])
            cot2 = int(l[1])
            aire = cot1 * cot2
            return print("aire = "+str(aire))
        else :
            cot1 = int(input("longueur ?   "))
            cot2 = int(input("largeur ?   "))
            aire = cot1 * cot2
            return print("aire = "+str(aire))
    else :
        print("echec")
        
    

def AnalyseChaine(chaine):## Analyse la demande initiale de l'utilisateur en lancant un calcul mathématique ou un calcul de géométrie
    if re.search('calcul', chaine)is not None :
        chaineOp = input("Dites moi un calcul sous la forme : somme de <a> et <b> :     ")
        return print(SearchOp(chaineOp))
    if re.search('mesure', chaine)is not None :
        chaineMe = input("Demandez moi une mesure sous la forme : je veux mesurer l'aire de mon carre de cote 5 :     ")
        return SearchMe(chaineMe)

        
print("Bonjour ! je suis votre systéme de calcul pas trés intelligent.")
print("Pour l\'instant, je prend en charge les calculs simple et la géométrie des carre et des rectangles.\n\n")
print("Je peux faire :\nDes calculs d'aire\nDes additions\nDes soustractions\nDes multiplications\nEt des Divisions")
maChaine = input("\n\nVoulez vous faire des calculs ou des operations sur les mesures ?")
AnalyseChaine(maChaine)

    
    
print("-------FIN PROGRAMME-------")
