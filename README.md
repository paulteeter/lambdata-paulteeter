# lambdata-paulteeter
Basic Utility functions for Data Science

### Installation: 
This module can be installed using pip

`!pip install pt-lambdata`

### Features:
Basic functions for creating new features in a dataframe from dates:

booger_picker(self, date_column_name):
        
        """
        Takes a passed in dataframe and converts the date feature into
        a Datetime column, then extracts the years, months and days to
        separate features.
        """



nostril_population(
            self,
            train_size=0.7 (default)
            val_size=0.1 (default)
            test_size=0.2 (default)
            random_state=None (default)
            shuffle=True) (default)
        '''
        This function is a utility wrapper around the Scikit-Learn
        train_test_split that splits arrays or matrices into train,
        validation, and test subsets.

        Args:
            X (list): This is a list of features.

            y (str): This is a string with target column.

            train_size (float or int): Proportion of the dataset to
            include in the train split (0 to 1).

            val_size (float or int): Proportion of the dataset to
            include in the validation split (0 to 1).

            test_size (float or int): Proportion of the dataset to
            include in the test split (0 to 1).

            random_state (int): Controls the shuffling applied to
            the data before applying the split for reproducibility.

            shuffle (bool): Whether or not to shuffle the data before
            splitting

        Returns:
            Train, test, and validation dataframes for features (X)
            and target (y).
        '''