"""Cherry tree - Complex 2003 - Licence: Python

This example creates a cherry tree and apply a simple
dynamics looks like the effect caused by a small wind.
Each run produces a different tree according to the
initial seed value of the pseudo-random generator.

TODO:

- Embed the tree into a class with keyword arguments
  such as colors, sizes, depth, fullness, etc...
- Add texture to make it more realistic
- Create a small forest
- Implement dynamic looks like the effect of waves of wind

Modifications:
2003.01.24. - Complex (cx@cx.hu) - First release
"""

from visual import *
from math import *
from random import *
import copy

scene2 = display(title='Peaceful Night',
     x=0, y=0, width=1024, height=768,
     center=(0,6,0), background=(0,0,0)) #,material=materials.texture(data=stars, mapping ="cubic"))

##scene.width = 1024
##scene.height = 768
#scene.material=materials.marble

scene.autozoom = False


leaves=[]
fruits=[]

def random_vector():
    return vector(random(),random(),random())

def fruit(frm,p,a,r):
    f=frame(frame=frm, pos=p)
    cylinder(frame=f, pos=(0,0,0), axis=a, radius=r, color=color.green)
    sphere(frame=f, pos=(0,0,0), radius=r/2, color=color.red)
    return f

def make_tyre(frm,pos, axis):
        f=frame(frame = frm)
        tyframe = f  #frame()
        typos = pos
        axoffset = -axis[2] / 10.0
        tyr = materials.loadTGA("\\Users\\rutho\\Desktop\\project graphicxs car\\tyre.tga")
        ty = cylinder(frame=tyframe, pos=typos, length=1, radius=0.85, axis=axis, color=(0.2,0.2,0.2),material=materials.texture(data=tyr, mapping ="cubic") ,opacity=0.9)
        tyaxl = cylinder(frame=tyframe, pos=(typos[0],typos[1],typos[2]+axoffset), length=ty.length, radius=0.3*ty.radius, axis=ty.axis, color=(0.6,0.6,0.6),material=materials.chrome, opacity=ty.opacity)
        return tyframe

def copy_move(o, pos=(0,0,0)):
        no = copy.copy(o)
        no.pos[0],no.pos[1],no.pos[2] = pos
        return no

def new_car(frm,p):
    f=frame(frame=frm, pos=p)

    p0= vector(-3,0,1)
    p1=vector(-3,0,1.9)
    p2=vector(-3,0,-1.85)
    p3=vector(2,-0.5,2.5)
    p4=vector(-1.8,-0.5,2.5)
    p5=vector(2,-0.5,-2.5)
    p6=vector(-1.8,-0.5,-2.5)
    p7=vector(0,1.5,0)
    p8=vector(-3,0,-1)
    p9=vector(3,0,1)
    p10=vector(3,0,-1)
    p11=vector(3.4,0.75,0)
    p12=vector(3.2,1.25,-0.05)

    
    range=4
    window= materials.loadTGA("\\Users\\rutho\\Desktop\\project graphicxs car\\window.tga")
    paint= materials.loadTGA("\\Users\\rutho\\Desktop\\project graphicxs car\\car_paint.tga")
    b = box(frame=f,pos= p, length=6, width=4, height=2, color=(0.95,0.1,0.89), material=materials.texture(data=paint, mapping ="rectangular" ))
    b2 = box(frame =f,pos=p+p7, length=3, width=3, height=1, color=color.yellow,material=materials.texture(data=window, mapping ="cubic" ))
    b3 = box(frame=f,pos= p+p12, length=0.1, width=5, height=1, color=color.blue, material=materials.blazed)

    text(frame=f,pos=p+p11,text='XruthX',axis=(0,0,-18),align='center', hieght =0.01,width=0.01, depth=-0.3, color=color.black, material=materials.silver)
    lpos = p+p0
    headlight_length = 100


    tspos = p+p1
    ts = local_light(frame =f,pos=tspos, color=color.yellow)
    bts = box(frame =f,pos=tspos, length=0.3, width=0.3, height=0.4, material=materials.emissive, color=color.yellow)
    tsl = local_light(frame =f,pos=tspos, color=color.yellow)
    tsc = cone(frame =f,pos=(tspos[0]-5,0,tspos[2]+5), length=10, axis=(1,0,-1), radius=0.3, material=materials.emissive, color=color.yellow, opacity=0.3)

    new_ts_pos = p+p2
    ts2 = copy_move(ts, new_ts_pos)
    bts2 = copy_move(bts, new_ts_pos)
    tsl2 = copy_move(tsl, new_ts_pos)
    tsc2 = cone(frame =f,pos=(new_ts_pos[0]-5,0,new_ts_pos[2]-5), length=10, axis=(1,0,1), radius=0.3, material=materials.emissive, color=color.yellow, opacity=0.3)
    #tsc2 = copy_move(tsc, pos=(new_ts_pos[0]-4.65, 0, new_ts_pos[2]+5))
    #tsc2.axis = (1,0,5)


    ty0 = make_tyre(frm =f,pos=p+p3, axis=(0,0,-1))
    ty1 = make_tyre(frm =f,pos=p+p4, axis=(0,0,-1))
    ty2 = make_tyre(frm =f,pos=p+p5,axis=(0,0,1))
    ty3 = make_tyre(frm =f,pos=p+p6,axis=(0,0,1))


    l = local_light(frame =f,pos=lpos, color=color.red)
    s = sphere(frame =f,pos=lpos, radius=0.3, material=materials.emissive)
    #c = cone(pos=lpos, radius=0.3, axis=(-1,0,), length=40, material=materials.emissive, color=color.white, opacity=0.3)
    c = cone(frame =f,pos=(lpos[0]-headlight_length+65,lpos[1],lpos[2]), radius=4.0, axis=(1,0,0), length=40, material=materials.emissive, color=color.white, opacity=0.3)

    new_pos = p+p8
    l2 = copy_move(l, pos=new_pos)
    s2 = copy_move(s, pos=new_pos)
    c2 = copy_move(c, pos=new_pos)
    c2.pos[0],c2.pos[1],c2.pos[2] = p+vector(-38,0,-1)

    rlpos = p+p9
    rl = local_light(frame =f,pos=rlpos, color=color.red)
    rs = sphere(frame =f,pos=rlpos, radius=0.3, material=materials.emissive, color=color.red)
    rc = cone(frame =f,pos=(rlpos[0]+14,0,rlpos[2]), radius=1.0, axis=(-1,0,0),length=20, material=materials.emissive, color=color.red, opacity=0.3)


    rlpos2 = p+p10
    rl2 = copy_move(rl, pos=rlpos2)
    rs2 = copy_move(rs, pos=rlpos2)
    rc2 = copy_move(rc, pos=rlpos2)
    rc2.pos[0],c2.pos[1],c2.pos[2] = p+vector(17,0,-1)

    while True:
        rate(3)
        tsc.visible = not tsc.visible
        tsc2.visible = not tsc2.visible
##        ty0.rotate(angle=2*pi)
##        ty1.rotate(angle=2*pi)
##        ty2.rotate(angle=2*pi)
##        ty3.rotate(angle=2*pi)
        return f
        

##def tyre(frm,p,r,t):
##    f=frame(frame=frm, pos=p)
##    tyr = materials.loadTGA("\\Users\\Obidah\\Documents\\CPSC 484\\project\\tyre.tga")
##    ring(frame=f, pos= (0,0,0), axis=(1,0,0), radius=r,thickness=t,color=color.green, material=materials.texture(data=tyr, mapping ="cubic"))
##    cylinder(frame=f, pos=(-0.1,0,0),radius=r/2,axis=(0.2,0,0),color=color.red, material=materials.silver)
##    return f

    
def leaf(frm,p,a):
    na=norm(a)
    ex=cross((0,1,0),na)
    ey=cross(ex,na)
    ex=0.075*ex
    ey=0.045*ey
    points=[(0.0,0.1),(0.2,0.3),(0.4,0.5),(0.8,0.3),(1.0,0.0),(0.8,-0.3),(0.4,-0.5),(0.2,-0.3),(0.0,-0.1)]
    f=frame(frame=frm, pos=p)
    ex=rotate(ex, axis=ey, angle=pi*0.5*(random()-0.1))
    cylinder(frame=f, pos=(0,0,0), axis=1.2*ex, radius=0.025*mag(ey), color=color.green)
    c=convex(frame=f, pos=[(x+0.29)*ex+y*ey for x,y in points], color=color.green)
    return f

def tree(frm,p,a,r,c,ml,mr,e,d): #(frame, position, axis, radius, color,)
    q,v=p+a,ml*a*(0.8+0.4*random())
    tre3 = materials.loadTGA("\\Users\\rutho\\Desktop\\project graphicxs car\\tree.tga")
    cylinder(frame=frm, pos=p, axis=a, radius=r, color=c, material=materials.texture(data=tre3, mapping ="cylinder"))
    sphere(frame=frm, pos=q, radius=r, color=c, material=materials.texture(data=tre3, mapping ="cylinder"))
    if d>0 and (d>1 or randrange(3)>0):
        a1,a2=cross(a,(0,0,1)),cross(a,(1,0,0))
        s=rotate(v,axis=a1,angle=e)
        n=3+(randrange(10)>3)
        if d<2: n=2
        for i in range(n):
            tree(frm, q, rotate(rotate(s,axis=a,angle=2.0*pi/n*i+pi/5.0/d*random()), axis=a,angle=pi/4.0*(random()-0.5)), mr*r, c, ml, mr, e, d-1)
    else:
        b=vector(0,-0.05,0)
        if randrange(3)<1:
            t=0.1*p+0.9*q
            fruits.append(fruit(frm,t,rotate(b,axis=a,angle=pi*(1+random())/8.0),0.0025))
            fruits.append(fruit(frm,t,rotate(b,axis=a,angle=-pi*(1+random())/8.0),0.0025))
        for i in range(3):
            l=leaf(frm,q,0.5*v)
            l.rotate(axis=a,angle=2*pi*i/3.0)
            leaves.append(l)
    
def car(frm,p,s,a,c):
    f=frame(frame=frm, pos=p)
    dim = (0.4,1,0.5)
    p2 = vector(0,0.2,0.6)
    p3 = vector(0,-0.2,0.6)
    p2= p+vector(-0.58,-0.4,0.3)
    p0= vector(0,0.4,0.3)
    p1= vector(0,0.2,0.6)
    box(frame=f,pos = p,size=s, axis=a, color=c)
    box(frame=f, size =dim,pos = p-p2, axis=a, color=c)
    box(frame=f, size =dim,pos = p+p3, axis=a, color=c)


scene2.visible=0
fr=frame(pos=(0,-0.8,0))
fr2=frame(pos=(0,0.8,0),axis=(1,0,38))
watr = materials.loadTGA("\\Users\\rutho\\Desktop\\project graphicxs car\\pond.tga")
sand = materials.loadTGA("\\Users\\rutho\\Desktop\\project graphicxs car\\sand.tga")
road = materials.loadTGA("\\Users\\rutho\\Desktop\\project graphicxs car\\road_texture.tga")
box(frame=fr,pos=(0,0.11,0), size=(0.2,40,40), axis=(0,0.11,0), color=(1,0.6,0.5), material= materials.texture(data=sand, mapping ="cubic"))
box(frame=fr,pos=(0,0.11,0), size=(0.3,10,40), axis=(0,0.11,0), color=color.black, material= materials.texture(data=road, mapping ="cubic"))
ellipsoid(frame=fr,pos=(-12,0.11,-12), length=8, height=0.3, width=12, axis=(5,0,0), color=(1,0.6,0.5), opacity=0.35, material= materials.texture(data=watr, mapping ="cubic"))
ellipsoid(frame=fr,pos=(12,0.11,12), length=8, height=0.3, width=12, axis=(5,0,0), color=(1,0.6,0.5), opacity=0.35, material= materials.texture(data=watr, mapping ="cubic"))


##tr=tree(fr,vector(6,0,0), vector(0,5,0), 0.5, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)
##tr=tree(fr,vector(-18,0,0), vector(0,1,0), 0.1, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)
##tr=tree(fr,vector(-17,0,2), vector(0,1,0), 0.3, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)   #do some kind of while loop from range 1.5 to 6 and then one to the negative range
##tr=tree(fr,vector(5,0,0), vector(0,1,0), 0.25, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)    #changing the z axis changes across position
##tr=tree(fr,vector(5.5,0,0), vector(0,4,0), 0.3, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)  #A combination of changes to the x and z axis will fill the space with trees
##tr=tree(fr,vector(5.5,0,3), vector(0,4,0), 0.2, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)  #Other non-necessary enhancements will be to do textures for leaves, fruit, & tree
##
##tr=tree(fr,vector(-6,0,0), vector(0,6,0), 0.6, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)
##tr=tree(fr,vector(18,0,0), vector(0,1,0), 0.1, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)
##tr=tree(fr,vector(17,0,2), vector(0,1,0), 0.75, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)   #do some kind of while loop from range 1.5 to 6 and then one to the negative range
##tr=tree(fr,vector(-5,0,0), vector(0,1,0), 0.25, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)    #changing the z axis changes across position
##tr=tree(fr,vector(-5.5,0,0), vector(0,3,0), 0.1, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)  #A combination of changes to the x and z axis will fill the space with trees
##tr=tree(fr,vector(-5.5,0,3), vector(0,4,0), 0.2, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)  #Other non-necessary enhancements will be to do textures for leaves, fruit, & tree
##
##tr=tree(fr,vector(6,0,5), vector(0,5,0), 0.5, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)
##tr=tree(fr,vector(-10,0,-4), vector(0,1,0), 0.1, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)
##tr=tree(fr,vector(8,0,2), vector(0,1,0), 0.75, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)   #do some kind of while loop from range 1.5 to 6 and then one to the negative range
##tr=tree(fr,vector(5,0,6), vector(0,1,0), 0.25, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)    #changing the z axis changes across position
##tr=tree(fr,vector(5.5,0,-7), vector(0,3,0), 0.1, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)  #A combination of changes to the x and z axis will fill the space with trees
##tr=tree(fr,vector(5.5,0,3), vector(0,4,0), 0.2, (0.8,0.4,0.1), 0.6, 0.6, pi/3.0, 5)  #Other non-necessary enhancements will be to do textures for leaves, fruit, & tree


scene2.visible=1

f=3
ai=0
aim=f*100
while 1:
    rate(50)
    a=(ai-aim/2)*pi/50.0
    ai+=f
    if ai>=aim: ai=0
    for i in range(len(leaves)/20):
        for l in (leaves,fruits):
            o=choice(l)
            o.rotate(axis=o.up, angle=(a-pi)/200.0)

        
        
    cr1= new_car(frm=fr2,p=vector(10,0,0))#,s=(0.7,1,1),a=(0,0.3,0), c=color.cyan)
    #cr2= new_car(frm=fr2,p=vector(0,3,-2.7))#,s=(0.7,1,1),a=(0,0.3,0), c=color.cyan)
    r = vector(0,0.8,0)

    while r.z<0.1:#True: #r.z > -2.7:
        rate(15)
        fr2.pos=r
        #car(frm=fr2,p=r, s=(0.5,1,1),a=(0,0.3,0), c=color.cyan)
        cr1.frame.pos=vector(cr1.frame.x,cr1.frame.y,cr1.frame.z-6)
        r.z=r.z-.15

   
