from graphviz import Digraph

dot = Digraph(comment='Cancer Inquiry Logic')

# Nodes
dot.node('A', 'Cancer Site?')
dot.node('B', 'Yes')
dot.node('C', 'No, end')
dot.node('D', 'Site Details')
dot.node('E', '1° or 2°?')
dot.node('F', '1°')
dot.node('G', '2°')
dot.node('H', '1° Subtype')
dot.node('I', '1° Stage (TNM)')
dot.node('J', '1° Dx Method')
dot.node('K', '1° Tx')
dot.node('L', 'Recur?')
dot.node('M', 'Yes')
dot.node('N', 'No')
dot.node('O', 'Recur When')
dot.node('P', 'Recur Dx')
dot.node('Q', 'Recur Tx')
dot.node('R', 'Recur Tx Plan')
dot.node('S', '2° 1° Site')
dot.node('T', '2° Site Detail')
dot.node('U', '2° Dx Method')
dot.node('V', '2° Tx')
dot.node('W', '2° Tx Plan')
dot.node('X', 'Another Site?')
dot.node('Y', 'Yes, Next')
dot.node('Z', 'No, end')
dot.node('AA', 'Biomarker')
dot.node('AB', 'Genetics')
dot.node('AC', 'Comorbid')
dot.node('AD', 'PS')

# Edges
dot.edge('A', 'B')
dot.edge('A', 'C')
dot.edge('B', 'D') 
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('E', 'G')
dot.edge('F', 'H')
dot.edge('H', 'I')
dot.edge('H', 'AA')
dot.edge('I', 'J')
dot.edge('AA', 'AB')
dot.edge('AB', 'J')
dot.edge('F', 'AC')
dot.edge('F', 'AD')
dot.edge('AC', 'K')
dot.edge('AD', 'K')
dot.edge('J', 'K')
dot.edge('K', 'L')
dot.edge('L', 'M')
dot.edge('L', 'N')
dot.edge('M', 'O')
dot.edge('O', 'P')
dot.edge('P', 'Q')
dot.edge('Q', 'R')
dot.edge('G', 'S')
dot.edge('G', 'T')
dot.edge('S', 'AC')
dot.edge('S', 'AD')
dot.edge('T', 'U')
dot.edge('T', 'AC')  
dot.edge('T', 'AD')
dot.edge('U', 'V')
dot.edge('V', 'W')
dot.edge('R', 'X')
dot.edge('W', 'X')
dot.edge('X', 'Y')
dot.edge('X', 'Z')
dot.edge('Y', 'D')

dot.attr(label=r'\nOptimized Cancer Inquiry Logic')
dot.attr(fontsize='20')

dot.render('optimized_cancer_inquiry_logic', view=True)
