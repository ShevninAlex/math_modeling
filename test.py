from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
from random import random 
 
 
def circle_move(k, t):
    x = t
    y = k * t
    return x, y
 
 
def animate(i):
    for j in range(10):
        balls[i].set_data(circle_move(k=koeff[j], t=i))
 
 
if __name__ == '__main__':
 
    fig, ax = plt.subplots()

    balls = []
    for i in range(10):
        ball, = plt.plot([], [], 'o', color='r', label='Ball')
        balls.append(ball)
    
    koeff = []
    for i in range(10):
        koeff.append(random())
        
    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=np.linspace(0, 3, 100),
                        interval=30
                       )
    
    ani.save('test1.gif')