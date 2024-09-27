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