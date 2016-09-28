=====
Usage
=====

To use Langevin Dynamics in a project::

    import langevin_dynamics

    langevin_simulation(init_position, init_velocity, temperature, damp_coeff, time_step, total_steps, potential_energy_file, mass, output_file_location="langevin_dynamics_output"):
    	'''init_position = initial position of particle
    	init_velocity = initial velocity of particle
    	temperature = temperature of the system in Kelvin
    	damp_coeff = the dampening coefficient for use in calculating solvent drag and stochastic force
    	time_step = the amount of time you'd like per iteration of the numerical integration in seconds
    	total_steps = total number of integration steps desired
    	potential_energy_file = a text file containing potential energy values. Each potential energy value should be \n
    	of the format index position energy force'''

    #example: 
    langevin_simulation(1.23,3.34,200, 1, .001, 1000, 'potential_energies_of_system.txt')

