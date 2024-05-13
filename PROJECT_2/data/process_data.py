import sys

import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    Loading datasets.
    Args:
        messages_filepath : messages dataset file path.
        categories_filepath : categories dataset file path.
    Returns:
        df : The merged one.
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id', how='inner')
    
    return df


def clean_data(df):
      '''
    Clean the data by removing duplicates and converting category values to binary (0 or 1)
    
    Input:
    df: pandas DataFrame. The DataFrame containing the raw data.
    
    Output:
    df: pandas DataFrame. The cleaned DataFrame.
    '''
    # Split categories into separate category columns
    categories = df['categories'].str.split(';', expand=True)
    
    # select the first row of the categories dataframe
    first_row = categories.iloc[0,:]
    # Use first_row to create column names for the categories data.
    categories_names = first_row.apply(lambda n: n[:-2]) # Use only the last 2 characters of each string with slicing
    # rename the columns of `categories` with new column names
    categories.columns = categories_names
    categories.head()

    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda n: n.split('-')[1])
        # replace 2 with 1
        categories[column] = categories[column].str.replace('2','1')
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])
        
    # drop the original categories column from `df`
    df.drop('categories', axis=1, inplace=True)

    df.head()

    # concatenate df and categories data frames
    df = pd.concat([df,categories], axis=1)
    df.head()
    
    # Remove duplicates
    duplicate_count = df.duplicated().sum()
    df = df.drop_duplicates()
    return df

    
def save_data(df, database_filename):
    '''
    Save the data into a sql database. 
    Input:
        df (pandas.DataFrame): dataframe containing the dataset
        database_filename (str): database filename
    Returns:
        none
    '''
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('Clean_DATA', engine, index=False , if_exists='replace')
    
    # Close the connection to the SQLite database
    engine.dispose()
    return df
     

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
