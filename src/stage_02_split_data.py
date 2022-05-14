import os
from src.utils.all_utils import read_yaml,createDirectory,save_local_df
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

def split_and_save(config_path,params_path):
  print(config_path)
  config=read_yaml(config_path)
  params=read_yaml(params_path)
  artifacts_directory=config['artifacts']['artifacts_dir']
  artifacts_local_dir=config['artifacts']['raw_local_dir']
  artifacts_local_file=config['artifacts']['raw_local_file']


  # save dataset in local directory
  raw_local_dir_path=os.path.join(artifacts_directory,artifacts_local_dir)
  raw_local_dir_file_path=os.path.join(raw_local_dir_path,artifacts_local_file)
  df=pd.read_csv(raw_local_dir_file_path)
  train,test=train_test_split(df,test_size=params['base']['test_size'],random_state=params['base']['random_state'])
  split_data_dir=config['artifacts']['split_data_dir']
  split_data_train_path=os.path.join(artifacts_directory,split_data_dir,config['artifacts']['train'])
  split_data_test_path=os.path.join(artifacts_directory,split_data_dir,config['artifacts']['test'])
  createDirectory([os.path.join(artifacts_directory,split_data_dir)])
  save_local_df(train,split_data_train_path)
  save_local_df(test,split_data_test_path)
  
  
  
  


if __name__=='__main__':
  args=argparse.ArgumentParser()
  args.add_argument("--config","-c",default="config/config.yaml")
  args.add_argument("--params","-p",default="params.yaml")
  parsed_args=args.parse_args()
  split_and_save(config_path=parsed_args.config,params_path=parsed_args.params)
  