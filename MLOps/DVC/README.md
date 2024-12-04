## How to run this DVC

#### Install DVC and Dagshub

```
pip install dvc
pip install dagshub
```

#### Initialize Git repository and DVC

```
git init
dvc init
```

#### Add and commit DVC initialization

```
git add .dvc .dvcignore
git commit -m "Initialize DVC"
```


#### Add DAGsHub remote storage

```
dvc remote add origin https://dagshub.com/[username]/[repository].dvc
```

#### Configure remote authentication

```
dvc remote modify origin --local auth basic
dvc remote modify origin --local user [your-dagshub-username]
dvc remote modify origin --local password [your-dagshub-token]
```

#### Add a data directory to DVC tracking

```
dvc add data/
```

#### Stage and commit DVC tracking files

```
git add data.dvc .gitignore
git commit -m "Add data directory to DVC tracking"
```

#### Pull and Push in dagshub

```
dvc pull -r origin
dvc push -r origin
git push origin main
```






