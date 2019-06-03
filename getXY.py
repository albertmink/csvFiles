import numpy as np
from numpy import linalg as LA



def getDataMink( caseFile, line ):
    return np.genfromtxt( caseFile, delimiter=',', comments='#', dtype=float, usecols=(0,line) );

def getDataMcHardy( caseFile, line ):
    return getDataMink(caseFile, line);

def getDataLena( caseFile, line ):
    return np.genfromtxt( caseFile, delimiter=',', comments='#', dtype=float, usecols=(0,7+line) );

def getTotalEnergy( caseLena, line, indexAwayFromBoundary=0 ):
    dataLena = getDataLena( caseLena, line )
    index_to_keep = np.arange(1+indexAwayFromBoundary,99,1); # to slice array to voxel inside geometry
    if len(index_to_keep) < 1:
      return 1
    else:
      return 1./len(index_to_keep) * np.sum(dataLena[:,1][index_to_keep]) ;

'compute l2 norm from voxel inside the geometry'
def getNorm( caseNb1, dataLena, line, indexAwayFromBoundary=0 ):
    dM = getDataMink(caseNb1, line);
    index_to_keep = np.arange(1+indexAwayFromBoundary,99,1); # to slice array to voxel inside geometry
    if len(index_to_keep) < 1:
      return 1
    else:
      return 1./len(index_to_keep) *LA.norm( np.subtract(dM[:,1][index_to_keep],dataLena[:,1][index_to_keep]) );

def getNorm4( caseNb1, dataLena, line, indexAwayFromBoundary=0 ):
    dM = getDataMink(caseNb1, line);
    dM [:,1] = np.multiply(dM[:,1],4)
    index_to_keep = np.arange(1+indexAwayFromBoundary,99,1); # to slice array to voxel inside geometry
    if len(index_to_keep) < 1:
        return 1
    else:
        return 1./len(index_to_keep) *LA.norm( np.subtract(dM[:,1][index_to_keep],dataLena[:,1][index_to_keep]) );
