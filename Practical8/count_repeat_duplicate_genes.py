from get_duplicate_genes import extract_duplicate_genes  
  
def count_repeats_in_genes(genes, repeat_pattern):  
    genes_with_repeats = {}  
    for gene_name, sequence in genes.items():  
        repeat_count = sequence.count(repeat_pattern)  
        genes_with_repeats[gene_name] = (repeat_count, sequence)  
    return genes_with_repeats  
  
def write_genes_with_repeats_to_fasta(genes_with_repeats, output_file):  
    with open(output_file, 'w') as outfile:  
        for gene_name, (repeat_count, sequence) in genes_with_repeats.items():  
            outfile.write(f'>{gene_name}_{repeat_count}\n{sequence}\n')  
  
  
# Get user input  
repeat_pattern = input("Please enter the repetitive sequence (GTGTGT or GTCTGT): ")  

# Extract duplicate genes  
duplicate_genes = extract_duplicate_genes('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')  
  
# Calculate the number of duplicate sequences in each duplicate gene  
genes_with_repeats = count_repeats_in_genes(duplicate_genes, repeat_pattern)  
  
# Create the output file name  
output_file_name = f'{repeat_pattern}_duplicate_genes.fa'  
  
# Write the results to a new fasta file name  
write_genes_with_repeats_to_fasta(genes_with_repeats, output_file_name)

