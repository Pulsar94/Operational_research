"""
faire le pseudo code demadné par dans la consigne
"""

from Classtab import Tab

tab = Tab()
tab.cout= [[6, 3, 8], [5, 7, 4], [8, 2, 3]]
tab.command = [500, 240, 610, 350]#manque 350 par rapport au provider
tab.provider = [450, 550]#manque 700 par rapport au command
"""
print(tab.command," command \n")
print(tab.provider," provider \n")
print(tab.content," content \n")
print(tab.cout, "cout \n")
"""
tab.balas_hammer()
print("\n")
print(tab.command, " command \n")
print(tab.provider, " provider \n")
print(tab.cout, "cout \n")

