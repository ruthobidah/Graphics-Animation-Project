from visual import*


##def tyre():
##    ring(pos=(1,1,1), axis=(0,1,0), radius=0.5, thickness=0.1, color=color.red, material=materials.marble)
##    ring(pos=(2,2,2), axis=(0,1,0), radius=0.5, thickness=0.2, color=color.cyan, material=materials.marble)
##    
##tyre()

#sphere()

#def car():
theCar = box(pos=(0,0,1), axis=(0,5,0),lenght=0.05, size =(0.1,0.05,0.05), height=0.05, width=0.05, color=color.orange,material=materials.emissive)

#car()


r = vector(0,0,1)

while r.x < 10:
    rate(1)
    theCar.pos = r
    r.x = r.x+ 1

print("end")
