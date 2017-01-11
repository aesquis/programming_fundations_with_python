import os

#Definint la variable del directori proporcionem la ruta on volem modificar el fitxers
dirName = ("C:\OOP")

#definim la funcio rename_file
def rename_files():
    #(1) get file names from a folder
   file_list = os.listdir(dirName) #guardem en la variable file_list el llistat d'arxius
   print(file_list) #Mostrem el llistat
   os.chdir(dirName) #canviem la carpeta actual per la de la variable dirName
   saved_path = os.getcwd() #definim la variable saved_path i hi guardem la ruta que acabem de modificar
   print ("Current Working Directory is "+saved_path) #Mostrem la carpeta on estem

    #(2) for each file, rename filename
   for file_name in file_list:  #Fem el loop per els fitxers guardats en la variable file_list
       print("Old Name was " +file_name) #Mostrem nom de arxiu actual
       #Mostrem nom del resultant, amb la funció file_name.translate eliminem el numeros
       print("New name is going to be " +file_name.translate(None, "0123456789"))
       os.rename(file_name, file_name.translate(None, "0123456789")) #renombrem l'arxiu
   os.chdir(saved_path) #tornem a canviar e directori

rename_files() #Cridem la funcio
