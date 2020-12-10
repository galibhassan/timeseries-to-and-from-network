import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def isVisible(ta, ya, tb, yb, tc, yc):
    heightLimit = yb + (ya-yb)*(tb-tc)/(tb-ta)
    if(yc < heightLimit):
        return True
    else:
        return False

def getVisibilityGraph(ts, plt):
    for i in range(len(ts)):
        for j in range(i+1, len(ts)):
            tsInBetween = ts[i+1:j]
            if len(tsInBetween) == 0:
                # i, j consecutive indices; so visible
                # print(f"{ts[i]} is visible from {ts[j]}")
                plt.plot([i, j], [ts[i],ts[j]], color="green")
                pass
            elif len(tsInBetween) > 0:
                stillVisible = True
                for k in range(len(tsInBetween)):
                    visFlag = isVisible(
                        i, ts[i], j, ts[j], (i+1+k), tsInBetween[k])
                    if visFlag == False:
                        # print(f"{i},{ts[i]} not visible from {j},{ts[j]} because of obstacle {i+1+k},{tsInBetween[k]}")
                        plt.plot([i, j], [ts[i],ts[j]], color="lightgray")
                        stillVisible = False
                        break

                if stillVisible == True:
                    # print(f"{ts[i]} is visible from {ts[j]}")
                    plt.plot([i, j], [ts[i],ts[j]], color="green")

# test
# t = [0, 1, 2, 3, 4, 5]
# ts = [0, 1, 20, 3, 4, 100]
t = np.arange(0, 10, 0.2)
ts = np.sin(t)
plt.bar(t, ts, width=.05, zorder=99)
plt.scatter(t, ts, zorder=100)
getVisibilityGraph(ts, plt)

plt.show()
