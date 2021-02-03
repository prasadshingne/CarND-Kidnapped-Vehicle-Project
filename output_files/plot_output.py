#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:41:01 2021

@author: sprasad
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=6)     # fontsize of the axes title
plt.rc('axes', labelsize=6)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=6)    # fontsize of the tick labels
plt.rc('ytick', labelsize=6)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


#%% read data

data_column        = ["deltat","x","y","theta"]

output_file_name100   = "pf_100.out"
output_file_name001   = "pf_1.out"  
output_file_name002   = "pf_2.out"  
output_file_name003   = "pf_3.out" 
data100 = pd.read_csv(output_file_name100, sep = " ", names = data_column, index_col=False)
data001 = pd.read_csv(output_file_name001, sep = " ", names = data_column, index_col=False)
data002 = pd.read_csv(output_file_name002, sep = " ", names = data_column, index_col=False)
data003 = pd.read_csv(output_file_name003, sep = " ", names = data_column, index_col=False)

mapdata = pd.read_csv("../data/map_data.txt", sep = "\t", names = ["x","y","num"])
# %% create time array
data100["time"] = np.cumsum(data100["deltat"])
data100["r"]    = np.sqrt(data100["x"]*data100["x"]+data100["y"]*data100["y"])

data001["time"] = np.cumsum(data001["deltat"])
data001["r"]    = np.sqrt(data001["x"]*data001["x"]+data001["y"]*data001["y"])

data002["time"] = np.cumsum(data002["deltat"])
data002["r"]    = np.sqrt(data002["x"]*data002["x"]+data002["y"]*data002["y"])

data003["time"] = np.cumsum(data003["deltat"])
data003["r"]    = np.sqrt(data003["x"]*data003["x"]+data003["y"]*data003["y"])
#%% plot position

fig = plt.figure(figsize=(3.2, 2.5))
plt.scatter(mapdata["x"],mapdata["y"], s = 25, marker = "+", color = 'k', linewidths=1, label = "Map Data")
plt.scatter(data100["x"],data100["y"], s = 1, marker = "x", color = 'b', linewidths=1, label = "N_particles = 100")
plt.scatter(data001["x"],data001["y"], s = 1, marker = "+", color = 'r', linewidth=1, label = "N_particles = 1")
plt.scatter(data003["x"],data003["y"], s = 1, marker = "|", color = 'g', linewidth=1, label = "N_particles = 3")

plt.grid(color = 'k', ls = '--', lw = 0.5)
plt.legend(loc='lower right', prop={'size': 6})
plt.xlabel('X (units)')
plt.ylabel('Y (units)')
plt.title('Predicted Position [X,Y]')
fig.savefig( 'Compare_predictions'+'_position.jpg', dpi = 300)
plt.xlim(100.0, 200.0)
plt.ylim(-40, 0)
fig.savefig( 'Compare_predictions'+'_position_zoom1.jpg', dpi = 300)
plt.xlim(75, 125)
plt.ylim(-40, -20)
fig.savefig( 'Compare_predictions'+'_position_zoom1.jpg', dpi = 300)
#%% plot R vs time
fig = plt.figure(figsize=(3.2, 2.5))
plt.scatter(data100["time"],data100["r"], s = 1, marker = "x", color = 'b', linewidths=1, label = "N_particles = 100")
plt.scatter(data001["time"],data001["r"], s = 1, marker = "+", color = 'r', linewidth=1, label = "N_particles = 1")
plt.scatter(data003["time"],data003["r"], s = 1, marker = "|", color = 'g', linewidth=1, label = "N_particles = 3")
plt.grid(color = 'k', ls = '--', lw = 0.5)
plt.legend()
plt.xlabel('time (sec)')
plt.ylabel('R (units)')
plt.title('R vs time')
fig.savefig('Compare_r'+'_rmse.jpg', dpi = 300)
# plt.ylim(0.0, 1.0)
# fig.savefig('Compare_r_theta'+'_rmse_zoom_y.jpg', dpi = 300)
#%%
fig = plt.figure(figsize=(3.2, 2.5))
plt.scatter(data100["time"],data100["theta"], s = 1, marker = "x", color = 'b', linewidths=1, label = "N_particles = 100")
plt.scatter(data001["time"],data001["theta"], s = 1, marker = "+", color = 'r', linewidth=1, label = "N_particles = 1")
plt.scatter(data003["time"],data003["theta"], s = 1, marker = "|", color = 'g', linewidth=1, label = "N_particles = 3")

plt.grid(color = 'k', ls = '--', lw = 0.5)
plt.legend()
plt.xlabel('time (sec)')
plt.ylabel('theta (units)')
plt.title('theta vs time')
fig.savefig('Compare_theta'+'.jpg', dpi = 300)
plt.xlim(30, 70)
plt.ylim(3, 4)
fig.savefig('Compare_theta'+'zoom.jpg', dpi = 300)