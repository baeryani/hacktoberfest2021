import os

newName = []
for i in range(6000):
    newName.append('{0:04}'.format(i))
i = 0
for filename in os.listdir('./slaps'):
    newname = str('./slaps/'+newName[i]+".png")
    filename = str('./slaps/'+filename)
    os.rename(filename, newname)
    i = i+1