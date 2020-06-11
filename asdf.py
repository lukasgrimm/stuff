import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def cap_var_swap(vol,cap,vol_strike):
    return min(cap,(vol**2))-(vol_strike**2)

def vol_swap(vol,vol_strike):
    return vol - vol_strike

vol_swap_strike = 14
var_swap_strike = 16
var_swap_cap = 40**2

pnl = []
vola = []
long_var_swap = []
short_vol_swap = []
for r in range(0,100,1):
    pnl.append(cap_var_swap(r,var_swap_cap,var_swap_strike)-32*vol_swap(r,vol_swap_strike))
    long_var_swap.append(cap_var_swap(r,var_swap_cap,var_swap_strike))
    short_vol_swap.append(-1*32*vol_swap(r,vol_swap_strike))
    vola.append(r)
plt.plot(vola,pnl,"g",long_var_swap,"b",short_vol_swap,"r")
plt.show()