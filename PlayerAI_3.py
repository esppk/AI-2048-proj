# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:51:25 2017

@author: esppk
"""



from BaseAI_3 import BaseAI

 
class PlayerAI(BaseAI):
    def getMove(self, grid):
        depth = 4
        moves = grid.getAvailableMoves()
        move_dict = dict()
        for m in moves:
            gr = grid.clone()
            gr.move(m)
            reward = self.alphabeta(gr, depth, -9999, 9999, "p1")
            move_dict[reward] = m
        r = list(move_dict.keys())
        r.sort()
        return move_dict[r[-1]]
        
        
    
    
    def hueristic(self, g):

        empty = g.getAvailableCells()
        E = len(empty)
        max_v = g.getMaxTile
        corner = [(0,g.size),(g.size, g.size),
                  (g.size, 0), (0,0)]
        
        for c in corner:
            if g.getCellValue(c) == max_v:
                M = 10
            else:
                M = 0
        
        #calculate distance and smoothness
#        d_list = []
        #penalty for non-monoticity
        row = []
        P = 0
        for i in range(g.size):
            for j in range(g.size):
                cell = g.getCellValue((i,j))
                if cell != 0:
                    dist = min(i,j)
                    P += cell*dist
                    row.append(cell)
                    
        
        #penalty for non-monoticity
        N = 0
        col = []
        for i in range(g.size):
            for j in range(g.size):
                cell = g.getCellValue((j,i))
                if cell != 0:
                    col.append(cell)
                            
        col_s = col.copy()
        col_s.sort()
        for i in range(len(col_s)):
            N+=(col[i] - col_s[i])**2
            
        row_s = row.copy()
        row_s.sort()
        for i in range(len(row_s)):
            N+=(row[i] - row_s[i])**2
            
            
        
        reward = 4096*E - 10*P + M - 20*N
        return reward
        
    
    def alphabeta(self, grid, depth , alpha, beta, turn):
        
        if (depth == 0) or (grid.getAvailableMoves() == []):

            return self.hueristic(grid)
        
        if turn == "p1":
     
            for move_ in grid.getAvailableMoves():
                child = grid.clone()
                child.move(move_)
                
                alpha_temp= self.alphabeta(child, depth -1, alpha, beta, "p2")
                alpha = max(alpha, alpha_temp)
                if beta <= alpha:
                    break 
            return alpha
        else:
   
            
            for move_ in grid.getAvailableMoves():
                child = grid.clone()
                child.move(move_)

                beta_temp = self.alphabeta(child, depth -1, alpha, beta, "p1")
                beta = min(beta, beta_temp)
                if beta<=alpha:
                    break
                
            return beta
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
                    
                    