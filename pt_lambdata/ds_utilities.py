import pandas as pd

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

if __name__ == '__main__':
    print('Hello, World!')