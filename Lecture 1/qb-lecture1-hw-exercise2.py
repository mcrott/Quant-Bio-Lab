import graphviz as gv
import os
os.environ['PATH'] += os.pathsep + r"C:\Program Files\Graphviz\bin"

reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']



k = 3

kmer_edge = []
edges = open('qb-quant-edges-exercise-2.txt','w')
reads_combo = "".join(reads)
n = len(reads_combo) - k
for i in range(n):
    first = reads_combo[i:i+k]
    last = reads_combo[i+1:i+(k+1)]
    if first[1:] == last[:(k-1)]:
        edges.write(f"{first} -> {last}\n")
        kmer_edge.append((first,last))

        
edges.close()
        
#2.2
"""
Done with pythons venv libray, no need for conda

although I had to install graphviz to my C: drive
"""

#2.3,2.4
"""

"""
dot = gv.Digraph('k-mer-3',comment='3 mer graph for lecture 1 exercise 2')

dot.format = ("png")

for start,end in kmer_edge:
    dot.edge(start,end)
dot.render(directory='3mer').replace("\\","/")