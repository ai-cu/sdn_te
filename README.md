# sdn_te
CS4450 stuff

Hello and welcome to a_team's final project on software-defined network traffic engineering!

Instructions on how to run the code:

Within VSCode (what our team used), press Run All within the TE_4450 notebook for all cells to run.

This will output topology.png (representing the overall topo), circ_1 (representing traffic allocations for max throughput),
circ_2 (representing traffic allocations for minimizing MLU).

Alternatively, https://colab.research.google.com/drive/1hO7_JP-rNrpw1ErL8xJrHaNTI9Ih-SxN?usp=sharing
Use the link above and upload the 'nodes.txt', 'demand.txt' and 'topology.txt' files. Then press Runtime -> Run All

You can also upload any of the larger topologies that we generated for the extra credit section as long as you either change the 
file name references in code where we designated via comments, or renamed the files to names above. 

All the generated files are in the generated_networks folder and the script generating them is in network_gen.py