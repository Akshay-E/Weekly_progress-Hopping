import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Circle

def telescope(fov,a):
    
    ax1= fig.add_subplot(1,2,a)
    ax1.set_facecolor('k')
    
    # to prevent error occuring while zooming in at the poles 2 conditions r used
    if (dec_in+fov<85 and dec_in-fov>-85):
         m = Basemap(projection = "stere",
            llcrnrlon=ra_in-fov,llcrnrlat=dec_in-fov,
            urcrnrlon=ra_in+fov,urcrnrlat=dec_in+fov,
            resolution = "i",lat_0=dec_in,lon_0=ra_in,
            celestial=True,fix_aspect=False)
         
         m.drawparallels(range(-90,90,1),color='white',labels=[1,1,0,0],dashes=[1,1])
         m.drawmeridians(range(0,360,1),color='white',labels=[0,0,1,1],dashes=[1,1])
         if a==1:
             plt.title('Field of view through eyepiece',pad=30,size=20)
         else:
             plt.title('Field of view through finder scope',pad=30,size=20)
        
         ra_crc=360-ra_in if ra_in>180 else -ra_in 
         dec_crc=dec_in
         x_crc,y_crc=m(ra_crc,dec_crc,inverse=False)
         s1=m(ra_crc,dec_crc)
         s2=m(ra_crc+1,dec_crc)
         r=(s1[0]-s2[0])*(fov/2)
        
         circle = Circle((x_crc, y_crc), r,color='r',fill=False,ls='--',lw=2)
         ax1.add_patch(circle)
    
   
    else:
        
        m = Basemap(width=2000000,height=2000000,projection = "stere",
            lat_0=dec_in,lon_0=ra_in,resolution = "i",celestial=True)
        
        m.drawparallels(range(-90,90,3),color='white',labels=[1,1,0,0],dashes=[1,1])
        m.drawmeridians(range(0,360,10),color='white',labels=[0,0,0,1],dashes=[1,1])
        plt.title('Projection of sky at Pole',pad=30,size=20)
    
    m.drawmapboundary(color='white',linewidth=1.5,fill_color='k')
    
    x1,y1=m(ra_1,dec_1) # converting to coordinates of the projection
    m.scatter(x1,y1,s=300,color='white')
    
    x2,y2=m(ra_2,dec_2)
    m.scatter(x2,y2,s=200,color='white')
    
    x3,y3=m(ra_3,dec_3)
    m.scatter(x3,y3,s=100,color='white')
    
    x4,y4=m(ra_4,dec_4)
    m.scatter(x4,y4,s=50,color='white')
    
    x5,y5=m(ra_5,dec_5)
    m.scatter(x5,y5,s=10,color='white')
    
    x6,y6=m(ra_6,dec_6)
    m.scatter(x6,y6,s=5,color='white',label='stars')
    
    #if condition is added to avoid plotting those stars with V< limiting mag
    if m_lim>=8:  
        x7,y7=m(ra_7,dec_7)
        m.scatter(x7,y7,s=4,color='white')
        
    if m_lim>=10:
        x8,y8=m(ra_8,dec_8)
        m.scatter(x8,y8,s=3,color='white')
    
    if m_lim>=10.5:
        x9,y9=m(ra_9,dec_9)
        m.scatter(x9,y9,s=1,color='white')
    
    xm,ym=m(ra_m,dec_m)
    m.scatter(xm,ym,s=100,color='yellow',marker='^',label='messier objects')
    
    xcb,ycb=m(ra_cb,dec_cb)
    m.scatter(xcb,ycb,s=20,color='g',marker='_',label='constellation borders')
   
    plt.legend(loc=8,shadow=True,ncol=3,fontsize=15,facecolor='grey')
    plt.show()



def hop_sequence_plot(lon,lat):
    
    fig2=plt.figure(figsize=(60,60))
    #RA values of hops are converted to the celestial coordinates 
    lon=[(360-i) if i>180 else (-i) for i in lon]
    ax2=fig2.add_subplot(1,1,1)
    ax2.set_facecolor('k')
    
    n = Basemap(width=10000000,height=8000000,projection = "stere",
            lat_0=dec_in,lon_0=ra_in,resolution = "i",celestial=True
            ,fix_aspect=False)
    
    plt.title('Hops',pad=30,size=20)
    n.drawmapboundary(color='grey',linewidth=1.5,fill_color='k')
    
    x1,y1=n(ra_1,dec_1) # converting to coordinates of the projection
    n.scatter(x1,y1,s=300,color='white')
    
    x2,y2=n(ra_2,dec_2)
    n.scatter(x2,y2,s=100,color='white')
    
    x3,y3=n(ra_3,dec_3)
    n.scatter(x3,y3,s=20,color='white')
    
    x4,y4=n(ra_4,dec_4)
    n.scatter(x4,y4,s=10,color='white')
    
    x5,y5=n(ra_5,dec_5)
    n.scatter(x5,y5,s=5,color='white')
    
    x6,y6=n(ra_6,dec_6) #data of stars with < 6 mag
    n.scatter(x6,y6,s=1,color='white',label='stars')
       
    # uncheck the following if u want to include dimmer stars 
    #x7,y7=n(ra_7,dec_7)
    #n.scatter(x7,y7,s=4,color='r',label='stars')
        
    #x8,y8=n(ra_8,dec_8)
    #n.scatter(x8,y8,s=3,color='b',label='stars')
        
    #x9,y9=n(ra_9,dec_9)
    #n.scatter(x9,y9,s=1,color='g',label='stars')
   
    xm,ym=n(ra_m,dec_m)
    n.scatter(xm,ym,s=150,color='yellow',marker='^',label='messier objects')
    
    xcb,ycb=n(ra_cb,dec_cb)
    n.scatter(xcb,ycb,s=10,color='g',label='constellation boundaries')
    
    n.drawparallels(range(-90,90,10),color='white',labels=[1,1,0,0])
    n.drawmeridians(range(0,360,10),color='white',labels=[0,0,1,1])
    
    #adding star hops 
    for i in range(1,len(lon)):
        n.drawgreatcircle(lon[i-1],lat[i-1],lon[i],lat[i],
                          color='white',linewidth=1.9)
    lon,lat=n(lon,lat)
    n.scatter(lon,lat,color='dimgrey',s=100,marker='o')
    
    #adding prominenet star names. 
    Ra,Dec=n(RA,DEC)
    
    for i in range(700):
        if name[i]!='-':
            ax2.text(Ra[i],Dec[i]+100000,name[i],fontsize=10,
                     fontweight='bold',color='deeppink').set_clip_on(True)
           
        else:
            ax2.text(Ra[i],Dec[i]+100000,name_bayer[i],fontsize=10,
                     fontweight='bold',color='deeppink').set_clip_on(True)
        
    plt.legend(loc=8,shadow=True,ncol=3,fontsize=15,facecolor='grey')
    plt.show()
 

ra_in=float(input('enter RA of object in degrees  (0 and 360 '))

dec_in=float(input('enter DEC f object in degrees (-90 and +90 '))
#a_fov=float(input('enter the apparent field of view of eyepiece in degrees'))
#f_eyep=float(input('enter the focal length of eye piece'))
#f_obj=float(input('enter the focal length of  objective'))
#D=float(input('enter diameter of telescope in mm'))

#fov=float(a_fov/(f_obj/f_eyep)) #true field of view
#m_lim=2+5*np.log10(D)
#app_fov_finder_scope=float(input('enter apparent field of view of finder scope'))
#mag_fov_finder_scope=float(input('enter magnification of finder scope'))
#fov_finder_scope=float(app_fov_finder_scope/mag_fov_finder_scope)
fov=float(input('enter true fov in degrees'))
fov_finder_scope=float(input('enter fov of finder scope'))
m_lim=float(input('enter lim mag'))

#ra_in,dec_in,fov,fov_finder_scope,m_lim=[245.8,-25.6,2,3,10]

#constellation borders
data_cb=pd.read_csv('constellation_borders.csv',encoding='latin1')
dec_cb=np.array(data_cb['DEJ2000'])
ra_cb=np.array(data_cb['RAJ2000'])
#converting the ra to celestial coordinate conventions.
ra_cb=[(360-i) if i>=180 else (-i) for i in ra_cb]

#messier objects
data_m=pd.read_csv("messier_objects.csv",encoding='latin1')
ra_m =np.array( data_m['RAJ2000'])
ra_m=[(360-i) if i>=180 else (-i) for i in ra_m]
dec_m =np.array (data_m['DEJ2000'])

#star data
file=pd.read_csv('tycho-1.csv')
data=file[file.columns[file.columns.isin (['RAJ2000','DEJ2000','V','Name','Bayer'])]]
#converting to celestial coordinates
data['RAJ2000']=[(360-i) if i>=180 else (-i) for i in data['RAJ2000']]

RA=np.array(data['RAJ2000'])
DEC=np.array(data['DEJ2000'])
name=np.array(data['Name'])
name_bayer=np.array(data['Bayer'])


# sorting the data into groups based their mag so that each class can be plotted with different size
data_1=data[data['V'] <= 1] # will be the brightest stars
ra_1=np.array(data_1['RAJ2000'])
dec_1=np.array(data_1['DEJ2000'])

data_2=data[(data['V'] <=2) & (data['V'] > 1)]
ra_2=np.array(data_2['RAJ2000'])
dec_2=np.array(data_2['DEJ2000'])

data_3=data[(data['V'] <=3) & (data['V'] >2)]
ra_3=np.array(data_3['RAJ2000'])
dec_3=np.array(data_3['DEJ2000'])

data_4=data[(data['V'] <= 4) & (data['V'] > 3)]
ra_4=np.array(data_4['RAJ2000'])
dec_4=np.array(data_4['DEJ2000'])

data_5=data[(data['V'] <=5)  & (data['V'] > 4)]
ra_5=np.array(data_5['RAJ2000'])
dec_5=np.array(data_5['DEJ2000'])

data_6=data[(data['V'] <=6) & (data['V'] > 5)]    
ra_6=np.array(data_6['RAJ2000'])
dec_6=np.array(data_6['DEJ2000'])

data_7=data[(data['V'] <=8) & (data['V'] > 6)]    
ra_7=np.array(data_7['RAJ2000'])
dec_7=np.array(data_7['DEJ2000'])

data_8=data[(data['V'] <10) & (data['V'] > 8)]    
ra_8=np.array(data_8['RAJ2000'])
dec_8=np.array(data_8['DEJ2000'])

data_9=data[data['V'] >= 10] 
ra_9=np.array(data_9['RAJ2000'])
dec_9=np.array(data_9['DEJ2000'])

fig = plt.figure(figsize=(60,60))
telescope(fov,1)
telescope(fov_finder_scope,2)

Lon=[0,10,20,15,-10]
Lat=[20,18,-15,-6,24]
#pass the longitude and latitude array of the hops created
hop_sequence_plot(Lon,Lat)


