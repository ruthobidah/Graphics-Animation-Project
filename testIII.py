from visual import*

rings=[]
#ring(pos=(1,0,1), axis=(1,0,1), radius=0.5,thickness=0.1 )
#box(pos = (2,0,1), axis = (1,1,1), size = (2,2,2), color=color.green)

s= (2,2,2)
c = 4
for i in range(c):
    i=ring(pos=(1,0,1), axis=(1,0,1), radius=0.5,thickness=0.1 )
    i.rotate(angle=2*pi)
    rings.append(i)
    
    #rings.append(ring(pos=(1,0,1), axis=(1,0,1), radius=0.5,thickness=0.1 ))
    
