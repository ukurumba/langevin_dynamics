=====
Usage
=====

To use Langevin Dynamics in a project::

    import langevin_dynamics

    langevin_simulation(init_position, init_velocity, temperature, damp_coeff, time_step, total_steps, mass, potential_energy_file, output_file_location="langevin_dynamics_output"):


Help output::
    '''This function models the motion of a particle undergoing the forces considered in Langevin Dynamics in 1-Dimension. These include a potential energy distribution, a dampening force, and a random/stochastic force due to molecular collisions. Note that this solution implicitly assumes cyclic boundary conditions (i.e. smallest position = largest position), so the only values which the particle can exist at are ones for which a potential energy is defined. 

    ---------------------------------------------
    Inputs: 

    init_position = initial position of particle
    init_velocity = initial velocity of particle
    temperature = temperature of the system in Kelvin
    damp_coeff = the dampening coefficient for use in calculating solvent drag and stochastic force
    time_step = the amount of time you'd like per iteration of the numerical integration in seconds
    total_steps = total number of integration steps desired (must be an integer)
    potential_energy_file = a text file containing potential energy values. Each potential energy value should be
    of the format: index position energy force   <- where each value is separated by a space and each index is on a new line
    mass = the mass of the particle
    output_file_location = (optional) output file name

    ----------------------------------------------
    Example:

    langevin_dynamics.langevin_simulation(1.23,3.34,200, 1, .001, 1000, 2, 'potential_energies_of_system.txt')

    ----------------------------------------------
    Sample Input File:

    1 1.002 3.0 -2.5 
    2 1.003 3.0 -2.4 
    3 1.004 2.4 -1.9 

    ----------------------------------------------
    Output:

    tuple: (final_position,final_velocity)
    file created @ specified location with values in the following format:
    index time position velocity 

    ----------------------------------------------
    Sample Output File:
    1 0     2.42 1.333 
    2 0.10  2.32 -3.21 

    '''

