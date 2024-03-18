#プレデター・プレイモデル(ロトカーヴォルテカ方程式)
#→捕食者と獲物の個体数が時間とともにどのように変化するか記述

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
"""↑解説
・scipy→科学技術計算を行うためのPythonライブラリ
scipy.integrate→数値積分や常微分方程式(ODE)の開放に関する関数を含む
odeint→常微分方程式を解くための関数
"""

#パラメータ
alpha=1.0
beta=0.1
delta=0.075
gamma=1.5

#ロトカ-ヴォルテラ方程式
def lotka_volterra(y,t,alpha,beta,delta,gamma):
    #prey→獲物 predator→捕食者
    prey,predator=y
    dydt=[alpha * prey - beta*prey*predator,delta*prey*predator-gamma*predator]
    return dydt

#初期値
y0=[10,5]

#時間の範囲
t=np.linspace(0,50,1000)

#微分方程式を解く
sol=odeint(lotka_volterra,y0,t,args=(alpha,beta,delta,gamma))

#結果をプロット
plt.plot(t,sol[:,0],label='Prey')
plt.plot(t,sol[:,1],label='Predator')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()