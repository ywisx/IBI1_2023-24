def favourite_bond_actor(birth_year):    
    bond_actors = {    
        'Roger Moore': (1973, 1986),    
        'Timothy Dalton': (1987, 1994),    
        'Pierce Brosnan': (1995, 2005),  
        'Daniel Craig': (2006, 2021) 
    }    
    turn_18_year = birth_year + 18    
    for actor, (start_year, end_year) in bond_actors.items():    
        if start_year <= turn_18_year:  
            if end_year is None or turn_18_year < end_year:  
                return actor    
    return "No Bond actor during their 18th year"    
  
# Example:  
print(favourite_bond_actor(1980)) # output should be 'Roger Moore'

