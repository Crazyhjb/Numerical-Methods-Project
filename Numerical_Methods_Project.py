import numpy as np
import matplotlib.pyplot as plt
#Heat equation
A1 = np.array([[4,-1,0,-1,0,0,0,0,0],
 [-1,4,-1,0,-1,0,0,0,0],
 [0,-1,4,0,0,-1,0,0,0],
 [-1,0,0,4,-1,0,-1,0,0],
 [0,-1,0,-1,4,-1,0,-1,0],
 [0,0,-1,0,-1,4,0,0,-1],
 [0,0,0,-1,0,0,4,-1,0],
 [0,0,0,0,-1,0,-1,4,-1],
 [0,0,0,0,0,-1,0,-1,4]])
b= np.array([0,0,100,0,0,100,200,200,300])
T = np.matmul(np.linalg.inv(A1),b)
print("Temprature at given points:",T)
Z = np.array([[0,0,0,0,50],
 [0,T[0],T[1],T[2],100],
 [0,T[3],T[4],T[5],100],
 [0,T[6],T[7],T[8],100],
 [100,200,200,200,150]])
plt.imshow(Z)
plt.colorbar(label="Temprature")
plt.title('Heat Map of temperatures at defined points')
plt.show()
#1-D wave equation
A=np.linalg.inv(np.array([[4,-1,0,0],
 [-1,4,-1,0],
 [0,-1,4,-1],
 [0,0,-1,4]]))
Tj0= np.array([np.sin(0.4*np.pi),
 np.sin(0.2*np.pi)+np.sin(0.6*np.pi),
np.sin(0.4*np.pi)+np.sin(0.8*np.pi),
np.sin(0.6*np.pi)])
Tu1=np.matmul(A,Tj0)
u11,u21,u31,u41=Tu1
print("\n"+"Tempratures at t= 0.04:",Tu1)
Tj1=np.array([u21,u31+u11,u41+u21,u31])
u12,u22,u32,u42=np.matmul(A,Tj1)
Tu2=np.array([u12,u22,u32,u42])
print("Tempratures at t= 0.08:",Tu2)
Tj2=np.array([u22,u12+u32,u22+u42,u32])
u13,u23,u33,u43=np.matmul(A,Tj2)
Tu3=np.array([u13,u23,u33,u43])
print("Tempratures at t= 0.12:",Tu3)
Tj3=np.array([u23,u13+u33,u23+u43,u33])
u14,u24,u34,u44=np.matmul(A,Tj3)
Tu4=np.array([u14,u24,u34,u44])

print("Tempratures at t= 0.16:",Tu4)
Tj4=np.array([u24,u14+u34,u24+u44,u34])
u15,u25,u35,u45=np.matmul(A,Tj4)
Tu5=np.array([u15,u25,u35,u45])
print("Tempratures at t= 0.20:",Tu5)
#The border points are =0 meaning that
#appending them on will give the correct
#result when plotted
u1=np.append([0],np.append(Tu1,[0]))
u2=np.append([0],np.append(Tu2,[0]))
u3=np.append([0],np.append(Tu3,[0]))
u4=np.append([0],np.append(Tu4,[0]))
u5=np.append([0],np.append(Tu5,[0]))
x=np.arange(0,1.2,0.2)
plt.plot(x,u1,label='t=0.04',c='k')
plt.scatter(x,u1,c='k')
plt.plot(x,u2,label='t=0.08',c='b')
plt.scatter(x,u2,c='b')
plt.plot(x,u3,label='t=0.12',c='g')
plt.scatter(x,u3,c='g')
plt.plot(x,u4,label='t=0.16',c='y')
plt.scatter(x,u4,c='y')
plt.plot(x,u5,label='t=0.20',c='c')
plt.scatter(x,u5,c='c')
plt.title("Temperature against distance with varying times")
plt.ylabel("Temprature")
plt.xlabel("Distance")
plt.legend(loc=0)
plt.show()