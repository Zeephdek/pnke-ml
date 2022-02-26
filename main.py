from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
 
# for euclid dist, it's 
# sklearn.metrics.pairwise.euclidean_distances
 
# init the empty list with no people
 
class person():
    """
    init it with a .fv as the fv
 
    """
    def _init_(self, fv):
        self.fv = fv
 
def afdsfadsfafs():
    for n, f in enumerate(frames):
        fprev = frames[n-1]
 
        # run torch reid?
        # and then get featureextractor
 
        framePeople = [] # obtained from feature extract
 
        distResults = [] # empty list for comparing
        for framePerson in framePeople:
            for person in people:
                distResults.append(eDist(framePerson.fv, people.fv))
 
 
## test code
 
def distanceCode(fvs0, fvs1):
    print(fvs0)
    print(fvs1)
 
    distances = euclidean_distances(fvs1, fvs0)
 
    print(distances)
 
    # these can or should be moved to the obj's
    presentIndexes = []
    closestDists = []
 
    for a in distances:
        minvalue = a.min()
        newIndex = list(a).index(minvalue) # ineffiencies be like:
 
        if newIndex in presentIndexes:
            annoyance = presentIndexes.index(newIndex)
            # comparing and stuff
            if distances[annoyance][newIndex] < minvalue:
                closestDists.append(-1)
                presentIndexes.append(-1)
 
            else:
                closestDists.append(minvalue)
                closestDists[annoyance] = -1
                presentIndexes[annoyance] = -1
                presentIndexes.append(newIndex)
                continue
        else:
            closestDists.append(minvalue)
            presentIndexes.append(newIndex)
 
    print(presentIndexes)
    print(closestDists)
 
    # threshold
    threshold = 0.75
    cD = np.array(closestDists) # do this shit earlier
    pI = np.array(presentIndexes)
 
    cD[cD > threshold] = -2
    pI[cD == -2] = -2
 
    """
    BUG BUG
    New oerson 2 is most similar to person -2, by -2.0
 
    (lmao)
    """
 
 
    print(pI)
    print(cD)
    print()
 
    printAndInterpret(pI, cD)
 
    # create shit
 
def printAndInterpret(pI, cD):
    print("For this new frame:")
    for n, p in enumerate(pI):
        if p == -1:
            print("New person {} is a new person.".format(n))
        else:
            print("New person {} is most similar to person {}, by {}".format(n, p, cD[n]))
 
    # and for the people that are left, probably just compare two arrays 
    # and find the difference.
 
 
# generating the people objs
def main():
    fvs0 = [
        [1,1,1,2],
        [2,3,4,12],
        [6,4,4,7]
    ]
    fvs1 = [
        [1,1,1.3,2],
        [1,1,1.1,2], # extra person with very close fv
        [2,3,4.5,12],
        [18,45,9,1], # diff person
    ]
 
    # distanceCode(fvs0, fvs1)
    distanceCode(
        np.random.rand(20,6),
        np.random.rand(20,6)
    )
 
 
 
# use the tensorflow obj detection api
 
"""
so we have two lists of people objs
one of the current frame
one of the previously present people
 
for each person in the current frame, 
you compare the euclid distnace to those already present
this outputs a list of values (dist), with indexes corresponding
to the indexes of the present people
 
so know we have several lists
or a list of lists / arrayof shape (2, n)
how to compare
 
for each sublist we find the minima -> use list.index() to get the 
index of said element
a new list? of the indexes of the closest people in previous frames
 
 
alternatively, 
run it iteratively (in a loop) -> each time appending the index of the person that it's the closest to
then for each succesive run,
if the index is in the indexList already, do somethng
otherwise return to a 
"""
 
if __name__ == "__main__":
    main()