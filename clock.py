#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:30:39 2018

@author: taylormade
"""

import matplotlib.pyplot as plt
labels = 'basketball', 'soccer', 'golf', 'baseball'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0.1, 0, 0, 0)
plt.pie(sizes, explode = explode, labels= labels, colors=colors, shadow=False, startangle=90)
plt.axis('equal')
plt.show()

