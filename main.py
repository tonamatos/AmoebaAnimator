# Config submodule
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "FerGroup"))
from FerGroup import Fer_group as Fer

# Graph and animation imports
import networkx as nx
from manim import *
config.pixel_height     = 480
config.pixel_width      = 480
config.background_color = BLACK
edge_color              = WHITE

# ---

G = nx.path_graph(7) # Generate a graph
K = Fer(G)           # Find Fer group
fer = K.non_aut[-1]  # Get a replacement

# Define manim scene
class Amoeba_scene(Scene):
   def animate_fer(self, fer, G, G_manim):
      '''
      fer is a Fer object. Output is a manim animation to be put in self.play.
      '''
      edge_seq = fer.sequence

      for i, ind_fer in enumerate(edge_seq):
        old_i, old_j = ind_fer.old_edge
        if old_i > old_j:
          _ = old_i

          old_i = old_j
          old_j = _

        new_i, new_j = ind_fer.new_edge
        if new_i > new_j:
          _ = new_i
          new_i = new_j
          new_j = _

        run_time = 0.15

        old_edge = G_manim.edges[(old_i,old_j)].copy()
        new_edge = Line(G_manim[new_i], G_manim[new_j], color=edge_color)
        G_manim.remove_edges((old_i,old_j))
        self.play(Transform(old_edge,new_edge),rate_func=linear, run_time=run_time)
        G_manim.add_edges((new_i,new_j))
        G_manim.edges[(new_i,new_j)].stroke_color = edge_color
        self.remove(old_edge,new_edge)

   def construct(self):
      G_manim = Graph(list(G.nodes), list(G.edges),
                layout="spring",
                layout_scale=6,
                labels=False)
      self.add(G_manim)
      self.animate_fer(fer, G, G_manim)
      self.wait()