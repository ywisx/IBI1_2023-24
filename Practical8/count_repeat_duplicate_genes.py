from get_duplicate_genes import extract_duplicate_genes,write_genes_file
from repetitive_counter import count_repetitive_elements

  
# Get user input until got corrent sequence
repeat_pattern=""
while True:
    repeat_pattern = input("Please enter the repetitive sequence (GTGTGT or GTCTGT): ")  
    if repeat_pattern != "GTGTGT" and repeat_pattern != "GTCTGT":
        print("Wrong sequence! Please input again\n")
        continue
    else:
        break

# Extract duplicate genes  
duplicate_genes = extract_duplicate_genes()  
  
# Calculate the number of duplicate sequences in each duplicate gene  
for index, gene in enumerate(duplicate_genes):
    number = count_repetitive_elements(gene["seq"], repeat_pattern)
    # need to update "name" in list, YBR024W_mRNA => YBR024W_mRNA 1
    duplicate_genes[index]["name"] = f'{gene["name"]} {number}'
    # remove \r\n so that the entire sequence is on one line
    no_crlf = gene["seq"].replace("\r", "").replace("\n", "")
    duplicate_genes[index]["seq"] = no_crlf + "\n"

# set the output file name  
output_file_name = f'{repeat_pattern}_duplicate_genes.fa'  
  
# Write the results to a new fasta file name  
write_genes_file(output_file_name, duplicate_genes)
