# mlops-assignment

This is a basic mlops structure. Here is how to run it.

To run locally, first install the reuirements into your virtual environment.

The train.py file will log artifacts to mflow. On commandline type `mlflow` ui and then proceed to view it at `localhost:5000` Here you can view each instance of training.

1. First clone the repository
2. It already contains the artifacts. Simply proceed to building the docker image
3. Run the following comand in the same folder as the Dockerfile to build the docker container
   `docker build -t your-image-name .`
4. Once this is done, run the image and expose port 8000 byt he following command
   `docker run -it -p 8000:8000 your-image-name`
5. proceed to `localhost:8000/docs` to view endpoint documentation

## Optionals

1. Artifacts can be stored to artifact registry
2. Other metrics can also be tracked using MLflow
3. Logs can be sent to monitoring tools like Grafana
4. Docker Image can be stored to dockerhub
5. For scaling, I would use the kompose tool to auto generate kubernetes files, and then use helm to install it as an app within Kubernetes
