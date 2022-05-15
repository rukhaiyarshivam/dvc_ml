import os
from src.utils.all_utils import read_yaml,createDirectory
import argparse
import pandas as pd

def get_data(config_path):
  print(config_path)
  config=read_yaml(config_path)
  remote_data_path=config['data_source']
  if remote_data_path.endswith("csv"):
    df=pd.read_csv(remote_data_path,sep=";")
  elif remote_data_path.endswith("data"):
    df=pd.read_fwf(remote_data_path)
  artifacts_directory=config['artifacts']['artifacts_dir']
  artifacts_local_dir=config['artifacts']['raw_local_dir']
  artifacts_local_file=config['artifacts']['raw_local_file']
  # save dataset in local directory
  raw_local_dir_path=os.path.join(artifacts_directory,artifacts_local_dir)
  raw_local_dir_file_path=os.path.join(raw_local_dir_path,artifacts_local_file)
  createDirectory([artifacts_directory,raw_local_dir_path])
  df.to_csv(raw_local_dir_file_path,sep=",",index=False)
  
  


if __name__=='__main__':
  args=argparse.ArgumentParser()
  args.add_argument("--config","-c",default="config/config.yaml")
  parsed_args=args.parse_args()
  get_data(parsed_args.config)
  