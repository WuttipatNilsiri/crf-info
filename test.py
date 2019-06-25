from sklearn.model_selection import train_test_split

_list = list(range(1,11))
test , train = train_test_split(_list)
print(test)
print(train)
