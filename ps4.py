# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *
import sys

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
    maxBirthProb = 0.5
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    delays = [150]
 
    # TODO
    for d in xrange(len(delays)) : 
        #Showing progress
        print "For trials delayed " + str(delays[d]) + " time steps" 
        v_populations = [0]*numTrials
        for i in range(numTrials) :
            #Showing progress
            print "\rFinished {0}% of trials".format(round(float(i)/numTrials*100, 3)),
            sys.stdout.flush()
            
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
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    delays = [300, 150, 75, 0]
 
    # TODO
    for d in xrange(len(delays)) : 
        #Showing progress
        print "\nFor trials delayed " + str(delays[d]) + " time steps" 
        v_populations = [0]*numTrials
        for i in range(numTrials) :
            #Showing progress
            print "\rFinished {0}% of trials".format(round(float(i+1)/numTrials*100, 3)),
            sys.stdout.flush()
            
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)]*numViruses
            patient = TreatedPatient(viruses, maxPop)

            for t in xrange(150) :
                patient.update()

            patient.addPrescription('guttagonol')
            
            
            for j in xrange(delays[d]) :
                patient.update()
                
            patient.addPrescription('grimpex')
                
            for t in xrange(149) :
                patient.update()
            
            v_populations[i] = patient.update()

        pylab.figure(d+1)
        pylab.hist(v_populations, bins = 50)
        pylab.xlabel("Final total virus population")
        pylab.ylabel("Number of trials")
        pylab.title("Histogram for " + str(delays[d]) + " time steps")

#Execution for problem 1
#pylab.close("all")
#simulationDelayedTreatment(1000)
#pylab.show()

#Execution for problem 2
pylab.close("all")
simulationTwoDrugsDelayedTreatment(500)
pylab.show()

