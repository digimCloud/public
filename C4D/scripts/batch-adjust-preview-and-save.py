# export selected objects to new C4D files
# Stanislav Szkandera, Digital Media
# standa@digitalmedia.cz
# www.cinema4d.cz


import c4d
from c4d import gui
import os


# ****************************************
#         USER SETUP
# ****************************************

# Open files with following extension only
# for multiple extensions use this format
# allowedExt = ['.c4d', '.fbx', '.obj', '.lwo', '.3ds', '.dxf']
#*****************************************************
allowedExt = ['.c4d']
# ****************************************************






def main():
    c4d.CallCommand(12305, 12305) # Show Console...
    c4d.CallCommand(13957); # Clear console

    path=c4d.storage.LoadDialog(c4d.FILESELECTTYPE_SCENES, "Please choose a folder", c4d.FILESELECT_DIRECTORY)
    if not path: return

    dirList=os.listdir(path)


    arr_files = []
    for fname in dirList:
        fname_name, fname_extension = os.path.splitext(fname)

        if fname_extension.lower() in allowedExt:

            fpath = os.path.join (path, fname)
            flags_load = c4d.SCENEFILTER_OBJECTS | c4d.SCENEFILTER_MATERIALS | c4d.SCENEFILTER_SAVECACHES
            newDoc = c4d.documents.LoadDocument(fpath,flags_load)

            # call internal Cinema 4D commands
            # to display more C4D command calls, go to menu Extension -> Script log and start clicking on different commands in C4D menus
            # copy/paste command call to the block below
            c4d.CallCommand(100004766) # Select All
            c4d.CallCommand(12151) # Frame Selected Objects
            c4d.CallCommand(18194) # Geometry Only
            # END of block
            
            
            c4d.EventAdd
            c4d.CallCommand(12098) # Save Project
            c4d.CallCommand(12664) # Close Project
        
            #flags_save = c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST | c4d.SAVEDOCUMENTFLAGS_SAVECACHES
            #c4d.documents.SaveDocument(newDoc,fpath,flags_save,c4d.FORMAT_C4DEXPORT)

            arr_files.append(fname_name+fname_extension)
            print("Saving file " + str(fname))

            #c4d.documents.KillDocument(newDoc)

    lenFiles = len(arr_files)
    if lenFiles>0:
        print("\n  GOOD JOB! ")
        print("**************")
        print(str(lenFiles) + " file(s) have been resaved with preview.")
    else:
        extToStr = ','.join([str(elem) for elem in allowedExt])
        print("\n  WARNING!")
        print("**************")
        print("No files with extension(s) " + extToStr + " have been found in folder " + str(path))

# Execute main()
if __name__=='__main__':
    main()
