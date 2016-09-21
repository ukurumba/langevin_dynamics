
with open('{}'.format(potential_energy_file)) as potential_energy_vals:
        values = []
        for line in potential_energy_vals: 
            vals = [float(i) for i in line.split()] #Source: http://stackoverflow.com/questions/19555472/change-a-string-of-integers-separated-by-spaces-to-a-list-of-int
            values.append(vals)
        values = np.asarray(values)

def potential_energy_force(pos, array_of_energy_values):
    def find_nearest(array,value):
        #source: http://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
        positions = np.array(array)[:,1]
        idx = (np.abs(positions-value)).argmin()
        return idx
    
    def find_second_nearest(array,pos,idx):
        positions = np.array(array)[:,1]
        if positions[idx]-pos == 0:
            return idx
        else:
            actual_value = positions[idx]
            positions[idx] = positions[idx] + pos + 80000.999 
            index = (np.abs(positions-pos)).argmin()
            positions[idx] = actual_value
            return index
        
    
    nearest = find_nearest(values,pos)
    second_nearest = find_second_nearest(values,pos,nearest)
    
    pot_energy_force = -1*(values[nearest,2]-values[second_nearest,2])/(values[nearest,1]-values[second_nearest,1])
        
    return pot_energy_force


    
    
    
    
