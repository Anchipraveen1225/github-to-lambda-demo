import pandas as pd

def lambda_handler(event,context):

    d={'call':[1,2,3],'call2':[4,5,6],'cal3':[5,6,7]}
    df=pd.DataFrame(data=d)
    print(df)
    print("Done x1")