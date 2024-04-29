"""
faire le pseudo code demandé par dans la consigne
"""

from Classtab import Tab
import os
import time
tab = Tab()
"""
tab.cout = [[6, 3, 8],
            [5, 7, 4],
            [8, 2, 3]]
tab.command = [500, 240, 610, 350]#manque 350 par rapport au provider
tab.provider = [450,
                550,
                700]#manque 700 par rapport au command
"""
"""
tab.cout = [[15, 9, 8],
            [2, 5, 2],
            [3, 1, 6]]
tab.command = [900, 140, 1000]
tab.provider = [630,
                650, 
                660]
"""
"""
tab.cout = [[15, 8, 3],
            [14, 8, 3],
            [13, 4, 3]]
tab.command = [600, 700, 400]
tab.provider = [400,
                700,
                600]
"""
"""
tab.cout = [[15, 8, 3], 
            [8, 6, 2], 
            [3, 4, 1]]
tab.command = [700, 600, 400]
tab.provider = [800, 
                700, 
                300]
"""


def store_time(n, time1, time2, time3, t):
    if not os.path.exists("time"):
        os.makedirs("time")

    with open("time/size_"+str(n)+"_t_"+str(t)+".txt", "w") as f:
        f.write(str(n) + "\n" + str(time1) + "\n" + str(time2) + "\n" + str(time3))


def optimise_test():
    start_time = time.time()
    n = 4
    t = 1
    while True:
        time1, time2, time3 = Tab().calculate_time(n)
        print("Complexity: ", n)
        print("Generating Nord_ouest:",round(time3,3), "seconds")
        print("Generating Balas:",round(time1,3), "seconds")
        print("Stepping Stone:",round(time2,3), "seconds")
        store_time(n, time1, time2, time3, t)
        n *= 2
        if n > 10000:
            store_time(999999999, time.time() - start_time, time.time() - start_time, time.time() - start_time, t)
            n = 2
            t += 1

#RIP IN PEPERONI
optimise_test()