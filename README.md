# Insurance cross-sell prediction
The goal of this project is to predict which customers are most likely to purchase additional insurance products using 
a machine learning model. Additionally, this project aims in MLops using mlflow, DVC etc




git rm -r --cached 'data'
git commit -m "stop tracking data"

dvc remote add -d <remote_name> <remote_storage_path>
dvc remote add -d myremote s3://lm-insurance-data/mydata/

git commit .dvc/config -m 'config dvc store'

Setup IAM user in AWS account give s3 full access and then configure 
aws user in local CLI

dvc push

dvc pull

## To launch MLflow UI

mlflow ui

![img.png](img.png)


## run the FastAPI app
uvicorn filename:instance_name --reload

uvicorn app:app --reload

Sample input:
{
  "Gender": "Female",
  "Age": 46,
  "HasDrivingLicense": 1,
  "RegionID": 21.0,
  "Switch": 0,
  "PastAccident": "Yes",
  "AnnualPremium": 2305.40
}

Sample Output:
{
  "predicted_class": 1
}

## To build docker image

docker build -t <image_name> <path_to_dockerfile>

docker build -t insurance_api .

## To run docker container
docker run -d -p 80:80 <image_name>

docker run -d -p 80:80 insurance_api

## To stop the container
docker stop <container_id_or_name>

## List images by name and tag.
docker image ls

## Tag the image
docker tag <image_name> <dockerhub_username>/<docker-repo-name>

docker tag insurance_api lokeshmamidi99/insurance_api

## Push the Docker image 
docker push <dockerhub_username>/<docker-repo-name>:latest

docker push lokeshmamidi99/insurance_api:latest