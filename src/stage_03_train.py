from ast import If
import os
from src.utils.all_utils import read_yaml,createDirectory,save_local_df
import argparse
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib

def train(config_path,params_path):
  print(config_path)
  config=read_yaml(config_path)
  params=read_yaml(params_path)
  artifacts_directory=config['artifacts']['artifacts_dir']
  split_data_dir=config['artifacts']['split_data_dir']
  split_data_train_path=os.path.join(artifacts_directory,split_data_dir,config['artifacts']['train'])
  train_data=pd.read_csv(split_data_train_path)
  train_y=train_data['quality']
  train_x=train_data.drop('quality',axis=1)
  alpha=params['model_parameters']['ElasticNet']['alpha']
  l1_ratio=params['model_parameters']['ElasticNet']['l1_ratio']
  random_state=params['base']['random_state']
  lr=ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=random_state)
  lr.fit(train_x,train_y)
  model_dir=os.path.join(artifacts_directory,config['artifacts']['model_dir'])
  createDirectory([model_dir])
  model_path=os.path.join(model_dir,config['artifacts']['model_file'])
  joblib.dump(lr,model_path)
  
  
  
  
  
  
  


if __name__=='__main__':
  args=argparse.ArgumentParser()
  args.add_argument("--config","-c",default="config/config.yaml")
  args.add_argument("--params","-p",default="params.yaml")
  parsed_args=args.parse_args()
  train(config_path=parsed_args.config,params_path=parsed_args.params)
  