# Define the gene sequence 
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'  
  
# Define the repeat elements
repeat_elements = ['GTGTGT', 'GTCTGT']  
  
# Write a function to count the total number of repetitive elements
def count_repetitive_elements(sequence, elements):  
    count = 0
    for i in range(len(sequence) - 5):   
        for element in elements: 
            if sequence[i:i+6] == element:
                count += 1  
                break
    return count 
  
# Call the function and print the result 
total_repeats = count_repetitive_elements(seq, repeat_elements)  
print(f"Total number of repetitive elements: {total_repeats}") 
  
  
