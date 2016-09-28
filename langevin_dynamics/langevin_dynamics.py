def langevin_simulation(init_position, init_velocity, temperature, damp_coeff, time_step, total_steps, potential_energy_file, mass, output_file_location="langevin_dynamics_output"):
    import numpy as np
    def potential_energy_force(position_particle, array_of_energy_values):
        array_of_energy_values = values
        def find_nearest(posit,array):
            #source: http://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
            positions = np.array(array)[:,1]
            idx = (np.abs(positions-posit)).argmin()
            
            return idx
        
        def find_second_nearest(posit, array, idx):
            positions = np.array(array)[:,1]
            if positions[idx]-posit == 0:
                return idx
            else:
                actual_value = positions[idx]
                positions[idx] = positions[idx] + 80000.999 
                index = (np.abs(positions-posit)).argmin()
                positions[idx] = actual_value
                return index
            
        
        nearest = find_nearest(position_particle,values)
        
        second_nearest = find_second_nearest(position_particle,values, nearest)
        
        if nearest == second_nearest:
            pot_energy_force = values[nearest,3]
        else:
            pot_energy_force = -1*(values[nearest,2]-values[second_nearest,2])/(values[nearest,1]-values[second_nearest,1])
            
        return pot_energy_force

    def stochastic_force(k_d,temp):
        std_dev = np.sqrt(2*2**.5*k_d*temp)
        return np.random.normal(0,std_dev)

    def drag_force(damping_coeff, veloc):
        return -1*damping_coeff*veloc

    def net_accel(position, velocity, temperature, damp_coeff, time_step, mass,array_of_energy_values):
        pot_energy_force = potential_energy_force(position, array_of_energy_values)
        stoch_force = stochastic_force(damp_coeff,temperature)
        drag__force = drag_force(damp_coeff,velocity)
        return (pot_energy_force + stoch_force + drag__force)/mass    
    def velocity(accel, init_veloc, timestep):
        return init_veloc + timestep*accel

    def position(init_position, velocity, time_per_step, array):
        position_particle = init_position + velocity*time_per_step
        values = np.asarray(array)
        positions = np.array(values)[:,1]
        max_val = np.argmax(positions)
        min_val = np.argmin(positions)
        if position_particle > positions[max_val]:
            while position_particle > positions[max_val]:
                position_particle = positions[min_val]+ position_particle - positions[max_val]
            return position_particle
        elif position_particle < positions[min_val]:
            while position_particle < positions[min_val]:
                position_particle = positions[max_val] - np.abs(position_particle - positions[min_val])
            return position_particle

        else:
            return position_particle 

    with open('{}'.format(potential_energy_file)) as potential_energy_vals:
        values = []
        for line in potential_energy_vals: 
            vals = [float(i) for i in line.split()] #Source: http://stackoverflow.com/questions/19555472/change-a-string-of-integers-separated-by-spaces-to-a-list-of-int
            values.append(vals)
        values = np.asarray(values)
        
        output_file = open ('{}.txt'.format(output_file_location),'w')
        output_file.write('{} {} {} {}'.format(1,0,init_position,init_velocity))
        pos = init_position
        veloc = init_velocity
        t=0
        for i in range(1,total_steps+1): 
            accel = net_accel(pos, veloc, temperature, damp_coeff, time_step, mass,values)
            veloc = velocity(accel,veloc,time_step)
            pos = position(veloc,pos,time_step,values)
            t += time_step
            output_file.write('{:.0f} {:.5f} {:.5f} {:.5f}\n'.format(i, t, pos, veloc))
        
        return(pos, veloc)


def position(init_position, velocity, time_per_step, potential_energy_file):
    import numpy as np
    position_particle = init_position + velocity*time_per_step
    with open('{}'.format(potential_energy_file)) as potential_energy_vals:
        values = []
        for line in potential_energy_vals: 
            vals = [float(i) for i in line.split()] #Source: http://stackoverflow.com/questions/19555472/change-a-string-of-integers-separated-by-spaces-to-a-list-of-int
            values.append(vals)
        values = np.asarray(values)
        positions = np.array(values)[:,1]
        max_val = np.argmax(positions)
        min_val = np.argmin(positions)

        if position_particle > positions[max_val]:
            while position_particle > positions[max_val]:
                position_particle = positions[min_val]+ position_particle - positions[max_val]
            return position_particle
        elif position_particle < positions[min_val]:
            while position_particle < positions[min_val]:
                position_particle = positions[max_val] - np.abs(position_particle - positions[min_val])
            return position_particle

        else:
            return position_particle 
