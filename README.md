# DESCRIPTION OF THE PROJECT
The aim of the project appears to be to build a machine learning pipeline that can classify messages into one or more categories.

 The project is divided into three main parts:

1. ETL Pipeline (Extract, Transform, Load): The process_data.py file contains Python code to create an ETL pipeline. The goal is to retrieve emergency text messages and their classifications from a given dataset, clean the data, and store it in an SQLite database.
2. ML Pipeline: The train_classifier.py file contains Python code to create an ML pipeline. The dataset is divided into a training and test set. A sklearn machine learning pipeline is created using NLTK (Natural Language Toolkit), incorporating hyperparameter optimization via Grid Search. The ML model uses the AdaBoost algorithm for multi-output classification to predict the classification of text messages.
3. Web App: The web application allows users to enter an emergency message. Users can view the categories of the message in real-time.

#  INSTALLATION
We installed Anaconda and python 3.x.x for using packages installed for EDA or modeling.

Connect to Python prompt and with the help of 'pip install' install :

flask, pickle, plotly, nltk, SQLAlchemy

# INSTRUCTIONS FOR RUNNING THE SCRIPT

To follow these steps, you need to open a command prompt or terminal and navigate to the directory where your project files are located. Then, you can execute the commands provided.

Here's how you can do it step by step:

1. Launch the ETL Pipeline: Open a command prompt or terminal. Navigate to the directory where your project files are located. Execute the following command to run the ETL pipeline: python data/process_data.py data/messages.csv data/categories.csv data/Disaster_Clean.db
   
2. Launch the ML Pipeline and Create the Model: After the ETL pipeline has finished processing the data and creating the SQLite database, execute the following command to run the ML pipeline and create the model: python models/train_classifier.py data/Disaster_Clean.db models/classifier.pkl
   
3. Launch the Server Web: Navigate to the "app" folder in your project directory. Execute the following command to run the Flask web server: python run.py
Once you see the confirmation message that the Flask server is running, open your web browser and go to http://0.0.0.0:3001/ to access the web application.
