import clean, analysis, split
import sys

#use store path without extension ( it will be automaticly added )
def main(load_path:str, store_path:str):

    storepath = store_path+".csv"
    trainpath = store_path+"_train.csv"
    testpath  = store_path+"_test.csv"

    #setup data
    data = clean.clean(load_path, storepath)

    #analysis
    analysis.analysis(data)

    #store everything
    split.split(data,trainpath,testpath)

if(__name__ == "main"):
    if(len(sys.argv)==1):
        arg1 = input("load path of csv: ")
        arg2 = input("store path of csv [without extension]: ")

        main(arg1,arg2)
    else:
        main(sys.argv[1], sys.argv[2])