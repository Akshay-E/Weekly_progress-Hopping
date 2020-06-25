from astroquery.simbad import Simbad 
import pandas as pd
from astroquery.vizier import Vizier
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap


ra_in=input('enter RA f object in degrees')
dec_in=input('enter DEC f object in degrees')

#constellation borders
data_cb=pd.read_csv('constellation_borders.csv')
dec_cb=np.array(data_cb['DEJ2000'])
ra_cb=np.array(data_cb['RAJ2000'])

#messier objects
data_m=pd.read_csv("messier_objects.csv")
ra_m =np.array( data_m['RA_d_A_ICRS_J2017_5_2000'])
dec_m =np.array (data_m['DEC_d_D_ICRS_J2017_5_2000'])

#star dataa
file=pd.read_csv('hygdata_v3.csv')
data=file[file.columns[file.columns.isin (['id','ra','dec','mag'])]]
data['ra']=data['ra']*15 

data_1=data[(data['mag'] > 15)] 
ra_1=np.array(data_1['ra'])
dec_1=np.array(data_1['dec'])

data_2=data[(data['mag'] <=15) & (data['mag'] > 10)]
ra_2=np.array(data_2['ra'])
dec_2=np.array(data_2['dec'])

data_3=data[(data['mag'] <=10) & (data['mag'] > 8)]
ra_3=np.array(data_3['ra'])
dec_3=np.array(data_3['dec'])

data_4=data[(data['mag'] <= 8) & (data['mag'] > 6)]
ra_4=np.array(data_4['ra'])
dec_4=np.array(data_4['dec'])

data_5=data[(data['mag'] <=6)  & (data['mag'] > 4)]
ra_5=np.array(data_5['ra'])
dec_5=np.array(data_5['dec'])

data_6=data[(data['mag'] <= 4)]
ra_6=np.array(data_6['ra'])
dec_6=np.array(data_6['dec'])

#plotting
fig = plt.figure(figsize=(30,30))
ax= fig.add_subplot(111)
m = Basemap(width=12000000,height=8000000,projection = "stere",lon_0 = ra_in, lat_0=dec_in ,resolution = "h")

x1,y1=m(ra_1,dec_1)

m.scatter(x1,y1,s=.01,color='deeppink')

x2,y2=m(ra_2,dec_2)
m.scatter(x2,y2,s=.1,color='k')

x3,y3=m(ra_3,dec_3)
m.scatter(x3,y3,s=1,color='k')

x4,y4=m(ra_4,dec_4)
m.scatter(x4,y4,s=5,color='k')

x5,y5=m(ra_5,dec_5)
m.scatter(x5,y5,s=10,color='k')

x6,y6=m(ra_6,dec_6)
m.scatter(x6,y6,s=15,color='k')

xm,ym=m(ra_m,dec_m)
m.scatter(xm,ym,s=10,color='r',marker='*')

xcb,ycb=m(ra_cb,dec_cb)
m.scatter(xcb,ycb,s=10,color='g',marker='_')


parallels = np.arange(-90,90,15)
meridians = np.arange(0,360,15)
m.drawparallels(parallels,color="k",labels=[1,1,0,0],dashes=[1,1])
m.drawmeridians(meridians,color="k",labels=[0,0,1,1],dashes=[1,1])
plt.show()









