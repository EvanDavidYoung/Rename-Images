import os
cwd = os.getcwd()

for i, filename in enumerate(sorted(os.listdir(cwd))):
    print(cwd+'/'+filename)
    if filename[-4:]==".jpg":
        os.rename(cwd +'/'+ filename, cwd +'/'+str(i) + ".jpg")
