import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

class Plotter:
    def plot_equation(self, func: Callable, description: str):
        x_wide = np.linspace(-10, 10, 2000)
        y_wide = func(x_wide)
        
        mask = (~np.isnan(y_wide)) & (~np.isinf(y_wide)) & (np.abs(y_wide) < 1e10)
        x_wide = x_wide[mask]
        y_wide = y_wide[mask]
        
        roots = []
        for i in range(len(y_wide)-1):
            if y_wide[i] * y_wide[i+1] < 0:  
                roots.append(x_wide[i])
        
        if roots:  
            x_min, x_max = min(roots), max(roots)
            x_padding = max(2, 0.5 * (x_max - x_min))  
            x_focused = np.linspace(x_min - x_padding, x_max + x_padding, 1000)
            y_focused = func(x_focused)
            
            mask = (~np.isnan(y_focused)) & (~np.isinf(y_focused)) & (np.abs(y_focused) < 1e10)
            x_focused = x_focused[mask]
            y_focused = y_focused[mask]
            
            if len(y_focused) > 10:  
                x, y = x_focused, y_focused
            else:
                x, y = x_wide, y_wide
        else:
            x, y = x_wide, y_wide
        
        if len(y) > 0:
            y_min, y_max = np.min(y), np.max(y)
            y_range = y_max - y_min
            
            padding = max(0.5, 0.2 * y_range) if y_range > 0 else 1.0
            y_lim = (y_min - padding, y_max + padding)
        else:
            y_lim = (-5, 5)  
        
        plt.figure(figsize=(10, 6), facecolor='#f8f9fa')
        ax = plt.gca()
        
        ax.spines['bottom'].set_color('#4a7b9d')
        ax.spines['left'].set_color('#4a7b9d')
        ax.spines['bottom'].set_linewidth(1.5)
        ax.spines['left'].set_linewidth(1.5)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.plot(x, y, '#2c7be5', linewidth=2, label=f"f(x) = {description}")
        
        plt.axhline(0, color='#d62728', linestyle='--', alpha=0.7, linewidth=1)
        plt.axvline(0, color='#2ca02c', linestyle='--', alpha=0.7, linewidth=1)
        
        plt.xlim(x[0], x[-1])  
        plt.ylim(y_lim)
        
        plt.title(f"Function: {description}", pad=20, fontsize=14)
        plt.xlabel("x", fontsize=12, color='#4a7b9d')
        plt.ylabel("f(x)", fontsize=12, color='#4a7b9d')
        plt.grid(True, linestyle=':', alpha=0.7)
        plt.legend(framealpha=0.9, loc='upper right')
        
        plt.margins(0.05)
        plt.tight_layout()
        plt.savefig('graph.png')
        plt.show()

    def plot_system(self, system: dict):

        f1, f2 = system['system']
    
        def find_reasonable_range(func):
            for scale in [2, 5, 10, 20]:  
                x = np.linspace(-scale, scale, 100)
                X, Y = np.meshgrid(x, x)
                Z = func(X, Y)
                if np.any(np.abs(Z) < 10):  
                    return (-scale, scale)
            return (-5, 5)          
        range_x = find_reasonable_range(f1)
        range_y = find_reasonable_range(f2)
        view_range = (
            min(range_x[0], range_y[0]),
            max(range_x[1], range_y[1])
        )
        x = np.linspace(view_range[0], view_range[1], 200)
        y = np.linspace(view_range[0], view_range[1], 200)
        X, Y = np.meshgrid(x, y)
        
        plt.figure(figsize=(10, 8), facecolor='#f8f9fa')
        
        plt.contour(X, Y, f1(X, Y), levels=[0], colors='red', linewidths=2)
        plt.contour(X, Y, f2(X, Y), levels=[0], colors='blue', linewidths=2)
        
        plt.title(f"{system['description']}", pad=20, fontsize=14)
        plt.xlabel("x", fontsize=12, color='#4a7b9d')
        plt.ylabel("f(x)", fontsize=12, color='#4a7b9d')
        plt.grid(True, linestyle=':', alpha=0.5)
        plt.axhline(0, color='#d62728', linestyle='--', alpha=0.7, linewidth=1)
        plt.axvline(0, color='#2ca02c', linestyle='--', alpha=0.7, linewidth=1) 
        plt.gca().set_aspect('equal')
        
        plt.margins(0.1)
        plt.tight_layout()
        plt.show()