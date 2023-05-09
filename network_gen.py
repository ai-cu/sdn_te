import random

def generate_network(num_nodes, net_dens = 0.5, avg_edge_cap = 1000000000, 
                     edge_cap_rand = 0, time_stamps = 100, avg_demand = 20000, demand_rand = 1, 
                     edge_prob_fail = 0.004):
  node_file_name = str(num_nodes) + "nodes.txt"
  with open(node_file_name, 'a') as f:
    i = 0
    while (i < num_nodes):
        f.write(str(i) + '\n')
        i += 1


  topology_file_name = str(num_nodes) + "topology.txt"
  with open(topology_file_name, 'a') as g:
    i = 0
    while (i < num_nodes):
        j = 0
        while (j < num_nodes):
            has_edge = (random.random() < (num_nodes*net_dens)/num_nodes) and (i != j)
            if (has_edge):
                edge_cap = avg_edge_cap+((random.uniform(-1*edge_cap_rand, edge_cap_rand))*avg_edge_cap)
                g.write(str(j) + " " + str(i) + " " + str(int(edge_cap)) + " " + str(edge_prob_fail) + '\n')
            j += 1
        i += 1


  demand_file_name = str(num_nodes) + "demand.txt"
  with open(demand_file_name, 'a') as h:
    k = 0
    while (k < time_stamps):
        node_demands = ""
        i = 0
        while (i < num_nodes):
            j = 0
            while (j < num_nodes):
                if (i != j):
                    demand = avg_demand+((random.uniform(-1*demand_rand, demand_rand))*avg_demand)
                    node_demands += (str(demand) + " ")
                j += 1
            i += 1
        h.write(node_demands[:-1] + '\n')
        k += 1

generate_network(5, 0.4, 1000000000, 0)
generate_network(10, 0.4, 1000000000, 0)
generate_network(20, 0.3, 1000000000, 0)
generate_network(35, 0.4, 1000000000, 0)
generate_network(55, 0.4, 1000000000, 0)
generate_network(80, 0.4, 1000000000, 0)
generate_network(110, 0.4, 1000000000, 0)
generate_network(145, 0.4, 1000000000, 0)
generate_network(185, 0.3, 1000000000, 0)
generate_network(230, 0.3, 1000000000, 0)
generate_network(280, 0.3, 1000000000, 0)
generate_network(350, 0.3, 1000000000, 0)