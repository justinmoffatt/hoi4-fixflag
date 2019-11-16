import os

dir = "/home/justin/.steam/steam/steamapps/common/Hearts of Iron IV/gfx/flags"
dirs = [dir+"/", dir+"/small/", dir+"/medium/"]

for currentdir in dirs:
        for file in os.listdir(currentdir):
                if "unified" in file:
                        sliceat = file.rfind("_")
                        newname = file[:sliceat].upper() + file[sliceat:]
                        #print(newname)
                        os.rename(currentdir+file, currentdir+newname)
