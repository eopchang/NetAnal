#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#networkx로 생성된 그래프 객체를 cytoscape에 import할 수 있는 엑셀파일로 저장해주는 모듈
"""
Created on Sun Mar 26 20:28:22 2017

@author: Chang-Eop
"""

import os
os.chdir('/Users/Chang-Eop/Desktop/GitHub/NetAnal')


import pandas as pd
import networkx as nx

def interactions(G, title):
    G.edges()
    G_dic_frame = pd.DataFrame(G.edges(), columns = ['node 1', 'node 2']) #단순 interaction 쌍 without attribute
    
    #연결 정보 저장
    G_dic_frame.to_excel(title + '.xlsx') 
    
   

def node_attr(G, title):
    #
    G_dic_frame_node = pd.DataFrame(G.nodes(), columns = ['node name'])
    attrs_node = list(list(G.node.values())[0])
    for i in attrs_node:
        node_attr = list(nx.get_node_attributes(G,i).values())
        G_dic_frame_node[i+' (attr)'] = node_attr
        
    #node attribute 저장                 
    G_dic_frame_node.to_excel(title + '.xlsx')