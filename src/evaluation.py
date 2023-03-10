from matching import match
from utils import list_full_paths

import pandas as pd

def evaluation(df_pred, df_gt, topk):
    num_correct = 0
    for i in range(0, len(df_gt)):
        file_name = df_gt[0].iloc[i]
        label = df_gt[1].iloc[i]
        list_pred = df_pred[[*range(0,topk)]].loc[file_name].values.tolist()

        if label in list_pred: 
            num_correct +=1

    return num_correct/len(df_gt)


def predict(dir_query, dir_gallery, topk, dir_save = None):
    list_dir_query = list_full_paths(dir_query)
    list_dir_gallery = list_full_paths(dir_gallery)
    result = match(list_dir_query, list_dir_gallery, topk=topk)
    df = pd.DataFrame(result).T
    if dir_save:
        df.to_csv(dir_save, sep='\t')
    return df

def main():
    dir_query = '../data/data_test/test_images'
    dir_gallery = '../data/data_train/'
    dir_gt = '../data/data_test/test.txt'
    topk = 5
    dir_save = f'../result/{topk}-acc.txt'
    df_pred = predict(dir_query, dir_gallery, topk, dir_save)
    df_gt = pd.read_csv(dir_gt, sep="\t", header=None)
    acc = evaluation(df_pred, df_gt, topk)
    print(f"Top-{topk} Accuracy: {acc}")
    

if __name__ == "__main__":
    main()