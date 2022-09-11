from sklearn import svm

x = [[-3, -1], [0, 2], [-2.5, 2]]


y = [0,2,1]

clf = svm.SVC(kernel='linear').fit(x, y)


