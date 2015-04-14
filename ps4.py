# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    delays = [300, 150, 75, 0]
 
    # TODO
    for d in xrange(len(delays)) : 
        v_populations = [0]*numTrials
        for i in range(numTrials) :
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)]*numViruses
            patient = TreatedPatient(viruses, maxPop)

            for t in xrange(delays[d]) :
                patient.update()

            patient.addPrescription('guttagonol')
            for j in xrange(delays[d], delays[d]+149) :
                patient.update()
            v_populations[i] = patient.update()

        pylab.figure(d+1)
        pylab.hist(v_populations, bins = 50)
        pylab.xlabel("Final total virus population")
        pylab.ylabel("Number of trials")
        pylab.title("Histogram for " + str(delays[d]) + " time steps")


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO

#Execution
simulationDelayedTreatment(1000)
pylab.show()


