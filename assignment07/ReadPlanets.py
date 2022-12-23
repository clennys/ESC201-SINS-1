
import pandas as pd
import numpy as np


def readPlanets(filename, N=-1):
    # Loading text files with Pandas
    df = pd.read_csv(filename, sep=',', header=None,
                     names=['name', 'm', 'x', 'y', 'z', 'vx', 'vy', 'vz'])

    # Data is now in a Pandas dataframe
    # print(df)

    name = np.array(df.loc[:, 'name'])
    m = np.array(df.loc[:, 'm'])
    r = np.array(df.loc[:, 'x':'z'])
    v = np.array(df.loc[:, 'vx':'vz'])

    if N > 0:
        name = name[0:N-1]
        m = m[0:N-1]
        r = r[0:N-1]
        v = v[0:N-1]

    return (name, r, v, m)


# Loading text files with NumPy
def readPlanetsNp(filename):
    data = np.loadtxt(filename, delimiter=',', unpack=False,
        dtype={'names': ('planet', 'mass', 'x', 'y', 'z', 'vx', 'vy', 'vz'),
               'formats': ('S10', np.float, np.float, np.float, np.float,
                           np.float, np.float, np.float)})

    # print(data)
    name = np.array([d[0] for d in data])
    m = np.array([d[1] for d in data])
    r = np.array([[d[2], d[3], d[4]] for d in data])
    v = np.array([[d[5], d[6], d[7]] for d in data])
    return (name, r, v, m)


name, r, v, m = readPlanets("SolSystData.dat")

name1, r1, v1, m1 = readPlanetsNp("SolSystData.dat")

# def accel(...):
#    a = np.zeros(...)
#    for (i=0...N-1)
#      for (j=i+1...N-1)
#        calculate force between i and j
#        a[i] += ...
#        a[j] -= ...
    

# 1. Read Solar system data

# h = 4
# end time = 1000 * h
# 2. for time in 0 to end time:
#    3. First drift to give r1/2
#    4. Calculate forces and accels at position r1/2
#    5. Kick: v1 = v0 + ... using accels from step 4.
#    6. Second drift to give r1
#    7. Store r1 for graphics
# 8. Plot all planets
#    


