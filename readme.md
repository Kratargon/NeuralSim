# Neural Simulator

## General Simulation Process:
1. Create a 'brain' object. This encapsulates an emulation of a clump of neurons to allow a variety of neural simulations to proceed through sequential firing.
2. Give the brain a specified number of neurons.
3. Create connections between sets of these neurons. These define which neurons effect each other. These neurons will fire if their activity crosses a threshold.
4. Give the brain a specified input data file. This consists of neuron identifiers and the times at which they receive stimuli or fire.
5. Run the brain simulation for the desired length of time.
6. Visualize the static structure of the brain, and/or the active observation of its firing patterns. The static structure is an image of the neurons and their connections, while the active observation are animations consisting of the static structure with neurons lighting up as they fire

## Objects:
- Brain
- Neuron
- Axon
- Event

### Brain object:
- addNeuron()
	- Adds a new blank neuron to the brain
- visualizeStatic()
	- Creates a visualization of the brain's structure
- visualizeActive()
	- Creates a visualization of the brain's structure over time
- simulate(time in ms)
	- Allows the brain to fire and process
- size()
	- Returns the count of neurons in the brain
- importInputData(file containing firing data)
	- Adds the data in the file to the list of events that neurons will undergo

### Neuron object:
- surgery(input neurons, output neurons)
	- Adds the given neurons to the lists of inputs and outputs
- timeShock(value of shock, time of shock)
	- Tells the neuron to be shocked at a specific time
- applySHOCK(value of shock)
	- Shocks the neuron with the given shock value

### Axon object:
- TODO

### Event object:
- TODO


This structure was used in an attempt to increase the modularity of code and allow for certain regions to be replaced if a better approximation is found for any component; i.e. if we decide to expand on the detail of simulating axons, we need only keep external-facing functions' inputs and outputs the same.
