def extract_duplicate_genes(fasta_file):  
    with open(fasta_file, 'r') as file:  
        genes = {}  
        for line in file:  
            if line.startswith('>'):  
                header = line.strip('>').strip()  
                current_gene = ''  
                continue  
            current_gene += line.strip()  
            if 'duplication' in header:  
                gene_name = header.split()[0]  # Assume gene name is the first word in the header    
                genes[gene_name] = current_gene  
    return genes  
  
# Define the path to the fasta file  
fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'  

# Extract duplicate genes  
duplicate_genes = extract_duplicate_genes(fasta_file)  
  
# Write a new fasta file  
with open('duplicate_genes.fa', 'w') as outfile:  
    for gene_name, sequence in duplicate_genes.items():  
        outfile.write(f'>{gene_name}\n{sequence}\n')