"""
faire le pseudo code demandé par dans la consigne
"""

from Classtab import Tab

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
"""
print(tab.command," command \n")
print(tab.provider," provider \n")
print(tab.content," content \n")
print(tab.cout, "cout \n")
"""
tab.rand_fill(3)
tab.balas_hammer()
print("stepping stone")
tab.stepping_stone()
tab.show_tab()
print("\n")
"""
print(tab.command, " command \n")
print(tab.provider, " provider \n")
print(tab.cout, "cout \n")
print(tab.content, " content \n")

"""