import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.special import factorial2
from numpy import sin,deg2rad
import numpy as np

r=np.linspace(40,218) #dominio de la grafica 

%matplotlib qt

def f_ang(theta): #esta función calcula el ángulo y es dependiente de la función Omega 
    serie=np.array([(factorial2(2*n-1)/factorial2(2*n)*(sin(deg2rad(theta)/2))**(2*n))**2 for n in range(1,120)])
    return 1+np.sum(serie)

def Omega(g,theta,M,R,L,mu,l,r,m): #se obtiene la frecuencia angular de oscilación (Ω)
    mu=mu/m
    M=M/m
    a_0=(g/(f_ang(theta)**2))*((M*R-mu/2*(l-L))/(M*R**2+mu/3*(L**2+l**2-l*L)))
    b_2=-1/(M*R**2+ mu/3*(L**2+l**2-l*L))
    omega_0=(a_0+(b_2*g*r)/(f_ang(theta)**2))/(1-b_2*r**2)
    return omega_0


go,thetao,Mo,Ro,Lo,muo,lo,mo=(9800,50,30,51,50,3.59,138,7) #valores guía para la gráfica 
fig=plt.figure() #crea la figura
ax=fig.subplots() #crea los ejes 
p,=plt.plot(r,Omega(go, thetao, Mo, Ro, Lo, muo, lo, r, mo),'-ok',color='darkblue') #establece en el eje x la "r" y en el eje y Ω
plt.subplots_adjust(left=0.10,bottom=0.45) #ajuste de la grafica left=ajusta a la izquierda botton=ajusta desde abajo 
plt.xlabel('Distancia masa al eje r (mm)',color='#2E2E2E',fontsize=15) #nombre y color del eje x 
plt.ylabel('Omega Ω²',color='#2E2E2E',fontsize=15)#nombre y color del eje y 
plt.suptitle('El enigma del metrónomo de Beethoven',fontsize=20,fontweight='bold') #título de la gráfica
plt.grid() #grilla 

#Aquí se crean los sliders de las variables 
#los axes crean los rectángulos en la gráfica para los sliders, botón de reinicio y el gráfico
ax1=plt.axes([0.15,0.06,0.65,0.03]) 
g_slider = Slider(ax=ax1,label='Gravedad', valmin=40,valmax=9807,valinit= go,orientation='horizontal')

ax2=plt.axes([0.15,0.10,0.65,0.03])
theta_slider = Slider(ax=ax2,label='Theta', valmin=40,valmax=60,valinit=thetao,orientation='horizontal')

ax3=plt.axes([0.15,0.14,0.65,0.03])
M_slider = Slider(ax=ax3,label='Masa Inferiror (M)', valmin=0.01,valmax=31.01,valinit=Mo,orientation='horizontal')

ax4=plt.axes([0.15,0.18,0.65,0.03])
R_slider = Slider(ax=ax4,label='Distancia masa inferior al eje (R)', valmin=35,valmax=70,valinit=Ro,orientation='horizontal')

ax5=plt.axes([0.15,0.22,0.65,0.03])
L_slider = Slider(ax=ax5,label='L', valmin=35,valmax=70,valinit=Lo,orientation='horizontal') #Distancia del eje hasta el extremo masa

ax6=plt.axes([0.15,0.26,0.65,0.03])
mu_slider = Slider(ax=ax6,label='Masa no despreciable varilla (μ)', valmin=0.01,valmax=3.59,valinit=muo,orientation='horizontal')

ax7=plt.axes([0.15,0.30,0.65,0.03])
l_slider = Slider(ax=ax7,label='Distancia del eje al final barilla (l)', valmin=130,valmax=200,valinit=lo,orientation='horizontal')

ax8=plt.axes([0.15,0.34,0.65,0.03])
m_slider = Slider(ax=ax8,label='Peso deslizante (m)', valmin=0.01,valmax=7.1,valinit=mo,orientation='horizontal')


def update(val): #ayuda a mover a los sliders 
    p.set_ydata(Omega(g_slider.val, theta_slider.val, M_slider.val, R_slider.val, L_slider.val, mu_slider.val, l_slider.val, r,m_slider.val))
    fig.canvas.draw_idle()
    
g_slider.on_changed(update)
theta_slider.on_changed(update)
M_slider.on_changed(update)
R_slider.on_changed(update)
L_slider.on_changed(update)
mu_slider.on_changed(update)
l_slider.on_changed(update)
m_slider.on_changed(update)

eliminar=plt.axes([0.89,0.065,0.10,0.05]) #botón reiniciar 
button=Button(eliminar,'Reiniciar',hovercolor='0.95') # hovercolor da un color claro al botón

def reset(evento): #esta función hace que al aplastar el botón reinicar vuelva a los parámetros establecidos
    g_slider.reset()
    theta_slider.reset()
    M_slider.reset()
    R_slider.reset()
    L_slider.reset()
    mu_slider.reset()
    l_slider.reset()
    m_slider.reset()
button.on_clicked(reset) #on_clicked permite al dar un click volver parámetros iniciales 

plt.show() #muestra la gráfica 