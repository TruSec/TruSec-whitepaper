# This code computes a minimium total dominating set approximation.
import random


def compute_mtds(G):
    # T-O(1) S-O(1) NE-O(1)
    if G.is_directed():
        raise Exception("Parameter graph should be undirected")

    # 1.a Each vertex v_i chooses random float r_i in range 0<r_i<1
    for node in G.nodes:
        G.nodes[node]["rand_val"] = random.uniform(0, 1)
        print(f'rand_val={G.nodes[node]["rand_val"]}')
    # 1.b Each vertex v_i computes d_i. d_i=degree of vertex v_i
    for node in G.nodes:
        G.nodes[node]["degree"] = G.nodes[node]["degree"] = G.degree(node)
        print(f'degree={G.nodes[node]["degree"]}')
    # 1.c Each vertex v_i computes weight: w_i=d_i+r_i
    for node in G.nodes:
        G.nodes[node]["weight"] = G.nodes[node]["degree"] + G.nodes[node]["rand_val"]
        print(f'weight={G.nodes[node]["weight"]}')

    # 1.d Each vertex v_i sends w_i to each of its neighbours.max.
    # TODO: paradigm: Either each neuron sends some value to another neuron.
    # OR: each neuron asks/demands some value of each of its neighbours.
    for node in G.nodes:
        max = 0
        for neighbor in G.neighbors(node):
            if max < G.nodes[neighbor]["rand_val"]:
                max = G.nodes[neighbor]["rand_val"]

    # 2.a Each vertex v_i gets the index of the
    # neighbouring vertex v_j_(w_max) that has the heighest w_i, with i!=j.
    # 2.b Each vertex v_i adds a mark to that neighbour vertex v_j_(w_max).

    # 3 for k in range [0,m] rounds, do:

    # 4.a Each node v_i computes how many marks it has received, as (x_i)_k.
    # 4.b Each node v_i computes (w_i)_k=(x_i)_k+ r_i

    # 5. Reset marked vertices: for each vertex v_i, (x_i)_k=0

    # 6.a Each vertex v_i computes d_i. d_i=degree of vertex v_i
    # 6.b Each vertex v_i sends w_i to each of its neighbours.
    # 6.c Each vertex v_i gets the index of the
    # neighbouring vertex v_j_(w_max) that has the heighest w_i, with i!=j.
    # 6.d Each vertex v_i adds a mark to that neighbour vertex v_j_(w_max).