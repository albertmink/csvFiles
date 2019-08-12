import numpy as np
from numpy import linalg as LA



def getDataMink( caseFile, line=1 ):
    return np.genfromtxt( caseFile, delimiter=',', comments='#', dtype=float, usecols=(0,line) );

def getDataMcHardy( caseFile, line=1 ):
    return getDataMink(caseFile, line);

def getDataLena( caseFile, line=1 ):
    return getDataMink(caseFile, line);

def getTotalEnergy( caseLena, line, indexAwayFromBoundary=0 ):
    dataLena = getDataLena( caseLena, line )
    index_to_keep = np.arange(1+indexAwayFromBoundary,97,1); # to slice array to voxel inside geometry
    if len(index_to_keep) < 1:
      return 1
    else:
      return 1./len(index_to_keep) * LA.norm(dataLena[:,1][index_to_keep], ord=1);

'compute l2 norm from voxel inside the geometry'
def getNorm( caseNb1, dataLena, line, indexAwayFromBoundary=0 ):
    dM = getDataMink(caseNb1, line);
    index_to_keep = np.arange(1+indexAwayFromBoundary,97,1); # to slice array to voxel inside geometry
    if len(index_to_keep) < 1:
      return 1
    else:
      return 1./len(index_to_keep) *LA.norm( np.subtract(dM[:,1][index_to_keep],dataLena[:,1][index_to_keep]) );

def getNorm4( caseNb1, dataLena, line, indexAwayFromBoundary=0 ):
    dM = getDataMink(caseNb1, line);
    if caseNb1.startswith("infiniteBeam/"):
      dM [:,1] = np.multiply(dM[:,1],5)
      #print( "scale by " + str(5) )
    elif caseNb1.startswith("finiteBeamDiffuse/"):
      dM [:,1] = np.multiply(dM[:,1],3)
      #print( "scale by " + str(3) )
    else:
      dM [:,1] = np.multiply(dM[:,1],4)
      #print( "scale by " + str(4) )
    index_to_keep = np.arange(1+indexAwayFromBoundary,97,1); # to slice array to voxel inside geometry
    if len(index_to_keep) < 1:
        return 1
    else:
        return 1./len(index_to_keep) *LA.norm( np.subtract(dM[:,1][index_to_keep],dataLena[:,1][index_to_keep]) );
