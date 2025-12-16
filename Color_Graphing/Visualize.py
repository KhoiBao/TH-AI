import tkinter as tk
from tkinter import messagebox
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def ToMau(G, nodes):
    colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Cyan", "Pink"] # list of colors
    color_dict = {n: colors[:] for n in nodes} # dict = key / value, where nodes at this moment stored as string or int/float, its mean A:"Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Cyan", "Pink" and go on
    
    degree = [sum(G[i]) for i in range(len(G))]
    
    sorted_nodes = [n for _, n in sorted(zip(degree, nodes), reverse=True)] # sort reversedly because "which node have highest degree colored first"
    
    solution = {}

    for n in sorted_nodes:
        available = color_dict[n]
        solution[n] = available[0]
        
        for j in range(len(G)):
            if G[nodes.index(n)][j] == 1 and available[0] in color_dict[nodes[j]]: #check have this colored being used yet? and have it connected to near by node yet?
                
                color_dict[nodes[j]].remove(available[0]) # yes, proceed not using the same color for it
    return solution

# ---------- Random Graph Generator  ----------
def generate_graph(num_nodes):
    while True:
        G = [[0]*num_nodes for _ in range(num_nodes)]
        # Randomly add edges
        for i in range(num_nodes):
            for j in range(i+1, num_nodes):
                if random.random() < 0.4: # only 40% that the node itself connect eachother
                    G[i][j] = G[j][i] = 1 # 0 = not connect || 1 = connect

                    #G =  A  B  C  D
                        #[0, 1, 0, 1],
                        #[1, 0, 1, 0],
                        #[0, 1, 0, 1],
                        #[1, 0, 1, 0]
                            

        # Ensure at least one node has degree >= 3
        degrees = [sum(row) for row in G]
        if any(d >= 3 for d in degrees):
            return G

# ---------- Draw Graph ----------
def draw_graph(ax, adj_matrix, colors=None, nodes=None):
    G = nx.Graph()
    for i in range(len(nodes)): # type: ignore
        G.add_node(nodes[i]) # type: ignore
    for i in range(len(nodes)):# type: ignore
        for j in range(i+1, len(nodes)):# type: ignore
            if adj_matrix[i][j] == 1:
                G.add_edge(nodes[i], nodes[j])# type: ignore

    pos = nx.spring_layout(G, seed=42)
    if colors:
        node_colors = [colors[n] for n in nodes]# type: ignore
    else:
        node_colors = "lightgray"

    nx.draw(
        G, pos, with_labels=True, node_color=node_colors,
        node_size=800, font_weight="bold", font_color="black", ax=ax
    )
    return pos

# ---------- Main App ----------
class GraphColoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Coloring Visualizer")
        self.root.geometry("950x600")

        self.nodes = []
        self.adj_matrix = []
        self.solution = {}

        # Controls
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Number of nodes:").grid(row=0, column=0, padx=5)
        self.entry_nodes = tk.Entry(control_frame, width=5)
        self.entry_nodes.grid(row=0, column=1)

        tk.Button(control_frame, text="Generate Graph", command=self.generate_and_show).grid(row=0, column=2, padx=10)

        # Canvas for Matplotlib
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.result_label = tk.Label(root, text="", font=("Consolas", 12))
        self.result_label.pack(pady=10)

    def generate_and_show(self):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        try:
            n = int(self.entry_nodes.get()) # constraint user numbers of nodes
            if n < 4 or n > 20:
                messagebox.showwarning("Warning", "Nhập tối đa 4 đến 20 nodes")
                return
        except ValueError:
            messagebox.showerror("Error", "Hãy nhập số.")
            return

        self.nodes = [chr(65 + i) for i in range(n)] # chr is ASCII coded and convert it to string, 65 stand for A, +1 for everytime will lead to other alphabet such as 66 is B,...
        self.adj_matrix = generate_graph(n)
        self.solution = ToMau(self.adj_matrix, self.nodes)

        # Plot before and after
        fig, axes = plt.subplots(1, 2, figsize=(9, 4.5))
        fig.subplots_adjust(wspace=0.3)
        axes[0].set_title("Before Coloring")
        axes[1].set_title("After Coloring")

        draw_graph(axes[0], self.adj_matrix, colors=None, nodes=self.nodes)
        draw_graph(axes[1], self.adj_matrix, colors=self.solution, nodes=self.nodes)

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

        # Show color result
        result_text = "\n".join([f"{n}: {c}" for n, c in self.solution.items()])
        self.result_label.config(text=result_text)


# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphColoringApp(root)
    root.mainloop()
