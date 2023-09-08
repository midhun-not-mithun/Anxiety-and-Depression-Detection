# Anxiety-and-Depression-Detection
**Detecting mental health illness like anxiety and depression from social media using Natural Language Processing
**

Here, the process begins with the collection of raw data from various social networking sites. 
This data is then pre-processed to identify and remove missing data and to reduce the original data so as to use the meaningful and reliable data set (Feature Extraction) for better results. 
Some common feature extraction techniques are:
Principle Components Analysis (PCA) :- PCA is one of the most used linear dimensionality reduction techniques. When using PCA, we take as input our original data and try to find a combination of the input features which can best summarize the original data distribution so that to reduce its original dimensions.
T-distributed Stochastic Neighbour Embedding (t-SNE) :- t-SNE is non-linear dimensionality reduction technique which is typically used to visualize high dimensional datasets. It is extensively applied in image processing, NLP , genomic data and speech processing.
This pre-processed data is then subjected to sampling after which it is split into training and testing data sets. 
Training data set is again pre-processed to perform:
Feature Selection :- It is a process of reducing the number of input variables when developing a predictive model. It is desirable to reduce the number of input variables to both reduce the computational cost of modeling and, in some cases, to improve the performance of the model. 
Feature Scaling :- It is a method used to normalize the range of independent variables or features of data. 
Dimensionality Reduction :- It reduces the time and storage space required. Removal of multicollinearity improves the interpretation of the parameters of the machine learning model. It becomes easier to visualize the data when reduced to very low dimensions such as 2D or 3D.
This data set is then subjected to the learning algorithm. 
Hyperparameter optimization is done, that is, hyperparameter optimization or tuning is the problem of choosing a set of optimal hyperparameters for a learning algorithm. A hyperparameter is a parameter whose value is used to control the learning process. 
Next is post-processing where performance matrix and model selection is taken into consideration. Common performance matrix are:
Confusion matrix :- It is the easiest way to measure the performance of a classification problem where the output can be of two or more types of classes.
Accuracy :- Accuracy in classification problems is the number of correct predictions made by the model over all kinds predictions made.
Precision :- It is defined as the number of correct documents returned by our ML model.
The testing data set is used to test the model and predict the accuracy.
