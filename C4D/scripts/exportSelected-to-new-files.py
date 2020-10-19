# export selected objects to new C4D files
# Stanislav Szkandera, Digital Media
# standa@digitalmedia.cz
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
createXRefs = True # True/False. If True, replaces exported objects with XRefs in original document
saveXrefDocAsSeparateFile = True # If False, replaces original C4D file with modified file including Xrefs.




def main():

    c4d.CallCommand(12305, 12305) # Show Console...
    c4d.CallCommand(13957); # Clear console

    docOrig = c4d.documents.GetActiveDocument()
    selected = docOrig.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    origSavePath = docOrig.GetDocumentPath()
    docName = docOrig.GetDocumentName()
    docName,ext = os.path.splitext(docName)
    if createXRefs and saveXrefDocAsSeparateFile:
        docName = docName + "_xrefs"


    if exportFolderName != "":
        path_savePath = os.path.join(origSavePath, exportFolderName)
        if not os.path.exists(path_savePath):
            os.makedirs(path_savePath)
    else:
        path_savePath = origSavePath

    if not selected:
        msg = "Nebyl vybrán žádný objekt. Vyberte alespoň jeden objekt a zkuste to znovu."
        gui.MessageDialog(msg)
        print(msg)
        print("*** SKRIPT BYL UKONČEN ***")
        return


    objDict = {}
    duplIndex = 0
    rename = False

    for obj in selected:
        fileBaseName = obj.GetName()

        if fileBaseName in objDict:
            duplIndex = objDict[fileBaseName] + 1
            objDict[fileBaseName] = duplIndex
            rename = True
        else:
            objDict[fileBaseName] = 0
            rename = False

        if (exportFolderName == "") and (fileBaseName == docName) and (saveXrefDocAsSeparateFile):
            rename = True

        if rename:
            fileBaseName = fileBaseName + str(objDict[fileBaseName])

        tempDoc = c4d.documents.IsolateObjects(docOrig, [obj])
        path_file =  os.path.join(path_savePath, fileBaseName + ".c4d")
        c4d.documents.SaveDocument(tempDoc, path_file, c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT)

        if createXRefs:
            #print("saving xref %s" %(fileBaseName))
            op = c4d.BaseObject(c4d.Oxref)
            docOrig.InsertObject(op)
            op.SetParameter(c4d.ID_CA_XREF_FILE, path_file, c4d.DESCFLAGS_SET_USERINTERACTION)
            op.SetName(fileBaseName)
            obj.Remove()
            c4d.EventAdd()


    savePath = os.path.join(origSavePath, docName + ".c4d")
    #print(savePath)
    c4d.documents.SaveDocument(docOrig, savePath, c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT)


    print("\nEXPORT JOB FINISHED")
    print("*******************************")
    print("vyexportováno souborů: " + str(len(selected)))






# Execute main()
if __name__=='__main__':
    main()
