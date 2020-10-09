# export selected objects to new C4D files
# Stanislav Szkandera, Digital Media
# www.cinema4d.cz

import c4d
import os
from c4d import gui

#*************************
#       USER SETUP       *
#*************************

#název exportní složky, která bude standardně umístěna uvnitř složky s původním c4d souborem
# pokud chcete exportovat přímo do složky s původním souborem, nechte zázev "".  
exportFolderName = "export" 




def main():

    c4d.CallCommand(12305, 12305) # Show Console...
    c4d.CallCommand(13957); # Clear console

    docOrig = c4d.documents.GetActiveDocument()
    selected = docOrig.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    savePath = docOrig.GetDocumentPath()
    
    if exportFolderName != "":
        path_savePath = os.path.join(savePath, exportFolderName) 
        if not os.path.exists(path_savePath):
            os.makedirs(path_savePath)

    if not selected:
        print("Nebyl vybrán žádný objekt. Vyberte alespoň jeden objekt a zkuste to znovu.")
        return

    objNames = []
    objDuplicateNames = []

    for obj in selected:

        fileBaseName = obj.GetName()
        if fileBaseName in objNames:
            print("POZOR! Objekt s názvem " + fileBaseName + " již byl exportován.")
            objDuplicateNames.append(fileBaseName)
        else:
            objNames.append(fileBaseName)
            tempDoc = c4d.documents.IsolateObjects(docOrig, [obj])
            path_file =  os.path.join(path_savePath, fileBaseName + ".c4d")
            c4d.documents.SaveDocument(tempDoc, path_file, c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT)
            c4d.EventAdd
    
            
    print("\nEXPORT JOB FINISHED")
    print("*******************")
    print("vyexportováno " + str(len(objNames)) + " souborů")
    print("nalezeno " + str(len(objDuplicateNames)) + " duplicitních názvů ")



# Execute main()
if __name__=='__main__':
    main()
