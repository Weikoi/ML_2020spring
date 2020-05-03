from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn import tree
import pickle as pk

X = pk.load(file=open('../data/temp/train.pkl', 'rb'))
y = pk.load(file=open('../data/temp/label.pkl', 'rb'))

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)


def train_model(model_name):
    if model_name == "LinearRegression":
        model = LinearRegression()
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        print(score)

    if model_name == "Lasso":
        model = Lasso(alpha=1)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        print(score)

    if model_name == "Ridge":
        model = Ridge(alpha=1)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        print(score)

    if model_name == "tree":
        model = tree.DecisionTreeRegressor()
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        print(score)


if __name__ == '__main__':
    model_chosen = "tree"
    train_model(model_chosen)
