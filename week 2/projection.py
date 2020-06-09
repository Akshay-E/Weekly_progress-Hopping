import matplotlib.pyplot as plt
import numpy as np

with open('hygdata_v3.csv','r') as f:
    lines=f.read().split('\n')
    
data=[]
for i in lines[1:-1]:
    data.append(i.split(','))
    
print(len(data))
print(float(data[0][7]))
    
ra=[float(data[i][7]) for i in range(len(data)-1)]
dec=[float(data[i][8]) for i in range(len(data)-1)]
mag=[float(data[i][14]) for i in range(len(data)-1)]
 
print(ra[0])

plt.style.use(['dark_background']) # For dark background
fig1 = plt.figure(figsize=(20,12))
fig1.suptitle('Mollweide projection of stars in sky (PART 1)', fontsize=30)

# projection='mollweide' makes a Molleweide projection
ax1 = fig1.add_subplot(221, projection='mollweide')
































































































ax1.scatter(ra, dec, c='white',s=.5)