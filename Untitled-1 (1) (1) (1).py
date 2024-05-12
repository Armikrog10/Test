from tkinter import *
from math import *
from random import*

Vova_kyshaet_pelmeni = 0
x = 600
y = 435
x1 = 0
y1 = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0
hp_igroka = 100
skorost = 5
Vova = []
Shabanov = []
Pyla_dyra = []
Pyla_dyraV = []
Mina_molodec = []
yroni = []
Pivo_cifri = []
Mina_cifri = []
Ybito_cifri = []
Aptetka = []
babanow = 0
babanow_max = 6
max_babanow_max = 20
Pyla_dyra_mozno = True
Yron_mozno = True
stan = False
Vrema_p = 500
Vrema_y = 500
Pivo = 20
Mina = 2
Ybito = 0

def KD():
    global Vrema_p
    global Pyla_dyra_mozno
    if(Vrema_p < 500):
        Vrema_p += 1
    else:
        Pyla_dyra_mozno = True
    w1.after(1,KD)
def KD_yron():
    global Vrema_y
    global Yron_mozno
    if(Vrema_y < 500):
        Vrema_y += 1
    else:
        Yron_mozno = True
    w1.after(1,KD_yron)
def KD_hodit(vrema):
    vrema += 1
def HP(x,y,x1,y1,hp,hp_max):
    podlozka1 = c.create_rectangle(x+x1, y+y1, x + x1+10, y + (y1+x1), fill='white')
    podlozka2 = c.create_rectangle(x+x1+2, y+y1+2, x + x1+8, y + (y1+x1)-2, fill='black')
    polozka = c.create_rectangle(x+x1+2, y+((y1+x1-2)-((y1+x1-2-(y1+2))*(hp/hp_max))), x + x1+8, y + y1+x1-2, fill='red')
    return([podlozka1,podlozka2,polozka])
def Patroni():
    global Pivo_cifri
    global Pivo
    global Mina_cifri
    global Mina
    c.delete(Pivo_cifri[0])
    c.delete(Mina_cifri[0])
    options2 = {"fill": "white","font":"Times 30","width": 200, "text": f"{Pivo}"}
    Pivo_cifri = [c.create_text((185, 24),**options2)]
    options = {"fill": "orange","font":"Times 30","width": 200, "text": f"{Mina}"}
    Mina_cifri = [c.create_text((245, 24),**options)]
def Vova_idot():
    global x
    global y
    global x1
    global y1
    global Vova
    global skorost
    global stan
    global Pivo_cifri
    global hp_igroka
    if(hp_igroka <=0 ):
        exit()
    if(skorost > 5):
        skorost -= 1
    if(skorost < 5):
        skorost += 1
    dx = x1 - x-15
    dy = y1 - y-15
    sd = atan2(dy,dx)/pi*180
    if(sqrt((dx)**2 + (dy)**2)>=3):
        x += cos(sd*(pi/180))*skorost
        y += sin(sd*(pi/180))*skorost
    else:
        stan = False
    c.delete(Vova[0])
    Vova = [c.create_rectangle(x, y, x + 30, y + 30, fill='white')]
    w1.after(30,Vova_idot)
def Shabanov_prihshol():
    global Shabanov
    hyha = randint(0,1)
    if(hyha == 0):
        hyha2 = randint(0,1)
        x = randint(0,1200)
        if(hyha2 == 0):
            y = -160
        if(hyha2 == 1):
            y = 1030
    if(hyha == 1):
        hyha2 = randint(0,1)
        y = randint(0,870)
        if(hyha2 == 0):
            x = -160
        if(hyha2 == 1):
            x = 1360
    razmer = randint(15,80)
    Shabanov_rad_hp = (razmer/30)*50
    for i in Shabanov:
        while((x+razmer > i[1][0] and x < i[1][0]+i[4])and(y+razmer > i[1][1] and y < i[1][1]+i[4])):
            hyha = randint(0,1)
            if(hyha == 0):
                hyha2 = randint(0,1)
                x = randint(0,1200)
                if(hyha2 == 0):
                    y = -160
                if(hyha2 == 1):
                    y = 1030
            if(hyha == 1):
                hyha2 = randint(0,1)
                y = randint(0,870)
                if(hyha2 == 0):
                    x = -160
                if(hyha2 == 1):
                    x = 1360
    if(len(Shabanov) < babanow_max):
        hyha3 = randint(0,1)
        if(hyha3 == 0):
            Shabanov += [[c.create_rectangle(x, y, x + razmer, y + razmer, fill='red'),[x,y],Shabanov_rad_hp,HP(x,y,razmer-5, razmer/2,Shabanov_rad_hp,Shabanov_rad_hp),razmer,Shabanov_rad_hp,[False,0,0,0],True,500,0]]
        if(hyha3 == 1):
            Shabanov += [[c.create_rectangle(x, y, x + razmer, y + razmer, fill='blue'),[x,y],Shabanov_rad_hp,HP(x,y,razmer-5, razmer/2,Shabanov_rad_hp,Shabanov_rad_hp),razmer,Shabanov_rad_hp,[False,0,0,0],True,500,1,700]]
    w1.after(3000, Shabanov_prihshol)
def Aptetka_prihshol():
    global Aptetka
    x = randint(30,1170)
    y = randint(30,840)
    Aptetka += [[c.create_rectangle(x, y, x + 20, y + 20, fill='green'),[x,y],0]]
    w1.after(randint(25000,40000), Aptetka_prihshol)
def Shabanov_idot():
    global x
    global y
    global x1
    global y1
    global Shabanov
    global skorost
    global stan
    global hp_igroka
    global hp_sled
    global yroni
    global babanow
    global babanow_max
    global max_babanow_max
    global Yron_mozno
    global Vrema_y
    global Aptetka
    global Ybito_cifri
    global Ybito
    global Pyla_dyraV
    for i in Shabanov:
        if(i[8] < 500):
            i[8]+=16
        else:
            i[7] = True
        if(i[2]<=0):
            c.delete(i[0],i[3][0],i[3][1],i[3][2])
            Shabanov.remove(i)
            hil = randint(0,1)
            Ybito += 1
            c.delete(Ybito_cifri[0])
            options8 = {"fill": "red","font":"Times 30","width": 200, "text": f"Убито: {Ybito}"}
            Ybito_cifri = [c.create_text((1100, 24),**options8)]
            if(hil >= 1):
                if(i[4]<50):
                    Aptetka += [[c.create_rectangle(i[1][0]+(i[4]/2), i[1][1]+(i[4]/2), i[1][0]+(i[4]/2) + 10, i[1][1]+(i[4]/2) + 10, fill='green'),[i[1][0]+(i[4]/2),i[1][1]+(i[4]/2)],1]]
                else:
                    Aptetka += [[c.create_rectangle(i[1][0]+(i[4]/2), i[1][1]+(i[4]/2), i[1][0]+(i[4]/2) + 20, i[1][1]+(i[4]/2) + 20, fill='green'),[i[1][0]+(i[4]/2),i[1][1]+(i[4]/2)],0]]
            if(babanow < babanow_max):
                babanow+=1
            else:
                if(babanow_max < max_babanow_max):
                    babanow_max+=1
                babanow = 0
        else:
            if(i[6][0]):
                dx = i[6][1] - i[1][0]
                dy = i[6][2] - i[1][1]
            else:
                dx = x - i[1][0]
                dy = y - i[1][1]
            sd = atan2(dy,dx)/pi*180
            x_x = True
            y_y = True
            for j in Shabanov:
                if(Shabanov.index(i) != Shabanov.index(j)):
                    if((i[1][0]+ i[4]+cos(sd*(pi/180))*(3/(i[4]/30)+i[6][3]) > j[1][0] and i[1][0]+cos(sd*(pi/180))*(3/(i[4]/30)+i[6][3]) < j[1][0]+ j[4])and(i[1][1]+ i[4] > j[1][1] and i[1][1] < j[1][1]+ j[4])):
                        x_x = False
                        i[6][0] = False
                        i[6][3] = 0
                    if((i[1][1]+ i[4]+sin(sd*(pi/180))*(3/(i[4]/30)+i[6][3]) > j[1][1] and i[1][1]+sin(sd*(pi/180))*(3/(i[4]/30)+i[6][3]) < j[1][1]+ j[4])and(i[1][0]+ i[4] > j[1][0] and i[1][0] < j[1][0]+ j[4])):
                        y_y = False
                        i[6][0] = False
                        i[6][3] = 0
            if(i[9] == 0):
                if(((i[1][0]+ i[4] < x or i[1][0] > x+ 30) or (i[1][1]+ i[4] < y or i[1][1] > y+ 30)) and i[7]):
                    if(x_x):
                        i[1][0] += cos(sd*(pi/180))*(3/(i[4]/30)+i[6][3])
                    if(y_y):
                        i[1][1] += sin(sd*(pi/180))*(3/(i[4]/30)+i[6][3])
                if(sqrt((dx)**2 + (dy)**2)<=20 and i[6][0]):
                    i[6][0] = False
                    i[6][3] = 0
                if(((i[1][0]+ i[4] >= x and i[1][0] <= x+ 30) and (i[1][1]+ i[4] >= y and i[1][1] <= y+ 30))and stan == False and Yron_mozno):
                    yron = randint(1,i[4])
                    hp_igroka -= yron
                    c.delete(hp_sled[2])
                    hp_sled[2] = c.create_rectangle(7, 7, 7+(151*(hp_igroka/100)), 38, fill='green')
                    options = {"fill": "white","font":"Times 30","width": 200, "text": f"-{yron}"}
                    yroni += [[c.create_text((x, y),**options),[x,y],y,f"-{yron}","red","Times 30"]]
                    skorost = 10
                    x1 = x+cos(sd*(pi/180))*50
                    y1 = y+sin(sd*(pi/180))*50
                    Vrema_y = 0
                    stan = True
                    Yron_mozno = False
                    i[7]=False
                    i[8]=0
                c.delete(i[0],i[3][0],i[3][1],i[3][2])
                i[0] = [c.create_rectangle(i[1][0], i[1][1], i[1][0] + i[4], i[1][1] + i[4], fill="red")]
                i[3] = HP(i[1][0],i[1][1],i[4]-5,i[4]/2,i[2],i[5])
            else:
                if(sqrt((dx)**2 + (dy)**2)<=300 and i[6][0]==False):
                    x_x = False
                    y_y = False
                if(sqrt((dx)**2 + (dy)**2)<=20 and i[6][0]):
                    x_x = True
                    y_y = True
                    i[6][0] = False
                    i[6][3] = 0
                if(((i[1][0]+ i[4] < x or i[1][0] > x+ 30) or (i[1][1]+ i[4] < y or i[1][1] > y+ 30)) and i[7]):
                    if(x_x):
                        i[1][0] += cos(sd*(pi/180))*(3/(i[4]/30)+i[6][3])
                    if(y_y):
                        i[1][1] += sin(sd*(pi/180))*(3/(i[4]/30)+i[6][3])
                if(i[10] < 700):
                    i[10]+=randint(1,10)
                else:
                    dxp = x - i[1][0]+(i[4]/2)
                    dyp = y - i[1][1]+(i[4]/2)
                    sdp = atan2(dyp,dxp)/pi*180
                    Pyla_dyraV += [[c.create_rectangle(i[1][0]+15, i[1][1]+15, i[1][0] + 10, i[1][1] + 10, fill='violet'),[i[1][0],i[1][1]],sdp]]
                    i[10] = 0
                c.delete(i[0],i[3][0],i[3][1],i[3][2])
                i[0] = [c.create_rectangle(i[1][0], i[1][1], i[1][0] + i[4], i[1][1] + i[4], fill="blue")]
                i[3] = HP(i[1][0],i[1][1],i[4]-5,i[4]/2,i[2],i[5])
    w1.after(30,Shabanov_idot)
def on_mouse_move(event):
    global x2
    global y2
    x2 = int(event.x)
    y2 = int(event.y)
def tochka():
    global x1
    global y1
    global x2
    global y2
    global stan
    if(stan == False):
        x1=x2
        y1=y2
def tochka1():
    global x
    global y
    global Mina_molodec
    global Mina
    if(Mina > 0):
        Mina_molodec += [[c.create_rectangle(x+15, y+15, x + 35, y + 35, fill='orange'),[x,y]]]
        Mina -= 1
        Patroni()
def tochka2():
    global x
    global y
    global x2
    global y2
    global x3
    global y3
    global Pyla_dyra
    global Pyla_dyra_mozno
    global Vrema_p
    global Pivo
    global Pivo_cifri
    x3=x2
    y3=y2
    dx = x3 - x
    dy = y3 - y
    sd = atan2(dy,dx)/pi*180
    if(Pyla_dyra_mozno and Pivo > 0):
        Pyla_dyra += [[c.create_rectangle(x+15, y+15, x + 10, y + 10, fill='yellow'),[x,y],sd]]
        Pivo -= 1
        Patroni()
        Vrema_p = 0
        Pyla_dyra_mozno = False
def Pyla_dyra_idot():
    global x3
    global y3
    global Pyla_dyra
    global Pyla_dyraV
    global yroni
    global Shabanov
    global x
    global y
    global hp_igroka
    global hp_sled
    for i in Pyla_dyra:
        mi = False
        i[1][0] += cos(i[2]*(pi/180))*10
        i[1][1] += sin(i[2]*(pi/180))*10
        c.delete(i[0])
        i[0] = [c.create_rectangle(i[1][0], i[1][1], i[1][0] + 10, i[1][1] + 10, fill='yellow')]
        if(i[1][0]+ 10 > 1200 or i[1][0] < 0 or i[1][1]+ 10 > 870 or i[1][1] < 0):
                mi = True
        for j in Shabanov:
            if((i[1][0]+ 10 > j[1][0] and i[1][0] < j[1][0]+ j[4]) and (i[1][1]+ 10 > j[1][1] and i[1][1] < j[1][1]+ j[4])):
                if(mi == False):
                    yron = randint(3,17)
                    j[2]-= yron
                    options = {"fill": "white","font":"Times 30","width": 200, "text": f"-{yron}"}
                    yroni += [[c.create_text((i[1][0], i[1][1]),**options),[i[1][0],i[1][1]],i[1][1],f"-{yron}","white","Times 30"]]
                mi = True
        if(mi):
            c.delete(i[0])
            Pyla_dyra.remove(i)
    for i in Pyla_dyraV:
        mi = False
        i[1][0] += cos(i[2]*(pi/180))*6
        i[1][1] += sin(i[2]*(pi/180))*6
        c.delete(i[0])
        i[0] = [c.create_rectangle(i[1][0], i[1][1], i[1][0] + 10, i[1][1] + 10, fill='violet')]
        if(i[1][0]+ 10 > 1200 or i[1][0] < 0 or i[1][1]+ 10 > 870 or i[1][1] < 0):
                mi = True
        if((i[1][0]+ 10 > x and i[1][0] < x+ 30) and (i[1][1]+ 10 > y and i[1][1] < y+ 30)):
            if(mi == False):
                yron = randint(3,17)
                hp_igroka -= yron
                c.delete(hp_sled[2])
                hp_sled[2] = c.create_rectangle(7, 7, 7+(151*(hp_igroka/100)), 38, fill='green')
                options = {"fill": "red","font":"Times 30","width": 200, "text": f"-{yron}"}
                yroni += [[c.create_text((i[1][0], i[1][1]),**options),[i[1][0],i[1][1]],i[1][1],f"-{yron}","red","Times 30"]]
            mi = True
        if(mi):
            c.delete(i[0])
            Pyla_dyraV.remove(i)
    w1.after(30,Pyla_dyra_idot) 
def Mina_bah():
    global x3
    global y3
    global Mina_molodec
    global yroni
    global Shabanov
    for i in Mina_molodec:
        for j in Shabanov:
            if((i[1][0]+ 20 >= j[1][0] and i[1][0] <= j[1][0]+ j[4]) and (i[1][1]+ 20 >= j[1][1] and i[1][1] <= j[1][1]+ j[4])):
                for g in Shabanov:
                    dx = g[1][0] - i[1][0]
                    dy = g[1][1] - i[1][1]
                    sd = atan2(dy,dx)/pi*180
                    if(sqrt((dx)**2 + (dy)**2)<=160 and g[6][0] == False):
                        yron = round(g[5]*0.5)
                        g[2]-= yron
                        g[6][1] = g[1][0] + cos(sd*(pi/180))*100
                        g[6][2] = g[1][1] + sin(sd*(pi/180))*100
                        g[6][0] = True
                        g[6][3] = 10
                        options = {"fill": "white","font":"Times 30","width": 200, "text": f"-{yron}"}
                        yroni += [[c.create_text((g[1][0], g[1][1]),**options),[g[1][0],g[1][1]],g[1][1],f"-{yron}","white","Times 30"]]
                c.delete(i[0])
                Mina_molodec.remove(i)
    w1.after(30,Mina_bah) 
def Aptetka_podnato():
    global x
    global y
    global Aptetka
    global hp_igroka
    global Pivo
    global Pivo_cifri
    global yroni
    global hp_sled
    global Mina
    for i in Aptetka:
        if((i[1][0]+ 10 > x and i[1][0] < x+30) and (i[1][1]+ 10 > y and i[1][1] < y+ 30)):
            if(i[2]<=0):
                hp_igroka += 10
                if(hp_igroka > 100):
                    hp_igroka = 100
                Pivo += 10
                Mina += 1
                c.delete(hp_sled[2])
                hp_sled[2] = c.create_rectangle(7, 7, 7+(151*(hp_igroka/100)), 38, fill='green')
                options = {"fill": "green","font":"Times 15","width": 200, "text": f"+10/+10/+1"}
                yroni += [[c.create_text((i[1][0], i[1][1]),**options),[i[1][0],i[1][1]],i[1][1],"+10/+10/+1","green","Times 15"]]
            else:
                hp_igroka += 1
                if(hp_igroka > 100):
                    hp_igroka = 100
                Pivo += 1
                c.delete(hp_sled[2])
                hp_sled[2] = c.create_rectangle(7, 7, 7+(151*(hp_igroka/100)), 38, fill='green')
                options = {"fill": "green","font":"Times 15","width": 200, "text": f"+1/+1"}
                yroni += [[c.create_text((i[1][0], i[1][1]),**options),[i[1][0],i[1][1]],i[1][1],"+1/+1","green","Times 15"]]
            Patroni()
            c.delete(i[0])
            Aptetka.remove(i)
    w1.after(30,Aptetka_podnato) 

def Yron_podnalsa():
    global yroni
    for i in yroni:
        ttt = 5
        c.delete(i[0])
        options = {"fill": f"{i[4]}","font":i[5],"width": 200, "text": i[3]}
        if(i[1][1]>i[2]-70):
            if(ttt > 1):
                ttt -= 3
            i[1][1]-=ttt
            i[0] = [c.create_text((i[1][0], i[1][1]),**options)]
        if(i[1][1]<=i[2]-70):
            c.delete(i[0])
            yroni.remove(i)
    w1.after(30,Yron_podnalsa)

w1 = Tk()
w1.geometry('1200x870')
w1.resizable(False, False)

w1.bind('<Motion>', on_mouse_move)
w1.bind('<Button-1>', lambda event: tochka())
w1.bind('<Button-2>', lambda event: tochka1())
w1.bind('<Button-3>', lambda event: tochka2())

c = Canvas(w1, height=870, width=1200, bg='black')
c.pack()

hp_sled = [c.create_rectangle(5, 5, 160, 40, fill='white'),c.create_rectangle(7, 7, 158, 38, fill='black'),c.create_rectangle(7, 7, 7+(151*(hp_igroka/100)), 38, fill='green')]
options3 = {"fill": "white","font":"Times 30","width": 200, "text": f"{Pivo}"}
options7 = {"fill": "orange","font":"Times 30","width": 200, "text": f"{Mina}"}
options8 = {"fill": "red","font":"Times 30","width": 200, "text": f"Убито: {Ybito}"}
Mina_cifri = [c.create_text((245, 24),**options7)]
Pivo_cifri = [c.create_text((185, 24),**options3)]
Ybito_cifri = [c.create_text((1100, 24),**options8)]

Vova += [c.create_rectangle(x, y, x + 10, y + 10, fill='white')]

Vova_idot()
Shabanov_prihshol()
Shabanov_idot()
Pyla_dyra_idot()
KD()
KD_yron()
Yron_podnalsa()
Aptetka_prihshol()
Aptetka_podnato()
Mina_bah()

w1.mainloop()