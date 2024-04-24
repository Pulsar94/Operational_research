"""
faire le pseudo code demadné par dans la consigne
"""

from Classtab import Tab

tab = Tab()
tab.cout= [[11, 12, 10, 10], [17, 16, 15, 18], [19, 21, 20, 22]]
tab.content = [[35, 0, 0, 25], [0, 0, 30, 0], [15, 75, 0, 0]]
tab.command = [50, 75, 30, 25]
tab.provider = [60, 30, 90]

tab.stepping_stone()

