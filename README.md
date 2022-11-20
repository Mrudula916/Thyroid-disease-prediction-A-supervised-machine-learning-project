# Thyroid-disease-prediction-A-supervised-machine-learning-project
Abstract
	
	Globally, thyroid dysfunction is one of the most common diseases in people. 5 in every 100 people are estimated to have it. It cannot be cured but can be treated before it becomes severe. Therefore, the project aims to analyze different classification algorithms like Logistic regression, Decision Tree, Random Forest and K-nearest Neighbors and Support Vector Machine.  It was observed that Random Forest and Decision Tree had similar results. Decision Tree reported an accuracy of 99.17%. Random Forest recorded an accuracy of 99.58%.


Preprocessing:
	
		
		Dataset Description:
			The dataset chosen is from Kaggle. It has data points of about 3773 observations with  30 corresponding features. The target variable for our models is “binayClass”. The rest of the variables are both categorical as well as continuous. Continuous features include TT4, T3 etc. Categorical features, which are boolean, include features such as pregnant, Psych etc. 
		
		Data Pre-processing:
			The dataset had a few issues with it including outliers, missing values and issues with data type. Hence, initially before working on missing values outliers had to be removed. By statistical principles, data points that are 1.5 times away from the 1st and 3rd Interquartile range can be considered as an outlier in the dataset. By applying this, the outliers from the dataset were removed.  After removing the outliers, the missing values need to be replaced. The mean of the data in each column was used to replace the null values in the corresponding columns. Lastly, the issues pertaining to categorical variables were corrected. Some categorical variables like on Thyroxine, on Thyroxine, on Antithyroid Medication etc were present in the dataset as characters. We converted such columns into 0s and 1s.
	
		Feature Selection:
			Post Pre-processing the dataset was in the right format for Feature Selection to be done. For this process, correlation matrix, visualised using the “seaborn” library known as heat maps, was used. A correlation matrix is a table showing correlation coefficients between variables. Each cell in the table shows the correlation between two variables. 

The Correlation values were found to be in the range between -0.4 to 1.0. In order to not lose important features, a threshold for the correlation had to be chosen. The threshold chosen was 0.02 and features with correlation above 0.02 with the target variable was chosen as an important feature.  

Conclusion:
The thyroid predictor helps in  identification of high-risk individuals and provides an opportunity for early detection and intervention to prevent or delay the onset of goiter and increased health care expenditures. Types  of  Thyroid dysfunction are crucial to correctly identify people with the condition . Such information is also a key to advise patients about their thyroid  health appropriately and stratify their future risk. 
Thyroid disease should be diagnosed earlier before it ends in goiter. To help doctors or medical experts in prediction of thyroid dysfunction among patients easily, this project has developed a Thyroid Disease Prediction using Decision Tree Classification Algorithm. The user-friendly design of the application, Thyroeidís, enables the user to get the prediction easily.
