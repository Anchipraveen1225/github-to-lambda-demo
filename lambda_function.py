import pandas as pd
def lambda_handler(event, context):
    data={'a1':[1,2,3],'b1':[4,5,6]}
    df=pd.DataFrame(data)
    print("lambda successful")
    print(data)

