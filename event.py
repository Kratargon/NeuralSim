#Event, V.0.0.3
#Featuring:
#   -Time of firing
#   -Neuron that fires
#   -Value (as 'fire' or a shock value)
#
#   -Ability to perform stored action; returns true if neuron fires
#
#   -External access to ID of action's neuron
#   -External access to action's time

class Event:
    def __init__(self, time, subject, action):
        # The time at which the action took place
        self.time = time
        # The neuron that took the action
        self.neuron = subject
        # The actual action that was/will be taken
        self.value = action

    def getTime(self):
        return self.time

    def act(self):
        # Have the neuron perform the action
        if self.value == "fire":
            self.neuron.fire()
            # Return True if the neuron fires
            return True
        # Return True if the neuron fires as a result of the shock
        return self.neuron.applySHOCK(self.value)

    def getNeuronID(self):
        return self.neuron.id

    def __eq__(self, other): 
        if not isinstance(other, Event):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.time == other.time and self.neuron == other.neuron and self.value == other.value