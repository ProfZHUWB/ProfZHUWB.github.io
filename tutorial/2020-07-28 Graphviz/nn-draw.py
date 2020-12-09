# -*- coding: utf-8 -*-
"""
基于 Craffel 的代码修改，原代码见： https://gist.github.com/craffel/2d727968c3aaebd10359
"""

import matplotlib.pyplot as plt

def draw_neural_net(ax, left, right, bottom, top, layer_sizes,nodeFontSize=15,edgeFontSize=12):
    '''
    Draw a neural network cartoon using matplotilb.
    
    :usage:
        >>> fig = plt.figure(figsize=(12, 12))
        >>> draw_neural_net(fig.gca(), .1, .9, .1, .9, [4, 7, 2])
    
    :parameters:
        - ax : matplotlib.axes.AxesSubplot
            The axes on which to plot the cartoon (get e.g. by plt.gca())
        - left : float
            The center of the leftmost node(s) will be placed here
        - right : float
            The center of the rightmost node(s) will be placed here
        - bottom : float
            The center of the bottommost node(s) will be placed here
        - top : float
            The center of the topmost node(s) will be placed here
        - layer_sizes : list of int
            List of layer sizes, including input and output dimensionality
    '''
    n_layers = len(layer_sizes)
    v_spacing = (top - bottom)/float(max(layer_sizes))
    h_spacing = (right - left)/float(len(layer_sizes) - 1)
    # Nodes
    for n, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
        cx = n*h_spacing + left
        for m in range(layer_size):
            # (cx, cy) center of node
            cy = layer_top - m*v_spacing
            R = v_spacing/4.
            textY = cy - 0.03*v_spacing
            if n == 0:
                rect = plt.Rectangle((cx-R,cy-R),2*R,2*R, zorder=4, color='w', ec='k')
                ax.add_artist(rect)
                label =  r'$X_{'+str(m+1)+'}$'
                plt.text(cx -0.03*h_spacing, textY, label, fontsize=nodeFontSize, zorder=5)
            else:
                circle = plt.Circle((cx, cy), R, color='w', ec='k', zorder=4) 
                ax.add_artist(circle)
                
                if n < n_layers-1:
                    label =  r'$H_{'+str(n)+","+str(m+1)+'}$'
                    plt.text(cx -0.05*h_spacing, textY, label, fontsize=nodeFontSize, zorder=5)
                else:
                    label =  r'$O_{'+str(m+1)+'}$'
                    plt.text(cx -0.03*h_spacing, textY, label, fontsize=nodeFontSize, zorder=5)
            
    # Edges
    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.

        # (mx, my) center for node m in layer a
        # (ox, oy) cetner for node o in layer b
        mx = n*h_spacing + left
        for m in range(layer_size_a):
            ox = mx + h_spacing
            my = layer_top_a - m*v_spacing
            
            for o in range(layer_size_b):
                oy = layer_top_b - o*v_spacing
                line = plt.Line2D([mx, ox], [my, oy], c='k')
                ax.add_artist(line)
                
                # length from center of node m to node o
                import numpy as np
                dx = ox - mx
                dy = oy - my
                
                
                rot_mo_rad = np.arctan(dy/dx)
                rot_mo_deg = rot_mo_rad*180./np.pi                
                
                t = (m+0.6) / (1+layer_size_a)
                textLoc = np.array([mx + t * dx, my + t * dy])
                trans_angle = ax.transData.transform_angles(np.array((rot_mo_deg,)),textLoc.reshape((1, 2)))[0]
                print("-------")
                print("mx: {0:.3f}, ox: {1:.3f}, dx: {2:.3f},  t: {3:.3f}, tx: {4:.3f}".format(mx,ox,dx,t,textLoc[0]))
                print("my: {0:.3f}, oy: {1:.3f}, dy: {2:.3f},  t: {3:.3f}, ty: {4:.3f}".format(my,oy,dy,t,textLoc[1]))
                label = r'$W_{'+str(n+1)+','+str(m+1)+','+str(o+1)+'}$'
                plt.text(textLoc[0], textLoc[1]+0.05*v_spacing, label, rotation=trans_angle, rotation_mode='anchor', fontsize=edgeFontSize, zorder=5)
                

fig = plt.figure(figsize=(12,12))
draw_neural_net(fig.gca(), 0.1, 0.9, 0.1, 0.9, [2,4,2])