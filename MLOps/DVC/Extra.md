#### To check remote list in dvc

```
dvc remote list
```

#### If fsspec giving error try this

```
pip install --force-reinstall dvc
```

#### Remove tracked data

```
dvc remove data/
```


#### Rollback to a previous data version

```
dvc checkout <data-hash>
```

#### Check DVC status

```
dvc status
```