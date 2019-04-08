import numpy as np
from numpy import linalg as LA



def getDataMink( caseFile ):
    return np.genfromtxt( caseFile, delimiter=',', comments='#', dtype=float, usecols=(0,1) );

def getDataMcHardy( caseFile ):
    return getDataMink(caseFile);

def getDataLena( caseFile ):
    return np.genfromtxt( caseFile, delimiter=',', comments='#', dtype=float, usecols=(0,8) );

'compute l2 norm from voxel inside the geometry'
def getNorm( caseNb1, caseLena ):
    dM = getDataMink(caseNb1);
    dL = getDataLena(caseLena);
    index_to_keep = np.arange(1,100,1); # to slice array to voxel inside geometry
    return LA.norm( np.subtract(dM[:,1][index_to_keep],dL[:,1][index_to_keep]) );

