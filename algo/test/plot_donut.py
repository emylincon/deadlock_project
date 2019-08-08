import matplotlib.pyplot as plt
import numpy as np
import random as r
import time
from drawnow import *



recipe = ["225 g flour",
          "90 g sugar",
          "1 egg",
          "60 g butter",
          "100 ml milk",
          "1/2 package of yeast",
          "225 g flour",
          "90 g sugar",
          "1 egg",
          "60 g butter",
          "225 g flour",
          "90 g sugar",
          "1 egg",
          "60 g butter",
          "100 ml milk"]

data = [277, 250, 267, 213, 274, 297]#[225, 90, 50, 60, 100, 5]

def gen_rand():
    global data
    data=[]
    for i in range(15):
        data.append(r.randint(50,300))

def plotme():
    print(data)
        
    #plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    wedges, texts = plt.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        plt.annotate(recipe[i], xy=(x, y), xytext=(np.sign(x),y),
                   horizontalalignment=horizontalalignment, **kw)

    plt.title("Matplotlib bakery: A donut")
    #plt.legend()
    #plt.show()

def plotme_easy():
    print(data)
        
    #fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    wedges, texts = plt.pie(data, wedgeprops=dict(width=0.5), startangle=-40, labels=recipe)

    #bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    #kw = dict(arrowprops=dict(arrowstyle="-"),
    #      bbox=bbox_props, zorder=0, va="center")

    #for i, p in enumerate(wedges):
        #ang = (p.theta2 - p.theta1)/2. + p.theta1
        #y = np.sin(np.deg2rad(ang))
        #x = np.cos(np.deg2rad(ang))
        #horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        #connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        #kw["arrowprops"].update({"connectionstyle": connectionstyle})
        #plt.annotate(recipe[i], xy=(x, y), xytext=(np.sign(x),y)
        #          horizontalalignment=horizontalalignment, **kw)

    plt.title("Matplotlib bakery: A donut")
    #plt.legend()
    #plt.show()

def main():
    while True:
        gen_rand()
        drawnow(plotme_easy)
        time.sleep(1)


main()
