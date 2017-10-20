

config=open('running-config.cfg','r')
newconfig=open('newfile.cfg','w')
f1 = open('text.cfg','w')
for line in config:
   newconfig.write(line.replace('172','192'))

list=[] 
for line in config:
  if 'access-list' in line:
    print(line)
    f.write(line)  

config.close()

