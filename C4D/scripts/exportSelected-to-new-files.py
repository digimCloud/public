# export selected objects to new C4D files
# Stanislav Szkandera, Digital Media 
# www.cinema4d.cz

import c4d
from c4d import gui


def main():
    
    c4d.CallCommand(12305, 12305) # Show Console...
    c4d.CallCommand(13957); # Clear console
    
    docOrig = c4d.documents.GetActiveDocument()
    selected = docOrig.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    
    savePath = docOrig.GetDocumentPath()
    
    if selected == None:
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
        
            newDoc = c4d.documents.BaseDocument() 
            newDoc.SetDocumentName(fileBaseName)
            
            newDoc.InsertObject(obj.GetClone())
            
            saveFile = savePath + "/export/" + fileBaseName + ".c4d"
            c4d.documents.SaveDocument(newDoc, saveFile, c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT)
            c4d.documents.KillDocument(newDoc)

    print("\nEXPORT JOB FINISHED")
    print("*******************")
    print("vyexportováno " + str(len(objNames)) + " souborů")
    print("nalezeno " + str(len(objDuplicateNames)) + " duplicitních názvů ")
        
        
    
# Execute main()
if __name__=='__main__':
    main()
