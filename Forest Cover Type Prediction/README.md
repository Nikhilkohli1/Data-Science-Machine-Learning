
# Forest Cover Type Prediction

# Abstract
The main aim of this Project is to predict the Forest Cover type for Roosevelt National Forest. Initial Exploratory data analysis is done to check the relationship between Independent variables & dependent variable(Cover_Type). The dataset after converting categorical variables to features which can be fed into a predictive model, has 54 features many of which does not have a direct relationship with the target variable. Therefore, Feature selection techniques and Significance tests are performed to get the most importance & significant features. Classification techniques such as KNN, Random Forest, logistic are used to build a predictive model. Kfold Cross-Validation & Grid Search is used to generalize the model better on the data it has not seen and tune the hyperparameters to get the best prediction. A final model was build using the most important features in a bagging algorithm and achieved an accuracy of 96% on testing data with Cross Validation.

To run the project and load the dataset, follow the below instructions - 

1. Download the dataset from - https://www.kaggle.com/uciml/forest-cover-type-dataset

2. keep all the files provided and the downloaded dataset in either the current working directory, or change the working directory to any path you like in the Jupyter Notebook. 

3. Open 'Data Preparation_Reverse_Encode.ipynb' and run it to prepare the dataset for EDA. 

4. Open 'Forest_Cover_Type_Prediction_ADS.ipynb' notebook and run it keep the same working directory where the files are. This is the main Notebook for the Assignment.

5. You will find all the steps from Data Analysis to feature Selection to Predictive Modeling for classification of Cover type. 

6. If you want to look at the rest Experiments too, you can open 'Forest_Cover_Type_Experiments_Outliers.ipynb' and run it. In this i have removed the Outliers and did predictive modeling without feature scaling. 
