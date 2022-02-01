#Brain, V.0.0.3
#Featuring:
#   -Brain IDs
#   -List of neurons
#   -File of inputs
#   -List of paired events and firing times
#
#   -Ability to add neurons to a brain
#   -Ability to simulate a period of time and record simulation firing data

from neuron import *
from event import *

class Brain:
    def __init__(self, val, inputFile = None):
        # This is intended for handling multiple brains computing in the same larger project
        self.id = val
        # This is a list containing all the neurons that belong to this brain
        self.neurons = []
        # TODO This file is in format
        self.inputFile = inputFile
        # This is an active list of all events that are currently planned to take place, in the correct temporal order
        self.eventList = []
        # This records every neuron that fired by time of action and id, in temporal order, as sublists of size 2
        self.fireRecord = []
        # This reflects how long the simulation has been run for in sim-time
        self.currentTime = 0

    def addNeuron(self):
        # Adds a Neuron object to the list of neurons of this brain
        self.neurons.append(Neuron(self, len(self.neurons)))

    def simulate(self, time):
        # Continues the simulation until the brain's local time exceeds the given bound
        while self.currentTime < time:
            # Fire the next neuron; this function updates the current time
            self.fireNext()
            # If the brain goes 'silent' and never fires again, ensure that we return even though the brain's time never advances
            if len(eventList) == 0:
                return self.fireRecord
        return self.fireRecord

    def visualizeStatic(self):
        # This code gives a static image representing the connectivity of the neurons
        for i in self.neurons:
            # Each neuron is called on to handle its own visualization
            i.visualizeStatic()

    def visualizeActive(self):
        #TODO This code gives a video representing the neurons of the brain firing over time
        return

    def size(self):
        # Returns the number of neurons the brain has
        return len(self.neurons)

    def fireNext(self):
        # Catch condition for if there's nothing left to fire
        if len(eventList) == 0:
            return
        # Grab the event from the list and remove it from the list
        nextEvent = eventList.pop(0)
        # Update time
        self.currentTime = nextEvent.getTime()
        # Event objects have the ability to act on their own, so call on them to do so
        if nextEvent.act():
            # Record the action if it was a fire (nextEvent returns true if it's a fire)
            self.fireRecord.append([self.currentTime, nextEvent.getNeuronID()])
        #This is where I should fix the eventList to reflect the new reality

    def importInputData(self, data):
        self.inputFile = data
        #I should update EventList here
        