# Hero Name Recognition

Structure of this project
```
📦hero_test
 ┣ 📂data
 ┃ ┣ 📂data_test
 ┃ ┃ ┣ 📂test_images
 ┃ ┃ ┃  ┗ 📜...image
 ┃ ┃ ┗ 📜test.txt
 ┃ ┗ 📂data_train
 ┣ 📂result
 ┃ ┣ 📜1-acc.txt
 ┃ ┣ 📜10-acc.txt
 ┃ ┣ 📜2-acc.txt
 ┃ ┣ 📜3-acc.txt
 ┃ ┣ 📜4-acc.txt
 ┃ ┣ 📜5-acc.txt
 ┃ ┣ 📜6-acc.txt
 ┃ ┣ 📜7-acc.txt
 ┃ ┣ 📜8-acc.txt
 ┃ ┗ 📜9-acc.txt
 ┣ 📂src
 ┃ ┣ 📜crawling.py
 ┃ ┣ 📜evaluation.py
 ┃ ┣ 📜localization.py
 ┃ ┣ 📜matching.py
 ┃ ┣ 📜result.txt
 ┃ ┗ 📜utils.py
 ┗ 📜README.md
 ```

## Installation
```
pip install -r requirements.txt
```

## Evaluation
Data test should be placed in `/data/data_test`

### Crawling
Gallery should be placed in `/data/data_train`. You can also crawling from scratch by do this command:

`python crawling.py`

### Prediction

You can test whold the test set in `/data/data_test` by the command line:
- First you have to cd to `src` directory by `cd src`
- Then, you just run `python evaluation.py` to test all the test set
- You can change the `top-k` variable in `evaluation.py` to calculate top-k accuracy

All result will be generate automatically and placed in `result/`
