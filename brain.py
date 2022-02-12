#Brain, V.0.0.5
#Featuring:
#   -Brain IDs
#   -List of neurons
#   -File of inputs
#   -List of paired events and firing times
#
#   -Ability to add neurons to a brain
#   -Ability to simulate a period of time and record simulation firing data
#
#   -Directly interfaces: Neuron, Event

from neuron import *
from event import *

class Brain:
    def __init__(self, val, inputFile = None):
        # This is intended for handling multiple brains computing in the same larger project
        self.id = val
        # This is a list containing all the neurons that belong to this brain
        self.neurons = []
        # This file is a CSV file in format (time, subject, action)
        self.inputFile = inputFile
        # This is an active list of all events that are currently planned to take place, in the correct temporal order, as event objects
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
            if len(self.eventList) == 0:
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
        if len(self.eventList) == 0:
            return
        # Grab the event from the list and remove it from the list
        nextEvent = self.eventList.pop(0)
        # Update time
        self.currentTime = nextEvent.getTime()
        for i in self.neurons:
            i.setTime(self.currentTime)
        # Event objects have the ability to act on their own, so call on them to do so
        if nextEvent.act():
            # Record the action if it was a fire (nextEvent returns true if it's a fire)
            self.fireRecord.append([self.currentTime, nextEvent.getNeuronID()])
        # Adds all events to the list, if they aren't already there
        # Neurons that could be impacted by the shock is every descendant of the action
        for i in self.neurons[nextEvent.getNeuronID()].getNeuralOutputs():
            for (j, k) in i.getShockTimes():
                event = Event(j, i, k)
                if event not in self.eventList:
                    self.eventList.append(Event(j, i, k))
        # Re-sort list so that it remains properly sorted by time
        self.sortData()

    def importInputData(self, data):
        self.inputFile = data
        for i in data:
            self.eventList.append(Event(i[0], self.neurons[i[1]], i[2]))
        # We do not assume the data is sorted
        self.sortData()

    def sortData(self):
        # Sort by time, by running quicksort
        self.eventList = self.qsort(self.eventList)
        
    def qsort(self, inlist):
        if inlist == []: 
            return []
        else:
            pivot = inlist[0]
            lesser = self.qsort([x for x in inlist[1:] if x.getTime() < pivot.getTime()])
            greater = self.qsort([x for x in inlist[1:] if x.getTime() >= pivot.getTime()])
            return lesser + [pivot] + greater