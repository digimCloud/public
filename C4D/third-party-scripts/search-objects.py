# taken from https://www.c4dcafe.com/ipb/forums/topic/94974-how-to-select-tag-in-c4d-using-python/

import c4d
from c4d import gui
#Welcome to the world of Python


def main():
    name = "cube"
    if doc.SearchObject(name)==None:
     return
    else :
        obj = doc.SearchObject(name) #defines the obj which i cube. OK
        dis = obj.GetTag(c4d.Tdisplay)#defines the tag which is display.OK
        doc.SetActiveTag(dis,mode=c4d.SELECTION_NEW)#Selects tag. OK
        dis[c4d.DISPLAYTAG_SDISPLAYMODE]=2# How do I enable the Use button? In level of detail it is automatically enabled.
        dis[c4d.DISPLAYTAG_WDISPLAYMODE]=1#
        dis[c4d.DISPLAYTAG_AFFECT_LEVELOFDETAIL]=80 #Gives me an error: invalid cross-threadcall. I searched for the c4d.utils if there is an option to translate a number to percentage but I can't seem to find any.
        dis[c4d.DISPLAYTAG_AFFECT_BACKFACECULLING]=TRUE # I was under the impression that boolean only takes True or False. correct me if I'm wrong but this Gives me an error:TRUE is not defined.  
        c4d.CallButton(dis,c4d.ONION_CALCULATE)#Calculates the cache. OK
        
       
    c4d.EventAdd()

if __name__=='__main__':
    main()
