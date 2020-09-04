#
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint

def expo(n):
    """
    Parameter n is a number
    Function will enlarge the number exponentially
    """
    return n**2


def date_splitter(dataframe, date_column_name):
    """
    Takes a passed in dataframe and converts the date feature into a Datetime
    column, then extracts the years, months and days to separate features.
    """
    dataframe[date_column_name] = pd.to_datetime(dataframe[date_column_name],
                                   infer_datetime_format=True)
    dataframe['Year'] = dataframe[date_column_name].dt.year
    dataframe['Month'] = dataframe[date_column_name].dt.month
    dataframe['Day'] = dataframe[date_column_name].dt.day
    dataframe.drop(date_column_name, axis=1, inplace=True)
    return dataframe


def train_validation_test_split(self, features, target,
                                    train_size=0.7, val_size=0.1,
                                    test_size=0.2, random_state=None,
                                    shuffle=True):
        '''
        This function is a utility wrapper around the Scikit-Learn train_test_split that splits arrays or 
        matrices into train, validation, and test subsets.
        
        Args:
            X (list): This is a list of features.
            y (str): This is a string with target column.
            train_size (float or int): Proportion of the dataset to include in the train split (0 to 1).
            val_size (float or int): Proportion of the dataset to include in the validation split (0 to 1).
            test_size (float or int): Proportion of the dataset to include in the test split (0 to 1).
            random_state (int): Controls the shuffling applied to the data before applying the split for reproducibility.
            shuffle (bool): Whether or not to shuffle the data before splitting
        
        Returns:
            Train, test, and validation dataframes for features (X) and target (y). 
        '''
        X = df[features]
        y = df[target]

        X_train_val, X_test, y_train_val, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, shuffle=shuffle)
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size / (train_size + val_size),
            random_state=random_state, shuffle=shuffle)
        return X_train, X_val, X_test, y_train, y_val, y_test


if __name__ == '__main__':
    print('Hello, World!')

    raw_data = load_wine()
    df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
    df['target'] = raw_data['target']

    X_train, X_val, X_test, y_train, y_val, y_test = train_validation_test_split(
        df, features=['ash', 'hue'], target='target'
    )


    breakpoint()