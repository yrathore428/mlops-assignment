from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import logging
from datetime import datetime

mlflow.set_tracking_uri("http://127.0.0.1:5000")

app = FastAPI()
model_path = "./artifacts"
model = mlflow.pyfunc.load_model(model_path)

class InputData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: InputData):
    start = datetime.now()
    prediction = model.predict([data.features])
    duration = (datetime.now() - start).total_seconds()
    logging.info(f"{datetime.now()} | {data.features} | {prediction.tolist()} | {duration:.3f}s")
    return {"prediction": prediction.tolist(), "inference_time": duration}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

