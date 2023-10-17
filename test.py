#nom = "Enzo";

# nom = input("Quels es votre nom ?  je")
# age = "330c"


# try:
#     age_prochain = int(age) + 1
# except ValueError:
#     print("ENTRER UN NOMBRE")
# else:
#   print("je sui "+str(age_prochain))  

# mot_passe = ""

# while not mot_passe == "ENZO":
#     mot_passe = input("DOnner votre mot de passe ") 

# n=0
# while n<5:
#     print("valeur "+ str(n))
#     n = n +1

# age = 0

# while age == 0 :
#     age_str = input("votre age svp ")
#     try:
#         age = int(age_str)
#     except:
#         print("l'age : c 'est en nombre ")



# def demandeName():
#     name = ""
#     while  name == "":
#         name = input("Donnez moi votre nom ? ... ") 
#     return name

# print("Bienvenue "+demandeName())

# age = 30;

# def globalVariable():
#     global age;
#     age = age + 3

# globalVariable()

# print(age)

# age = 1
# if age >= 18:
#     print("MAJEUR")
# elif age == 17:
#     print("PRESQUE MAJEUR")
# elif age == 2 or age == 1 :
#     print("Nouveau nne")
# elif age < 12 :
#     print("ENFANT")
# elif age >= 12  and age < 17:
#     print("ADOLESCENT")
# else:
#     print("MINEUR")

# for i in range(0, 5):
#     print(i)

# age = 30;
# nom = "Rakoto";

# print(f"votre nom est {nom} et votre age est {age}")
# print("votre nom est "+ nom + " et votre age est "+ str(age))
# print("votre nom est %s et votre age est %s" % (nom,age)) 

#------------------------NOMBRE MAGIQUE------------------------------------
#Nombre magiquye
# import random
# NOMBRE_MIN = 1
# NOMBRE_MAX = 10
# NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
# NOMBRE_VIE = 4

# def demander_nombre(nb_min , nb_max):
#     test = True
#     while test :
#         nbr = input("veuillez entrez entre (%s et %s) ....  " %(nb_min,nb_max))
#         try:
#             nbr = int(nbr)
#             test = True
#         except:
#             print("Veuillez entrer un nombre s'il vous plais!  ")
#         else:
#             test = False
#             nbr_test = int(nbr)
#             if nbr_test < 1  or nbr_test > 10 :
#                 print("le nombre doit etre entre 1 et 10, Reesssayer ! ")
#                 test = True


#     return nbr

# def test_magique(NOMBRE_MIN , NOMBRE_MAX , nb_magique, vie):
#     nb_vie =  vie
#     nb_saisie = 0
#     while nb_vie > 0 and nb_saisie != nb_magique :
#         print(f"il vous reste {nb_vie} de vie !")
#         nb_saisie = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
#         if nb_saisie == nb_magique :
#             print("Bravo, vous avez gagné")
#         elif nb_saisie < nb_magique : 
#             print("le nombre magique est plus petit")
#             nb_vie -= 1
#         else:
#             print("le nombre magique est plus grand")
#             nb_vie -= 1
#     if(nb_vie == 0):
#         print(f"Vous avez perdu , le nombre exacte etait de {nb_magique}")        



# test_magique(NOMBRE_MIN , NOMBRE_MAX , NOMBRE_MAGIQUE, NOMBRE_VIE)

#-----------------CALCUT MATHEMATIQUE-----------------------------------

# import random
# NOMBRE_MIN = 1
# NOMBRE_MAX = 10
# NOMBRE_QUESTION =4

# def poser_question():
#     iteration = NOMBRE_QUESTION
#     bonne_reponse = 0
#     for i in range(0,iteration):
#         print()
#         print(f"Question n° {i+1}")
#         a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
#         b = random.randint(NOMBRE_MIN,NOMBRE_MAX)
#         operateur  = random.randint(0,1)

#         operateur_str = '+'
#         calcul = a+b
#         if operateur == 1:
#             operateur_str = "*"
#             calcul = a*b


#         nombre = input(f"{a} {operateur_str} {b} =  ")
#         nombre = int(nombre)

#         if nombre == calcul :
#             print("votre reponse est correcte")

#             bonne_reponse += 1
#         else:
#             print("votre reponse est incorrecte") 
    
#     return bonne_reponse

# reponse = poser_question()
# print()
# print(f"votre notes est de {reponse}/{NOMBRE_QUESTION}")

# moyenne = int(NOMBRE_QUESTION/2)
# if(reponse == 0):
#     print("Revisez vos math! ")
# elif NOMBRE_QUESTION == reponse :
#     print("Vous etes bon en mathemantique")
# elif moyenne < reponse:
#     print("Pas mal")
# elif moyenne > reponse:
#     print("Peut mieux faire")


#-----------------------


# def test(fe):
#     return fe,'ko'

# ko  = test('fe')

# print('ko',ko)


# def afficher_table_de_multiplication(n,min=1,max=10):
#     if min>max:
#         print("erreur min max")
#         return
#     for i in range(min , max+1):
#         print(f"{i} * {n} = {i*n}")

# afficher_table_de_multiplication(6,50,13)


#fonction call back
# def a(a,b):
#     return a*b

# c = a

# print(c) # ne retourne rien , il dit que c'est simplement un fonction
# print(c(1,5)) #si on met u n paramettre ou parenthese alors il va retourner


# def table_multiplication(n, str_operateur, callback_function):
#     for i in range(1,10):
#         print(i,str_operateur,n, " = ", callback_function(i, n))

# def addition(a,b):
#     return a+b

# def multiplication(a,b):
#     return a*b 

# def puissance(a,b):
#     return pow(a,b)

# table_multiplication(4 , '+', lambda a , b : a+b)
# print()
# table_multiplication(4 , '*', lambda a,b : a*b)
# print()
# table_multiplication(4 , '*', lambda a,b : pow(a,b))
# SOMMME

# def somme(**nombres):
#     res=0
#     for i in nombres.values():
#         res +=i
#     return res

# print(somme(a=2,b=5,c=4))

# person = ('Miora','Todisoa','Fabienne','Fabienne2','Avana','Mbola','Nadya','boska','Hasina','Hasina2','Ranto','Felana','Mampionina','Tana','Nandrianina','Patsy','Princia','Lova','Sarah','Kanto');

# print(len(person)) #17

# print(len("princia")) #7

# print(person[0]) #afficher le premier element

# print(person[-1]) #afficher le dernier element

# print(person[-2]) #afficher avant dernier

# for i in range(0 , len(person)):
#     print(person[i])

# for i in person:
#     print(i)


# person =["Henintsoa", "Mado" , "Sophie" , "Sariaka"]

# #ajouter
# person.append("ravaka")

# #supprimer
# del person[0]

# #modifier
# person[0]="Olivia"

# #affichage
# for i in person:
#     print(i)

def information():
    return "Lova",50,"Tananarivo"

# print(information())

# info = information()

# print(info[0])
# print(info[1])
# print(info[2])

# nom , age , adresse = information()

# print(nom)
# print(age)
# print(adresse)


def afficherInformation(nom,age,adresse):
    print(f"je m'appelle {nom}, j'ai {age}, j'habite a {adresse}")
    
info = information()
afficherInformation(*info)





        












