# count the total number of repetitive element in the sequence
def count_repetitive_elements(sequence, element):  
    count = 0
    start = 0
    # string.find(substring, start=0, end=len(string))
    n =sequence.find(element, start)
    while n >= 0:
        count += 1
        # increment start for next find match
        start = n + len(element)
        n = sequence.find(element, start)
    return count 
  
# as this module can be import from
if __name__=='__main__':
    # Define the gene sequence 
    seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'  
    # Define the repeat elements
    repeat_elements = ['GTGTGT', 'GTCTGT']  
    
    total_repeats = 0
    for element in repeat_elements: 
        repeats = count_repetitive_elements(seq, element)  
        print(f"Repetitive element '{element}': {repeats}") 
        total_repeats += repeats

    print(f"Total number of repetitive: {total_repeats}") 
  
