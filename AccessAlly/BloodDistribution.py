# No specific modules required

'''
List of blood group match
    'O-' <= 'O-'
    'O+' <= 'O+', 'O-'
    'A-' <= 'A-', 'O-'
    'A+' <= 'A+', 'A-', 'O+', 'O-'
    'B-' <= 'B-', 'O-'
    'B+' <= 'B+', 'B-', 'O+', 'O-'
    'AB-' <= 'O-', 'A-', 'B-', 'AB-'
    'AB+' <='O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+'
'''

# We will use global variables as we will need them in several functions
# List of blood types
blood = ['O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+']
# Dictionary of blood types with their match sorted
# (The lists are sorted as to provide maximum units possible)
match_list = {
    'O-' : ['O-'],
    'O+' : ['O+', 'O-'],
    'A-' : ['A-', 'O-'],
    'A+' : ['A+', 'A-', 'O+', 'O-'],
    'B-' : ['B-', 'O-'],
    'B+' : ['B+', 'B-', 'O+', 'O-'],
    'AB-': ['O-', 'A-', 'B-', 'AB-'],
    'AB+': ['O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+']
}

def supply_blood(bloodtype: str, patients:dict, bloodmatch: list, units: dict) -> None:
    '''
    supply_blood tries to find maximum number of units of blood possible for a patient of a blood type
    
    bloodtype   (str): the blood group of patient
    patients   (dict): blood group is the key, number of patients of that group is the value
    bloodmatch (list): list of blood groups suitable for patient with 'bloodtype'
    units      (dict): blood group is the key, number of units available is the key
    
    Effects: dictionaries are mutated in a way that patient count and blood unit count are decreased
    '''
    
    for match in bloodmatch:                        
    # We iterate through each blood group matched for the patient's blood group
        if units[match] and patients[bloodtype]:
        # if either no. of patients needing blood is zero or the units of blood aren't available, we won't loop
            # print('Blood type:', bloodtype,', Number:', patients[bloodtype], ', Blood match:',match, ', Units:', units[match])
            if units[match] >= patients[bloodtype]:     # We have enough blood for patients
                units[match] -= patients[bloodtype]
                patients[bloodtype] = 0
            else:
                patients[bloodtype] -= units[match]     # We don't have enough blood hence other blood groups are required
                units[match] = 0
            # print('Post','Blood type:', bloodtype,', Number:', patients[bloodtype],', Blood match:',match, ', Units:', units[match])
    
def treat_patients(units:dict, patients:dict) -> int:
    '''
    treat_patients goes through each patient of each bloodgroup and supply blood from available units to them
    
    units      (dict): blood group is the key, number of units available is the key
    patients   (dict): blood group is the key, number of patients of that group is the value
    
    Effects: dictionaries are mutated such that there is decrease in patient count and blood unit count
    '''
    
    earlier_sum = sum(patients.values()) # We first check number of patients needing blood
    # print(earlier_sum)
    
    for bloodtype in blood:             # we go through each blood groups of patients who need help
        if patients[bloodtype]:
            # print(bloodtype, patients, match_list[bloodtype], units)
            supply_blood(bloodtype, patients, match_list[bloodtype], units)
            # A particular blood group of patients is cured or minimized and now we move onto next group
            # print(units)
            # print(patients)
            
    final_sum = sum(patients.values())  # We count the number of patients that are not cured
    return (earlier_sum - final_sum)      # This is the number of patients we could provide blood to optimally!!

if __name__ == '__main__':
    units = input().split(' ')                  # Get the units of blood of each type
    units = list(map(lambda x: int(x), units))
    blood_units = dict(zip(blood, units))
    
    patients = input().split(' ')               # Get the no. of patients of each type
    patients = list(map(lambda x: int(x), patients))
    patients_blood = dict(zip(blood, patients))
    
    print(treat_patients(blood_units, patients_blood))