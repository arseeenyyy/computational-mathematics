import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

class Plotter:
    def plot_equation(self, func: Callable, description: str):
        x_center = 0
        for attempt in range(3):
            x = np.linspace(x_center-5, x_center+5, 1000)
            y = func(x)
            
            mask = (np.abs(y) < 20) & (~np.isnan(y))
            if np.any(mask):
                x = x[mask]
                y = y[mask]
                break
            x_center += 5
        
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
        
        plt.title(f"Function: {description}", pad=20, fontsize=14)
        plt.xlabel("x", fontsize=12, color='#4a7b9d')
        plt.ylabel("f(x)", fontsize=12, color='#4a7b9d')
        plt.grid(True, linestyle=':', alpha=0.7)
        plt.legend(framealpha=0.9, loc='upper right')
    
        plt.margins(0.05)        
        plt.show()