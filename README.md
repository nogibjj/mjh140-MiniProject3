# Descriptive Statistics with Pandas and Matplotlib   [![GitHub Actions](https://github.com/nogibjj/mjh140-MiniProject3/workflows/CI/badge.svg)](https://github.com/nogibjj/mjh140-MiniProject3/actions)


## Summary:

This project introduces the Polars package for generating descriptive statistics on the Iris Species dataset. Matplotlib package was used to create a scatterplot visualization of Sepal Length vs Petal Length for all Species. For more info on the Iris Species dataset, visit the following link:

https://www.kaggle.com/datasets/uciml/iris?resource=download

## Structure

```text
├── .devcontainer
│   ├── Dockerfile
│   └── devcontainer.json
├── data
│   └── iris_data.csv
├── .github/workflows
│   └── actions.yml
├── .gitignore
├── Makefile
├── README.md
├── requirements.txt
├── SepalLengthVsPetalLength.png
├── src
│   ├── __init__.py
│   └── polars_statistics.py
└── tests
    ├── __init__.py
    └── test_polars.py

```

## Results:

The following table of descriptive statistics was outputed from the `describe_iris` function within `src/descriptive_statistic.py`:

┌────────────┬───────────────┬───────────────┬────────────────┬──────────────┬──────────────┐
│ describe   ┆ PetalLengthCm ┆ SepalLengthCm ┆ Species        ┆ PetalWidthCm ┆ SepalWidthCm │
│ ---        ┆ ---           ┆ ---           ┆ ---            ┆ ---          ┆ ---          │
│ str        ┆ f64           ┆ f64           ┆ str            ┆ f64          ┆ f64          │
╞════════════╪═══════════════╪═══════════════╪════════════════╪══════════════╪══════════════╡
│ count      ┆ 150.0         ┆ 150.0         ┆ 150            ┆ 150.0        ┆ 150.0        │
│ null_count ┆ 0.0           ┆ 0.0           ┆ 0              ┆ 0.0          ┆ 0.0          │
│ mean       ┆ 3.758667      ┆ 5.843333      ┆ null           ┆ 1.198667     ┆ 3.054        │
│ std        ┆ 1.76442       ┆ 0.828066      ┆ null           ┆ 0.763161     ┆ 0.433594     │
│ min        ┆ 1.0           ┆ 4.3           ┆ Iris-setosa    ┆ 0.1          ┆ 2.0          │
│ 25%        ┆ 1.6           | 5.1           ┆ null           ┆ 0.3          ┆ 2.8          │
│ 50%        ┆ 4.4           ┆ 5.8           ┆ null           ┆ 1.3          ┆ 3.0          │
│ 75%        ┆ 5.1           ┆ 6.4           ┆ null           ┆ 1.8          ┆ 3.3          │
│ max        ┆ 6.9           ┆ 7.9           ┆ Iris-virginica ┆ 2.5          ┆ 4.4          │
└────────────┴───────────────┴───────────────┴────────────────┴──────────────┴──────────────┘
|  Describe  | PetalLengthCm | SepalLengthCm |     Species    | PetalWidthCm | SepalWidthCm |
| ---------- | ------------- | ------------- | -------------- | ------------ | ------------ |
│ count      ┆ 150.0         ┆ 150.0         ┆ 150            ┆ 150.0        ┆ 150.0        │
│ null_count ┆ 0.0           ┆ 0.0           ┆ 0              ┆ 0.0          ┆ 0.0          │
│ mean       ┆ 3.758667      ┆ 5.843333      ┆ null           ┆ 1.198667     ┆ 3.054        │
│ std        ┆ 1.76442       ┆ 0.828066      ┆ null           ┆ 0.763161     ┆ 0.433594     │
│ min        ┆ 1.0           ┆ 4.3           ┆ Iris-setosa    ┆ 0.1          ┆ 2.0          │
│ 25%        ┆ 1.6           | 5.1           ┆ null           ┆ 0.3          ┆ 2.8          │
│ 50%        ┆ 4.4           ┆ 5.8           ┆ null           ┆ 1.3          ┆ 3.0          │
│ 75%        ┆ 5.1           ┆ 6.4           ┆ null           ┆ 1.8          ┆ 3.3          │
│ max        ┆ 6.9           ┆ 7.9           ┆ Iris-virginica ┆ 2.5          ┆ 4.4          |


The following boxplot visualization for Sepal Length distribution by Species was created from the `visualize_iris` function within `src/descriptive_statistic.py`:

<p align = "center"><img src = "https://github.com/nogibjj/mjh140-MiniProject3/blob/main/SepalLengthVsPetalLength.png" width = 500px></p>
