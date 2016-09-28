=====
Usage
=====

To use Langevin Dynamics in a project::

    import langevin_dynamics

    langevin_simulation(init_position, init_velocity, temperature, damp_coeff, time_step, total_steps, potential_energy_file, mass, output_file_location="langevin_dynamics_output"):
    	init_position = initial position of particle
    	init_velocity = initial velocity of particle
    	temperature = temperature of the system in Kelvin
    	damp_coeff = the dampening coefficient for use in calculating solvent drag and stochastic force
    	time_step = the amount of time you'd like per iteration of the numerical integration in seconds
    	total_steps = total number of integration steps desired
    	potential_energy_file = a text file containing potential energy values. Each potential energy value should be 
    	of the format: index position energy force   <- where each value corresponding to an index is separated by a space
    	and each index is on a new line 
        mass = the mass of the particle
        output_file_location = (optional) output file name

    #example: 
    langevin_dynamics.langevin_simulation(1.23,3.34,200, 1, .001, 1000, 'potential_energies_of_system.txt',2)

    #potential_energies_of_system.txt example: 
    #    1 1.002 3.0 -2.5
    #    2 1.003 3.0 -2.4
    #    3 1.004 2.4 -1.9

