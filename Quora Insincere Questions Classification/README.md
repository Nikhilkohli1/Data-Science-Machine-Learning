# Quora Insincere Questions Classification using Deep Learning

The objective is to predict whether a question asked on Quora is sincere or not.
An insincere question is defined as a question intended to make a statement rather than look for helpful answers. Some characteristics that can signify that a question is insincere:

- Has a non-neutral tone
- Has an exaggerated tone to underscore a point about a group of people
- Is rhetorical and meant to imply a statement about a group of people
- Is disparaging or inflammatory
- Suggests a discriminatory idea against a protected class of people, or seeks confirmation of a stereotype
- Makes disparaging attacks/insults against a specific person or group of people



You can find the data and Embeddings used from the below link - 
https://www.kaggle.com/c/quora-insincere-questions-classification/data

Steps to run - 

1. Download the data and save it. Change the working directory of Jupyter notebook to the same path where the data is. 
2. Run the '1. Quora Insincere Questions EDA & Topic Modeling.ipynb'. It has the detailed EDA and Topic Modeling of Quora Questions. 
3. Run the next notebook '2. Quora Insincere Questions Baseline Logistic.ipynb'. It contains the baseline model using Logistic Regression
4. Run the notebook '3. Quora Insincere Questions Deep Learning Models.ipynb'. It has all the Deep learning models i trained. 
5. Run the final notebook '4. Quora Insincere Classification Hyperparameter Effects.ipynb'. It has the models trained after tuning various hyperparameters(Cost function, Optimizer, Activation Function, Epochs etc,) and observing their effects on accuracy and how quickly the network plateaus. 





