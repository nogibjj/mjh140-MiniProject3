'''Returns descriptive statistics for the Iris dataset.'''

import os
import polars as ps
import matplotlib.pyplot as plt

def import_iris(file_name: str):
    '''Converts csv file to dataframe'''

    if not isinstance(file_name, str):
        raise TypeError("file_name must be a string")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    new_path = parent_dir + "/data"
    file_path = os.path.join(new_path, file_name)

    try:
        iris_df = ps.read_csv(file_path)
        cols = set(iris_df.columns) - {'Id'}
        reduced_iris = iris_df[list(cols)]
        return reduced_iris
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"The file ({file_name}) was not found.") from exc
    
def get_descriptive_statistics(df: ps.DataFrame):
    '''Returns descriptive statistics for the Iris dataset.'''

    if not isinstance(df, ps.DataFrame):
        raise TypeError("df must be a polars.DataFrame")

    return df.describe()

def plot_iris_data(df: ps.DataFrame):
    '''Plots the Iris dataset.'''

    if not isinstance(df, ps.DataFrame):
        raise TypeError("df must be a polars.DataFrame")
    
    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(9, 4))
    axs[0].boxplot(df.to_numpy(), labels=df.columns)
    
    #plt.savefig("SepalLength_Scatterplot_by_Species.png")

    plt.show()

if __name__ == "__main__":
    df = import_iris("iris_data.csv")
    print(get_descriptive_statistics(df))
    plot_iris_data(df)



