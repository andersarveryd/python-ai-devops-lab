from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def run_ai_demo():
    # 1. Ladda dataset (blommor)
    iris = load_iris()
    X = iris.data   # mätningar på blomblad/stjälkar
    y = iris.target # arterna (0,1,2)

    # 2. Dela upp i träning (80%) och test (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Skapa en enkel modell (K-Nearest Neighbors)
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    # 4. Testa modellen
    accuracy = model.score(X_test, y_test)

    print(f"Modellens träffsäkerhet: {accuracy:.2f}")

    # 5. Gör en egen förutsägelse
    sample = [[5.1, 3.5, 1.4, 0.2]]  # liknar Iris-setosa
    prediction = model.predict(sample)
    print("Förutsägelse för sample:", iris.target_names[prediction][0])

if __name__ == "__main__":
    run_ai_demo()
