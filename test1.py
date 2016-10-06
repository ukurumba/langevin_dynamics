from langevin_dynamics import langevin_dynamics
tup = langevin_dynamics.langevin_simulation(1.0, .001, 10.0, 1.0, .1, 50, 2.0, 'pot_example_expanded.txt')
print(tup)