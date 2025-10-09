import pandas as pd
from sklearn.model_selection import train_test_split

def split(data: pd.DataFrame, store_train_path:str, store_test_path:str) -> tuple[pd.DataFrame, pd.DataFrame]:
    
    attr = data.drop("Outcome", axis=1)
    label= data["Outcome"]

    attr_t, attr_s, label_t, label_s = train_test_split(
                                        attr,label,stratify=label)
    
    train = pd.concat([attr_t, label_t],axis=1)
    test  = pd.concat([attr_s, label_s],axis=1)

    train.to_csv(store_train_path)
    test.to_csv(store_test_path)

    return train, test