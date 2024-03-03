import pandas as pd
import os 

def define_paths(dir):
    folds = os.listdir(dir)
    files = []
    classes = []
    for fold in folds:
        foldpath = os.path.join(dir, fold)
        # Check if it's a directory 
        if os.path.isdir(foldpath):
            filelist = os.listdir(foldpath)
            for file in filelist:
                fpath = os.path.join(foldpath, file)
                files.append(fpath)
                classes.append(fold)
    return files, classes

def define_df(files, classes):
    Fseries = pd.Series(files, name= 'filepaths')
    Lseries = pd.Series(classes, name='labels')
    return pd.concat([Fseries, Lseries], axis= 1)

def create_df(tr_dir, val_dir, ts_dir):
    # train dataframe
    files, classes = define_paths(tr_dir)
    train_df = define_df(files, classes)

    # validation dataframe
    files, classes = define_paths(val_dir)
    valid_df = define_df(files, classes)
    # test dataframe
    files, classes = define_paths(ts_dir)
    test_df = define_df(files, classes)
    return train_df, valid_df, test_df


if __name__ == "__main__":
    def get_data():
        train_dir ="/Users/onyekachukwuojumah/Desktop/Lung-Cancer-Detection/Data_n_experiments/train"
        test_dir = "/Users/onyekachukwuojumah/Desktop/Lung-Cancer-Detection/Data_n_experiments/test"
        valid_dir = "/Users/onyekachukwuojumah/Desktop/Lung-Cancer-Detection/Data_n_experiments/valid"
        train_df, valid_df, test_df = create_df(train_dir, valid_dir, test_dir)
        return train_df, valid_df, test_df

    