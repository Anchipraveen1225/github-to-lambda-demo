import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
import pandas as pd
def lambda_handler(event, context):
  data={'a':[1,2,3],'b':[4,5,6],'c':[78,4,5]}
  df=pd.DataFrame(data)
  print(df)