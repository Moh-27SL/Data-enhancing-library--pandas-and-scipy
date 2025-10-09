import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def clean(load_path:str, store_path:str) -> pd.DataFrame:
    data = pd.read_csv(load_path)

    #remove zero values from columns with impossible zero value
    #and replacing them with the mean value (not including zero value data)

    features = data.columns.drop(["Pregnancies", "Outcome", "Age"])

    for feature in features:
        mean = data[feature].replace(0,np.nan,inplace=False).mean(skipna=True)
        data[feature] = data[feature].replace(0, mean)

    #clipping outliers to the whiskers
    #reason is impossible values ex age = 768 lol

    features = data.columns.drop(["Outcome"])

    Q_U  = data[features].quantile(0.75)
    Q_L  = data[features].quantile(0.25)
    IQR  = Q_U - Q_L

    whisk_U = Q_U + 1.5 * IQR
    whisk_L = Q_L - 1.5 * IQR

    data[features] = data[features].clip(lower=whisk_L, upper=whisk_U, axis=1)

    #feature scalling and saving processed data :)

    scaler = StandardScaler()
    data[features] = scaler.fit_transform(data[features])
    
    data.to_csv(store_path, index= False)
    return data