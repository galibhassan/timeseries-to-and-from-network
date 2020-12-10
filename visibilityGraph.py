import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def isVisible(ta, ya, tb, yb, tc, yc):
    heightLimit = yb + (ya-yb)*(tb-tc)/(tb-ta)
    if(yc < heightLimit):
        return True
    else:
        return False

def getVisibilityGraph(t, ts, plt):
    for i in range(len(ts)):
        for j in range(i+1, len(ts)):
            tsInBetween = ts[i+1:j]
            if len(tsInBetween) == 0:
                # i, j consecutive indices; so visible
                # print(f"{ts[i]} is visible from {ts[j]}")
                plt.plot([t[i], t[j]], [ts[i],ts[j]], color="green", zorder=200)
            elif len(tsInBetween) > 0:
                stillVisible = True
                for k in range(len(tsInBetween)):
                    visFlag = isVisible(t[i], ts[i], t[j], ts[j], t[i+1+k], tsInBetween[k])
                    if visFlag == False:
                        # print(f"{i},{ts[i]} not visible from {j},{ts[j]} because of obstacle {i+1+k},{tsInBetween[k]}")
                        plt.plot([t[i], t[j]], [ts[i],ts[j]], color="lightgray", zorder=199)
                        stillVisible = False
                        break

                if stillVisible == True:
                    # print(f"{ts[i]} is visible from {ts[j]}")
                    plt.plot([t[i], t[j]], [ts[i],ts[j]], color="green", zorder=200)

# test
# t = [0, 1, 2, 3, 4, 5]
# ts = [0, 1, 20, 3, 4, 100]
t = np.arange(0, 7*np.pi, np.pi/10)
ts = np.sin(t) +1
plt.bar(t, ts, width=.05, zorder=99)
plt.scatter(t, ts, zorder=300)
getVisibilityGraph(t, ts, plt)
plt.title("Visibility graph of $f(t)= sin(t)+1$")
plt.text(0, -0.2, 'Green lines are edges \nGray lines are failed edges', style='italic',
        bbox={'facecolor': 'white', 'alpha': 1, 'pad': 5}, zorder=1000)

plt.show()
