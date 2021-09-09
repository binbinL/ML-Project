import matplotlib.pyplot as plt
import sklearn.datasets as sk
import random
from sklearn.metrics import accuracy_score, normalized_mutual_info_score ,adjusted_rand_score
def KMeans(k):
    dis = []
    for i in range(k):
        d = (x1[:, 0]-X[i][0])**2+(x1[:,1]-X[i][1])**2
        dis.append(d)
    for i in range(800):
        min_num = 100000
        for j in range(k):
            if dis[j][i]<min_num:
                min_num = dis[j][i]
                y1[i] = j

def getcenter(k):
    sum_x = [[0]*k]
    sum_y = [[0]*k]
    cnt = [[0]*k]
    X.clear()
    for i in range(800):
        for j in range(k):
            if y1[i]==j:
                sum_x[0][j]+=x1[i,0]
                sum_y[0][j]+=x1[i,1]
                cnt[0][j]+=1
                break
    for i in range(k):
        X.append([(sum_x[0][i]/cnt[0][i]),(sum_y[0][i]/cnt[0][i])])
    print(X)

X1, Y1 = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
X2, Y2 = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
X = [[X1,Y1],[X2,Y2]]
fig = plt.figure('example', figsize=(10, 6))
x1, y1 = sk.make_moons(n_samples=800, noise=0.1)
y_true = y1.copy()
plt.subplot(121)
plt.title('data by make_moons()')
plt.scatter(x1[:, 0], x1[:, 1], marker='.', c=y1)
plt.scatter(X[0][0], X[0][1], marker='*', c='b', s=50)
plt.scatter(X[1][0], X[1][1], marker='*', c='b', s=50)

KMeans(2)
for i in range(20):
    getcenter(2)
    KMeans(2)

plt.subplot(122)
plt.title('data by make_moons()')
plt.scatter(x1[:, 0], x1[:, 1],marker='.', c=y1)
plt.scatter(X[0][0], X[0][1], marker='*', c='b', s=50)
plt.scatter(X[1][0], X[1][1], marker='*', c='b', s=50)

ACC=accuracy_score(y_true, y1)
NMI = normalized_mutual_info_score(y_true,y1)
ARI = adjusted_rand_score(y_true,y1)
plt.suptitle("ACC:{:.3f}  NMI:{:.3f}  ARI:{:.3f}".format(ACC,NMI,ARI))
print(ACC)
print(NMI)
print(ARI)

plt.show()

