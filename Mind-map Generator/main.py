import tkinter as tk
from tkinter import messagebox
import spacy
import matplotlib.pyplot as plt
import networkx as nx
import random
import os
from collections import Counter
from datetime import datetime

nlp = spacy.load("en_core_web_sm")

class MindMapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mind Map Generator")
        self.graph = None
        self.pos = None
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Mind Map Title:", font=("Arial", 12)).pack(pady=(10, 0))
        self.title_entry = tk.Entry(self.root, width=40, font=("Arial", 12))
        self.title_entry.pack(pady=(0, 10))

        self.text_entry = tk.Text(self.root, height=10, width=60, font=("Arial", 12))
        self.text_entry.pack(padx=10, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Generate Mind Map", command=self.generate_mind_map,
                  font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)

        tk.Button(button_frame, text="Export as Image", command=self.export_image,
                  font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

    def extract_keywords(self, text):
        doc = nlp(text.lower())
        keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]
                    and not token.is_stop and token.is_alpha and len(token.text) > 2]
        most_common = Counter(keywords).most_common(15)
        return [word.capitalize() for word, _ in most_common]

    def generate_mind_map(self):
        title = self.title_entry.get().strip() or "Mind Map"
        text = self.text_entry.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Input Error", "Please enter some text.")
            return

        keywords = self.extract_keywords(text)
        if not keywords:
            messagebox.showinfo("No Keywords", "No valid keywords found.")
            return

        self.draw_mind_map(title, keywords)

    def draw_mind_map(self, title, keywords):
        G = nx.Graph()
        G.add_node(title)

        for keyword in sorted(set(keywords)):
            G.add_node(keyword)
            G.add_edge(title, keyword)

        self.graph = G
        self.pos = nx.spring_layout(G, k=1.3, seed=42)
        self.display_graph(title)

    def display_graph(self, title):
        plt.figure(figsize=(14, 12))
        node_sizes = [5000 if node == title else 2500 for node in self.graph.nodes]
        node_colors = [
            "#ff6666" if node == title
            else random.choice(["#66b3ff", "#99ff99", "#ffcc99", "#ffb3e6", "#c2c2f0"])
            for node in self.graph.nodes
        ]

        nx.draw_networkx_nodes(self.graph, self.pos, node_color=node_colors,
                               node_size=node_sizes, edgecolors='black', linewidths=1.5)
        nx.draw_networkx_edges(self.graph, self.pos, width=2, edge_color='gray')

        for node, (x, y) in self.pos.items():
            label_size = 10 if len(node) < 15 else 8
            plt.text(x, y, node, fontsize=label_size, ha='center', va='center',
                     fontweight='bold', fontname='Arial',
                     bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

        plt.title(title, fontsize=18, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    def export_image(self):
        if not self.graph or not self.pos:
            messagebox.showwarning("No Mind Map", "Generate a mind map before exporting.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"mind_map_{timestamp}.png"
        title = self.title_entry.get().strip() or "Mind Map"

        plt.figure(figsize=(14, 12))
        node_sizes = [5000 if node == title else 2500 for node in self.graph.nodes]
        node_colors = [
            "#ff6666" if node == title
            else random.choice(["#66b3ff", "#99ff99", "#ffcc99", "#ffb3e6", "#c2c2f0"])
            for node in self.graph.nodes
        ]

        nx.draw_networkx_nodes(self.graph, self.pos, node_color=node_colors,
                               node_size=node_sizes, edgecolors='black', linewidths=1.5)
        nx.draw_networkx_edges(self.graph, self.pos, width=2, edge_color='gray')

        for node, (x, y) in self.pos.items():
            label_size = 10 if len(node) < 15 else 8
            plt.text(x, y, node, fontsize=label_size, ha='center', va='center',
                     fontweight='bold', fontname='Arial',
                     bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

        plt.title(title, fontsize=18, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(filename, dpi=300)
        messagebox.showinfo("Saved", f"Mind map exported as {os.path.abspath(filename)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MindMapApp(root)
    root.mainloop()
