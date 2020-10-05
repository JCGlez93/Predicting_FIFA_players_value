#Libraries

# Data manipulation
import pandas as pd
import numpy as np
import os
# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
%matplotlib inline

# Machine Learning Algorithms
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# Model Selection and Evaluation
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

# Performance
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# For Missing Values
from sklearn.impute import SimpleImputer

# Processsing

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
import time
start_time = time.time()





#Loading dataframes and unifying

data_2015 = pd.read_csv("/home/jc/Escritorio/Data_source_final_project/players_15.csv")
data_2016 = pd.read_csv("/home/jc/Escritorio/Data_source_final_project/players_16.csv")
data_2017 = pd.read_csv("/home/jc/Escritorio/Data_source_final_project/players_17.csv")
data_2018 = pd.read_csv("/home/jc/Escritorio/Data_source_final_project/players_18.csv")
data_2019 = pd.read_csv("/home/jc/Escritorio/Data_source_final_project/players_18.csv")
data_2020 = pd.read_csv("/home/jc/Escritorio/Data_source_final_project/players_20.csv")


print(data_2016.shape)

data_2015['year'] = 2015
data_2016['year'] = 2016
data_2017['year'] = 2017
data_2018['year'] = 2018
data_2019['year'] = 2019
data_2020['year'] = 2020

raw_data = pd.concat([data_2015,data_2016,data_2017,data_2018,data_2019,data_2020] , ignore_index= True)


#selecting parameters for the app
selection = raw_data.select_dtypes(exclude =['object'] )



#print(selection.info())

selection = selection.fillna( value = selection.mean())

selection = selection.fillna( value = 0)

selection = selection[selection.value_eur != 0]






#selecting trainin dataset
selection_train =  selection[selection.year != 2020]
a = selection_train.columns.values.tolist()


#removing y value and release clause as it has a massive impact on prediction
#a.remove('value_eur')
#print(len(a))

#a.remove('release_clause_eur','gk_diving',
 #'gk_handling',
 #'gk_kicking',
 #'gk_reflexes',
 #'gk_speed',
 #'gk_positioning')


#for loop to eliminate those parameters that we want out of the model
item_list = a
new_list = []
for e in item_list:
    if e not in ('release_clause_eur','gk_diving','gk_handling','gk_kicking','gk_reflexes','gk_speed','gk_positioning','value_eur','sofifa_id','contract_valid_until'):
        new_list.append(e)
a = new_list



# definitive training sets

X_train = selection_train[a]

y_train = selection_train['value_eur']


#selecting test set

selection_test =  selection[selection.year == 2020]

X_test = selection_test[a]

y_test = selection_test['value_eur']

#Applying best model

forest_reg = RandomForestRegressor(n_estimators=50, random_state=42)
forest_reg.fit(X_train, y_train)

forest_reg.feature_importances_

#creating a dataframe with coeficients
display(pd.DataFrame(forest_reg.feature_importances_ , X_train.columns , columns = ['Coeff']).sort_values( by = ['Coeff'] , ascending = False).head(30))


prediction_randomforest = forest_reg.predict(X_test)

#print errors

forest_mse = mean_squared_error(y_test, prediction_randomforest)
forest_rmse = np.sqrt(forest_mse)
forest_rmse

#scoring

score = r2_score(y_test, prediction_randomforest)  
print('r2:',format(score*100,'.2f'),'%')

#ploting

random_forest_scatter = plt.scatter (y_test , prediction_randomforest)


# Prediction dataset summary

d = {'y_test' : y_test , 'predictions': prediction_randomforest}
df = pd.DataFrame(d)
df['difference'] = ((y_test - prediction_randomforest) / y_test) * 100
a = df['difference'].mean()
df.reset_index(inplace = True) #quitar el antiguo

print(f'Media de la diferencia entre predicción y valor real:{a}')

df.head()


print("--- %s seconds ---" % (time.time() - start_time))



#Interface

import datetime
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
Current_Date = datetime.datetime.today() 
Current_Date= str(Current_Date)

a = X_train.columns.values.tolist()
root=Tk()

root.title("Fifa tool prediction")
entries = []
cont=0

#label3 = Label(root, text= display(X_train.describe())).grid(row = 7 , column = 100 )
for y in (a):
       
    my_label = Label(root, text = a[cont] )
    my_label.grid(row = cont ,column= 4 , pady=5 )
    my_label.config(font=("Arial", 10))
    cont = cont +1

for i in range(len(a)):
    en = Entry(root)
    en.grid(row=i, column=0)
    entries.append(en)
    i = i +1

def execute():
    lista= []
    for entry in entries:
        #print(entry.get())
        lista.append(entry.get())
    #print(lista)
    df = pd.DataFrame(columns=a )
    df.loc[0] = lista
    display(df)
    print(type(df))
    prediction_randomforest = forest_reg.predict(df)
    prediction_randomforest = int(prediction_randomforest)
    display(prediction_randomforest)
    print(type(prediction_randomforest))
    
    label = Label(root, text= f'Hola, su programa ha sido ejecutado con éxito en el dia {Current_Date}').grid(row = 5 , column = 1000 )
    #label.config(font=("Arial", 12))
    label2 = Label(root, text= f'El valor de este jugador es:  {prediction_randomforest /1000000} M €').grid(row = 7 , column = 1000 )
    
    

button=Button(root,text="Execute model",command=execute).grid(row = 10 , column = 1000 )

root.mainloop()

print("--- %s seconds ---" % (time.time() - start_time))
