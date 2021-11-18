import pandas as pd

def lambda_handler(event,context):

    d={'call':[1,2,3],'call2':[4,5,6]}
    df=pd.DataFrame(data=d)
    print(df)
    print("Done x1")