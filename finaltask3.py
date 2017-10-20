

config=open('running-config.cfg','r')
newconfig=open('newfile.cfg','w')
for line in config:
   newconfig.write(line.replace('172','192'))
