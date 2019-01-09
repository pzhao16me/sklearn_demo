from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import datasets

# 加载iris数据集
iris = datasets.load_iris()

X = iris.data
y = iris.target

print('Sample num: ', len(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = GaussianNB()

# 训练模型
clf.fit(X_train, y_train)

# 预测结果
ans = clf.predict(X_test)

# 计算准确率
cnt = 0
for i in range(len(y_test)):
    if ans[i] - y_test[i] < 1e-1:
        cnt += 1
    # print(ans[i], ' ', y_test[i])

print("Accuracy: ", (cnt * 100.0 / len(y_test)), "%")