import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("iris_experiment")

with mlflow.start_run() as run:
    # Load data
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_metric("accuracy", model.score(X_test, y_test))

    mlflow.sklearn.log_model(model, registered_model_name="iris_model")

    print("\n=== MLflow Run Info ===")
    print("Run ID:", run.info.run_id)
    print("Artifact URI:", mlflow.get_artifact_uri())

print("Training finished — Model logged to MLflow.")
