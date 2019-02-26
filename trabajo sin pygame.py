import matplotlib.pyplot as plt
from scipy.special import jn
import numpy as np
import math as ma

def pos_1(lista): #De vuelve las posiciones en que los elementos valen "1"
    ret=[]
    for i in range(len(lista)):
        if lista[i]==1:
            ret.append(i)
    return ret
def t_menor_periodo(tiempo,periodo):
    if tiempo<=periodo:
        return tiempo
    else:
        t_nueva=tiempo-periodo
        return t_menor_periodo(t_nueva,periodo)
def rad(x): #Conversor a radianes
    return(2*ma.pi*x/360)
def pos_el(el,lista): #Busca la posicion de un elemento en una lista
    pos=-1
    for i in range(len(lista)):
        if lista[i]==el:
            pos=i
        
    if pos==-1:
        return -23
    else:
        return pos
def sumatoria(tope,epsilon,periodo,tiempo):
    sumatoria=0
    cont=1
    while cont<=tope:
        sumatoria=sumatoria+(2/cont)*jn(cont,cont*epsilon)*ma.sin(2*ma.pi*tiempo*cont/periodo)
        cont=cont+1
    return sumatoria
def gira(pos,angulo): #Funcion que me hara el giro segun el parametro "w" del planeta
    if len(pos)!=2:
        return 'Error: posicion distinta a 2'
    else:
        return [pos[0]*ma.cos(angulo)-pos[1]*ma.sin(angulo),ma.sin(angulo)*pos[0]+ma.cos(angulo)*pos[1]]
    
G=6.674e-11 #Constante grav. universal
M=1.989e30 #Masa Solar
nu=M*G*((1.49e11)**(-3))*86400**2 #Conversion segundo-dia y metro-unidad astronomica
      
p1=['Mercurio',0.387,0.206,87.97,rad(28.76),'b',3.302e23]
p2=['Venus',0.723,0.007,224.7,rad(54.37),'g',4.869e24]
p3=['Tierra',1,0.017,365.26,rad(101.22),'c',5.9722e24]
p4=['Marte',1.524,0.093,686.98,rad(285.44),'r',6.4185e23]
p5=['Jupiter',5.203,0.048,4332.6,rad(273.28),'y',1.899e27]
p6=['Saturno',9.546,0.056,10759,rad(338.3),'m',5.688e26]
p7=['Urano',19.2,0.047,30687,rad(95.57),'k',8.686e25]
p8=['Neptuno',30.09,0.009,60784,rad(273.15),'b',1.024e26]
Planetas=[p1,p2,p3,p4,p5,p6,p7,p8]
#Aux=['me',p1,'ve',p2,'ti',p3,'ma',p4,'ju',p5,'sa',p6,'ur',p7,'ne',p8]

import tkinter as tk
from tkinter import font #Cambia fuentes y letra
from tkinter import messagebox

class Window(tk.Frame): #Window nombre opcional, Frame obligatorio
    def __init__(self, master = None): #Ventana vacia
        tk.Frame.__init__(self, master)
        
        self.master = master
        
        self.init_window() #init_window will be defined later
        
    def init_window(self):
        
        self.master.title('Trabajo Mecanica')#Name of the window
        
        self.pack(fill=tk.BOTH, expand=1)
        
        label_tiempo=tk.Label(self,text='Tiempo(Dias):',relief=tk.GROOVE)
        label_tiempo.pack()
        label_tiempo.place(x=3,y=18)
        tiempo=tk.Spinbox(self,from_=0,to=200,fg='grey',width=5)
        tiempo.pack()
        self.tiempo=tiempo
        tiempo.place(x=85,y=18)
        ######################################
        Fuente_calc=font.Font(family="Times", size=10, weight=font.BOLD)
        Conj_planetas=tk.LabelFrame(self,text="Planetas",padx=1,pady=1,font=Fuente_calc)
        Conj_planetas.pack(padx=10, pady=10)
        
        pl1=tk.IntVar(self)
        pl1.set(0)
        self.pl1=pl1
        mer=tk.Checkbutton(Conj_planetas, text='Mercurio',fg='red',variable=pl1,command=self.mer_check)
        mer.pack(anchor=tk.W)
        self.mer=mer
        
        pl2=tk.IntVar(self)
        pl2.set(0)
        self.pl2=pl2
        ven=tk.Checkbutton(Conj_planetas, text='Venus',fg='red',variable=pl2,command=self.ven_check)
        ven.pack(anchor=tk.W)
        self.ven=ven
        
        pl3=tk.IntVar(self)
        pl3.set(0)
        self.pl3=pl3
        tie=tk.Checkbutton(Conj_planetas, text='Tierra',fg='red',variable=pl3,command=self.tie_check)
        tie.pack(anchor=tk.W)
        self.tie=tie
        
        pl4=tk.IntVar(self)
        pl4.set(0)
        self.pl4=pl4
        mar=tk.Checkbutton(Conj_planetas, text='Marte',fg='red',variable=pl4,command=self.mar_check)
        mar.pack(anchor=tk.W)
        self.mar=mar
        
        pl5=tk.IntVar(self)
        pl5.set(0)
        self.pl5=pl5
        jup=tk.Checkbutton(Conj_planetas, text='Jupiter',fg='red',variable=pl5,command=self.jup_check)
        jup.pack(anchor=tk.W)
        self.jup=jup
        
        pl6=tk.IntVar(self)
        pl6.set(0)
        self.pl6=pl6
        sat=tk.Checkbutton(Conj_planetas, text='Saturno',fg='red',variable=pl6,command=self.sat_check)
        sat.pack(anchor=tk.W)
        self.sat=sat
        
        pl7=tk.IntVar(self)
        pl7.set(0)
        self.pl7=pl7
        ura=tk.Checkbutton(Conj_planetas, text='Urano',fg='red',variable=pl7,command=self.ura_check)
        ura.pack(anchor=tk.W)
        self.ura=ura
        
        pl8=tk.IntVar(self)
        pl8.set(0)
        self.pl8=pl8
        nep=tk.Checkbutton(Conj_planetas, text='Neptuno',fg='red',variable=pl8,command=self.nep_check)
        nep.pack(anchor=tk.W)
        self.nep=nep
        
        Conj_planetas.place(x=3,y=60)
        
        caja_resultados=tk.Listbox(self,width=80,height=26, highlightbackground = "black")
        caja_resultados.pack()
        caja_resultados.place(x=200,y=64)
        caja_resultados.insert(tk.END,'Introduzca los datos y presione "calcular".')
        self.caja_resultados=caja_resultados
        caja_resultados.configure(font=font.Font(family="Arial",size=9))
        Fuente_res=font.Font(family="Times", size=11, weight=font.BOLD)
        Resultado=tk.Label(self,text='Datos obtenidos:',bg='grey',font=Fuente_res)
        Resultado.pack()
        Resultado.place(x=400,y=45)
        ###########################################
        Boton_calculo=tk.Button(self,text='Calcula',width=10,height=1,font=Fuente_calc,bg = "green",command=self.calcula_datos)
        Boton_calculo.pack()
        Boton_calculo.place(x=90,y=80)
        self.Boton_calculo=Boton_calculo
        
        Boton_plot2D=tk.Button(self,text='Grafica 2D',width=10,height=1,font=Fuente_calc,bg = "green",command=self.dibuja_datos)
        Boton_plot2D.pack()
        Boton_plot2D.place(x=90,y=110)
        self.Boton_plot2D=Boton_plot2D
        
        Boton_plot3D=tk.Button(self,text='Grafica 3D',width=10,height=1,font=Fuente_calc,bg = "green",command=self.not_yet)
        Boton_plot3D.pack()
        Boton_plot3D.place(x=90,y=135)
        self.Boton_plot3D=Boton_plot3D
        ##########################################
        caja_info=tk.Listbox(self,width=31,height=10, highlightbackground = "blue")
        caja_info.pack()
        caja_info.place(x=3,y=320)
        self.caja_info=caja_info
        caja_info.insert(tk.END,'...')
        self.caja_info=caja_info
        Fuente_info=font.Font(family="Times", size=12, weight=font.BOLD)
        infor=tk.Label(self,text=' ? ',font=Fuente_info,bg='blue',fg='white',highlightbackground = "black")
        infor.pack()
        infor.place(x=83,y=298)
        
        Fuente_infos=font.Font(family="Times", size=10, weight=font.BOLD)
        
        info_calcula=tk.Label(self,text=' ? ',font=Fuente_infos,bg='black',fg='white',highlightbackground = "black")
        info_calcula.pack()
        info_calcula.place(x=171,y=82)
        info_calcula.bind("<Enter>", self.ha_entrado_c)
        info_calcula.bind("<Leave>", self.ha_salido_c)
        
        info_2D=tk.Label(self,text=' ? ',font=Fuente_infos,bg='black',fg='white',highlightbackground = "black")
        info_2D.pack()
        info_2D.place(x=171,y=111)
        info_2D.bind("<Enter>", self.ha_entrado_2d)
        info_2D.bind("<Leave>", self.ha_salido_2d)
        
        info_3D=tk.Label(self,text=' ? ',font=Fuente_infos,bg='black',fg='white',highlightbackground = "black")
        info_3D.pack()
        info_3D.place(x=171,y=137)
        info_3D.bind("<Enter>", self.ha_entrado_3d)
        info_3D.bind("<Leave>", self.ha_salido_3d)
        ############################################
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        
        file = tk.Menu(menu)
        file.add_command(label='Info', command=self.client_info)
        file.add_command(label='Cerrar', command=self.client_exit)
        menu.add_cascade(label='Archivo', menu=file)
        
        fuen = tk.Menu(menu)
        fuen.add_command(label='Times', command=self.times)
        fuen.add_command(label='Courier New', command=self.cou)
        fuen.add_command(label='Arial', command=self.aria)
        fuen.add_command(label='Comic Sans MS', command=self.comic)
        fuen.add_command(label='Symbol', command=self.symb)
        fuen.add_command(label='Verdana', command=self.verd)
        fuen.add_command(label='Fixedsys', command=self.fide)
        menu.add_cascade(label='Fuente', menu=fuen)
        
    def times(self):
        fuente_func=font.Font(family="Times",size=9)
        self.caja_resultados.configure(font=fuente_func)
    def cou(self):
        fuente_func=font.Font(family="Courier New",size=9)
        self.caja_resultados.configure(font=fuente_func)
    def aria(self):
        fuente_func=font.Font(family="Arial",size=9)
        self.caja_resultados.configure(font=fuente_func)
    def comic(self):
        fuente_func=font.Font(family="Comic Sans MS",size=9)
        self.caja_resultados.configure(font=fuente_func)
    def symb(self):
        fuente_func=font.Font(family="Symbol",size=9)
        self.caja_resultados.configure(font=fuente_func)
    def verd(self):
        fuente_func=font.Font(family="Verdana",size=9)
        self.caja_resultados.configure(font=fuente_func)
    def fide(self):
        fuente_func=font.Font(family="Fixedsys",size=9)
        self.caja_resultados.configure(font=fuente_func)
        
    def client_info(self):
        self.caja_info.delete(0,tk.END)
        self.caja_info.insert(tk.END,'En esta ventana se mostraran')
        self.caja_info.insert(tk.END,'posicion, distancia al sol,')
        self.caja_info.insert(tk.END,'velocidad, masa, etc, de los') 
        self.caja_info.insert(tk.END,'planetas que se seleccionen')
        self.caja_info.insert(tk.END,'en el tiempo introducido.')
    def client_exit(self):
        exit()
    def ha_entrado_c(self,typ):
        self.caja_info.delete(0,tk.END)
        self.caja_info.insert(tk.END,'Se calcularan los datos pedidos')
        self.caja_info.insert(tk.END,'para los planetas escogidos,')
        self.caja_info.insert(tk.END,'para ello introduzca un valor') 
        self.caja_info.insert(tk.END,'numerico en "tiempo"no negativo.')
    def ha_salido_c(self,typ):
        self.caja_info.delete(0,tk.END)
        self.caja_info.insert(tk.END,'...')
    def ha_entrado_2d(self,typ):
        self.caja_info.delete(0,tk.END)
        self.caja_info.insert(tk.END,'Se mostraran las trayectorias de ')
        self.caja_info.insert(tk.END,'los planetas escogidos, asi como ') 
        self.caja_info.insert(tk.END,'su posicion en ellas, para ello') 
        self.caja_info.insert(tk.END,'introduzca un valor numerico en') 
        self.caja_info.insert(tk.END,'"tiempo" no negativo.')
    def ha_salido_2d(self,typ):
        self.caja_info.delete(0,tk.END)
        self.caja_info.insert(tk.END,'...')
    def ha_entrado_3d(self,typ):
        self.caja_info.delete(0,tk.END)
        self.caja_info.insert(tk.END,'Aun en proceso, mostrara las')
        self.caja_info.insert(tk.END,'trayectorias \n de los planetas') 
        self.caja_info.insert(tk.END,'en 3 dimensiones.')
    def ha_salido_3d(self,typ):
        self.caja_info.delete(0,tk.END)
        self.caja_info.insert(tk.END,'...')
    def mer_check(self):
        aux=self.pl1.get()
        if aux==1:
            self.mer.configure(fg='green')
        else:
            self.mer.configure(fg='red')
    def ven_check(self):
        aux=self.pl2.get()
        if aux==1:
            self.ven.configure(fg='green')
        else:
            self.ven.configure(fg='red')
    def tie_check(self):
        aux=self.pl3.get()
        if aux==1:
            self.tie.configure(fg='green')
        else:
            self.tie.configure(fg='red')
    def mar_check(self):
        aux=self.pl4.get()
        if aux==1:
            self.mar.configure(fg='green')
        else:
            self.mar.configure(fg='red')
    def jup_check(self):
        aux=self.pl5.get()
        if aux==1:
            self.jup.configure(fg='green')
        else:
            self.jup.configure(fg='red')
    def sat_check(self):
        aux=self.pl6.get()
        if aux==1:
            self.sat.configure(fg='green')
        else:
            self.sat.configure(fg='red')
    def ura_check(self):
        aux=self.pl7.get()
        if aux==1:
            self.ura.configure(fg='green')
        else:
            self.ura.configure(fg='red')
    def nep_check(self):
        aux=self.pl8.get()
        if aux==1:
            self.nep.configure(fg='green')
        else:
            self.nep.configure(fg='red')
    
    def not_yet(self):
         self.Boton_plot3D.configure(bg='grey')
         messagebox.showwarning('Aviso','Estamos trabajando en ello.')
    def dibuja_datos(self):
        try:
            a=float(self.tiempo.get())
            Planetas_seleccionados=[self.pl1.get(),self.pl2.get(),self.pl3.get(),self.pl4.get(),self.pl5.get(),self.pl6.get(),self.pl7.get(),self.pl8.get()]
            cont=0
            for p in Planetas_seleccionados:
                cont=cont+p
            if float(a)<0:
                self.Boton_plot2D.configure(bg='red')
                messagebox.showerror('Error de datos introducidos','La entrada de tiempo no es valida,\n no se admiten tiempos negativos...')
                self.caja_resultados.insert(tk.END,)
            elif cont==0:
                self.Boton_plot2D.configure(bg='yellow')
                messagebox.showerror('Error de datos introducidos','No se ha seleccionado ningun planeta...')
            else:
                self.Boton_plot2D.configure(bg='green')
                Posiciones=pos_1(Planetas_seleccionados)
                Planetas_elegidos=[Planetas[i] for i in Posiciones]
                for p in Planetas_elegidos:
                    t=a
                    u=(2*ma.pi*t/p[3])+sumatoria(5000,p[2],p[3],t)
                    pos=[p[1]*(ma.cos(u)-p[2]),p[1]*ma.sqrt(1-p[2]**2)*ma.sin(u)]
                    pos_fin=gira(pos,p[4])
                    x=[]
                    y=[]
                    for i in np.linspace(0,p[3]*1.2,200):
                        u=(2*ma.pi*i/p[3])+sumatoria(5000,p[2],p[3],i)
                        pos_sin_girar=[p[1]*(ma.cos(u)-p[2]),p[1]*ma.sqrt(1-p[2]**2)*ma.sin(u)]
                        [a,b]=gira(pos_sin_girar,p[4])
                        x.append(a)
                        y.append(b)
                    plt.plot(x,y,linewidth=2.1,color=p[5] ,label=p[0])
                    plt.plot([pos_fin[0]],[pos_fin[1]],'bo')
                plt.plot([0],[0],'ro',label='Sol')
                plt.legend()
                plt.axis('equal')
                plt.show()
        except:
            self.Boton_plot2D.configure(bg='red')
            messagebox.showerror('Error de datos introducidos','No se han introducido datos \n numericos en "Tiempo"')
    def calcula_datos(self):
        try:
            a=float(self.tiempo.get())
            Planetas_seleccionados=[self.pl1.get(),self.pl2.get(),self.pl3.get(),self.pl4.get(),self.pl5.get(),self.pl6.get(),self.pl7.get(),self.pl8.get()]
            cont=0
            for p in Planetas_seleccionados:
                cont=cont+p
            if float(a)<0:
                self.Boton_calculo.configure(bg='red')
                self.caja_resultados.delete(0,tk.END)
                self.caja_resultados.insert(tk.END,'La entrada de tiempo no es valida, no se admiten tiempos negativos...')
            elif cont==0:
                self.Boton_calculo.configure(bg='yellow')
                self.caja_resultados.delete(0,tk.END)
                self.caja_resultados.insert(tk.END,'No se ha seleccionado ningun planeta...')
            else:
                self.Boton_calculo.configure(bg='green')
                self.caja_resultados.delete(0,tk.END)
                Posiciones=pos_1(Planetas_seleccionados)
                Planetas_elegidos=[Planetas[i] for i in Posiciones]
                for p in Planetas_elegidos:
                    t=a
                    u=(2*ma.pi*t/p[3])+sumatoria(5000,p[2],p[3],t)
                    pos=[p[1]*(ma.cos(u)-p[2]),p[1]*ma.sqrt(1-p[2]**2)*ma.sin(u)]
                    pos_fin=gira(pos,p[4])
                    self.caja_resultados.insert(tk.END,p[0]+':')
                    self.caja_resultados.insert(tk.END,'Masa(kg): '+str(p[6]))
                    self.caja_resultados.insert(tk.END,'Posicion(uA): '+str(pos_fin))
                    dist=ma.sqrt(pos_fin[0]**2+pos_fin[1]**2)
                    self.caja_resultados.insert(tk.END,'Distancia al sol(uA): '+str(dist))
                    vel_sin_giro=[((p[1]*2*ma.pi)/(p[3]*(1-p[2]*ma.cos(u))))*(-ma.sin(u)),((p[1]*2*ma.pi)/(p[3]*(1-p[2]*ma.cos(u))))*ma.sqrt(1-p[2]**2)*ma.cos(u)]
                    vel=gira(vel_sin_giro,p[4])
                    mod_vel=ma.sqrt(vel[0]**2+vel[1]**2)
                    self.caja_resultados.insert(tk.END,'Velocidad(uA/Dia): '+str(vel))
                    self.caja_resultados.insert(tk.END,'Modulo de la velocidad: '+str(mod_vel))
                    energia=p[6]*(((p[1]*2*ma.pi/(p[3]*(1-ma.cos(u)*p[2])))**2)*(1-ma.cos(u)*p[2]**2)/2-nu/(p[1]*(1+p[2]*ma.cos(u))))
                    self.caja_resultados.insert(tk.END,'Energia del planeta(kg*uA^2/Dia^2) mediante definicion: '+str(energia))
                    mom_ang=[0,0,pos_fin[0]*vel[1]-pos_fin[1]*vel[0]]
                    self.caja_resultados.insert(tk.END,'Energia obtenida a partir de los parametros del sistema(kg*uA^2/Dia^2): '+str((-1)*p[6]*nu/(2*p[1])))
                    self.caja_resultados.insert(tk.END,'Momento angular en funcion de los parametros del sistema: '+str(ma.sqrt(p[1]*nu*(1-p[2]**2))))
                    self.caja_resultados.insert(tk.END,'Momento angular mediante su definicion: '+str(mom_ang))
                    self.caja_resultados.insert(tk.END,'Anomalia excentrica(Rad): '+str(u))
                    if t==0:
                        real=ma.acos(int((((1-p[2]**2)/(1-p[2]*ma.cos(u)))-1)/p[2]))
                    else:
                        real=ma.acos((((1-p[2]**2)/(1-p[2]*ma.cos(u)))-1)/p[2])
                        
                    self.caja_resultados.insert(tk.END,'Anomalia real a partir de la excentrica(Rad): '+str(real))
                    def f(z):
                        return z-p[2]*ma.sin(z)-2*ma.pi*t/p[3]
                    def f_d(z):
                        return 1-p[2]*ma.cos(z)
                    u_newt_raph=0
                    inr=0
                    while inr<1000:
                        u_newt_raph=u_newt_raph-f(u_newt_raph)/f_d(u_newt_raph)
                        inr=inr+1
                    self.caja_resultados.insert(tk.END,'Anomalia excentrica por metodo de Newton Raphson(Rad): '+str(u_newt_raph))
                    c=ma.sqrt(p[1]*nu*(1-p[2]**2))
                    def theta(x,y):
                        return c/((p[1]**2)*(1-p[2]**2)**2)*(1+p[2]*ma.cos(y))**2
                    def RungeKutta(a,im_a,b,l): #a y b los valores de x inicial y tope,im_a el valor imagen inicial de a,t el tamanyo de paso
                        if b<a:
                            return('Error 1: los intervalos en que se quieren aproximar los valores no tienen sentido...')
                        elif b==a:
                            return [a,im_a]
                        else:
                            def K1(x,y,s):
                                return theta(x,y)
                            def K2(x,y,s):
                                return theta(x+s/2,y+K1(x,y,s)*s/2)
                            def K3(x,y,s):
                                return theta(x+s/2,y+K2(x,y,s)*s/2)
                            def K4(x,y,s):
                                return theta(x+s/2,y+K3(x,y,s)*s)
                            
                            RK=[a,im_a]
                            itera=a
                            valor_itera=im_a
                            while itera<=b:
                                valor_itera=valor_itera+(K1(itera,valor_itera,l)+2*K2(itera,valor_itera,l)+2*K3(itera,valor_itera,l)+K4(itera,valor_itera,l))*t/6
                                itera=itera+l
                                RK=[itera,valor_itera]
                            return RK
                    rk=RungeKutta(0,0,t,0.5)
                    self.caja_resultados.insert(tk.END,'Valor de la anomalia real por Runge kutta clasico(Rad): '+str(rk[1]))
                    self.caja_resultados.insert(tk.END,'El area barrida es:'+str(c*t/2))
                    
                    self.caja_resultados.insert(tk.END,'\n')
        except:
            self.Boton_calculo.configure(bg='red')
            self.caja_resultados.delete(0,tk.END)
            self.caja_resultados.insert(tk.END,'La entrada de tiempo no es valida, no se ha introducido un valor numerico')
                
            
root = tk.Tk()
root.geometry('775x500') #Specifies the dimensions of the window
app = Window(root)
root.mainloop() #genera la ventana
