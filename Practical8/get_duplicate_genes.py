# Define the path to the fasta file  
fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'  

# for str like ">xxxxx gene:YBR024W xxx" extract "YBR024W"
def extract_gene_name(str):
    start = str.find("gene:")
    if start < 0:
        return "N/A"
    
    end = str.find(" ", start)
    # extrace the name
    return str[start+5:end]    


# check each line, if start with ">", then append current gene into the list 
# then extrace the name and start a new gene
# otherwise  append the line as sequence into current gene object
def extract_duplicate_genes():  
    with open(fasta_file, 'r') as file:  
        geneList = []  
        curgene = None
        for line in file:  
            if line.startswith('>'):  
                if curgene != None:
                    # append last gene
                    geneList.append(curgene)
                    curgene = None

                idx = line.find("duplication")
                if  idx == -1:
                    continue
            
                # find a new duplicated gene
                curgene = {}
   
                # got the name, plug "_mRNA" according to the pdf examples
                curgene["name"] = extract_gene_name(line) + "_mRNA"
                curgene["seq"] = ""
            else: 
                if curgene != None:
                    # append current gene's remain line
                    curgene["seq"] += line        


    if curgene != None:
        # append last gene
        geneList.append(curgene)
    return geneList  
  
 
# Write a new fasta file with name and sequence
def write_genes_file(filename, gene_list):  
    with open(filename, 'w') as outfile:  
        for gene in gene_list:
            # each gene has a "name" and "seq"
            outfile.write(f'>{gene["name"]}\n{gene["seq"]}')

if __name__=='__main__':
    # extract all the genes whose sequence description contains ‘duplication’.
    duplicate_genes = extract_duplicate_genes()  
    write_genes_file("duplicate_genes.fa", duplicate_genes)
    
    print(f"Total number of duplicate_genes: {len(duplicate_genes)}") 
