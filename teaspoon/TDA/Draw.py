'''
Code for drawing various things.

'''



import matplotlib.pyplot as plt
import numpy as np


## \brief Draws simple persistence diagram plot
#
# @param D
#	a persistence diagram, given as a Kx2 numpy array
# @param boundary
# @param epsilon
#	The diagram is drawn on [0,boundary]x[0,boundary].  
#	If boundary not given, then it is determined to be the 
#	max death time from the input diagram plus epsilon.  
#
def drawDgm(D,boundary=None,epsilon = .5, color=None):
    # Separate out the infinite classes if they exist
    includesInfPts = np.inf in D
    if includesInfPts:
        Dinf = D[np.isinf(D[:,1]),:]
        D = D[np.isfinite(D[:,1]),:]

    # Get the max birth/death time if it's not already specified
    if not boundary:
        boundary = D.max()+epsilon

    # if fig is None:
    #     fig = plt.figure()
    # ax = fig.gca()
    # Plot the diagonal
    plt.plot([0,boundary],[0,boundary])

    # Plot the diagram points
    if color is None:
        plt.scatter(D[:,0],D[:,1])
    else:
        plt.scatter(D[:,0],D[:,1], c=color)

    if includesInfPts:
        plt.scatter(Dinf[:,0], .98*boundary, marker='s', color='red')

        plt.axis([-.01*boundary,boundary,-.01*boundary,boundary])

    plt.ylabel('Death')
    plt.xlabel('Birth')


## \brief Draws simple point cloud plot
#
# @param P
#	a point cloud, given as a KxD numpy array
#	Even if D>2, only the first two coordinates are plotted.
#
def drawPtCloud(P):
    plt.scatter(P[:,0],P[:,1])