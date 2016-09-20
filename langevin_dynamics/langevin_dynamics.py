# -*- coding: utf-8 -*-
def potential_energy_force(position, potential_energy_file):
    potential_energy_vals = open('{}'.format(potential_energy_file))
    values = []
    for line in potential_energy_vals: 
        vals = [int(i) for i in line.split()] #Source: http://stackoverflow.com/questions/19555472/change-a-string-of-integers-separated-by-spaces-to-a-list-of-int
        values.append(vals)
    values = np.asarray(values)
    def find_nearest(array,value):
        #source: http://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
        positions = np.array(array)[:,1]
        idx = (np.abs(positions-value)).argmin()
        return idx
    nearest = find_nearest(values,position)
    
    def find_second_nearest(array,position,idx):
        positions = np.array(array)[:,1]
        if positions[idx]-position == 0:
            return idx
        else:
            positions[idx] = positions[idx] + position + 80000 
            idx = (np.abs(positions-position)).argmin()
            return idx
    second_nearest = find_second_nearest(values,position,nearest)
    
    if nearest < second_nearest:
        pot_energy_force = -1*(values[nearest,2]-values[second_nearest,2])/(values[nearest,1]-values[second_nearest,1])
    elif nearest > second_nearest:
        pot_energy_force = (values[nearest,2]-values[second_nearest,2])/(values[nearest,1]-values[second_nearest,1])
    elif nearest == second_nearest:
        pot_energy_force = values[nearest,3]
        
    return pot_energy_force
    
        
            
    
    
    
    
