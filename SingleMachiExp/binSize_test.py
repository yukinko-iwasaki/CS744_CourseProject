def main():
    data = dd.read_csv('./output.csv.gz',compression="gzip", blocksize=None)
    train, test = data.random_split([0.8, 0.2])
    train_labels = train.col1 == 1
    test_labels = test.col1 == 1
    test = test.drop(columns, axis=1)
    train = train.drop(columns, axis=1)
    train=train.drop(["Unnamed: 0"], axis=1)
    test =test.drop(["Unnamed: 0"],axis=1)

    dtrain = xgb.DMatrix(train, label = train_labels)
    dtest = xgb.DMatrix(test, label = test_labels)
    for i in range(1, 10):
    import dask.dataframe as dd
        print("number of threads: "+ str(i))
        param = {"nthread":i}
        num_round=10
        evallist = [(dtest, 'eval'), (dtrain, 'train')]
        start = time.time()
        bst=xgb.train(param,dtrain, num_round, evallist)
        print(time.time()-start)

if __name__ == "__main__":
    main()
