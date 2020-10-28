# Predicting FIFA players value



## **Inspiration**

The main reason why I created this project is to understand what makes a football player more expensive based on different skills.
Can we find the new Messi on his very early stages?

Kaggle offers excellent datasets to start diving into the data : https://www.kaggle.com/ketanp79/fifa-19-predicting-players-market-value\

Jupyter notebooks are quite good to create and run the model as you can iterate and print the result easily.
To interact with the machine learning model , I have used tkinter as the main library.

![Image](http://www.radiohc.cu/articles/7633-fifa.jpg)

## **Overview**
This instructions will allow you to make a copy of the project locally.\
Check test execution to understand how  to deploy  and execute the Model_for_app.ipynb. \
I have created 2 extra files as a bonus so you can understand better the machine learning models and make investment decisions

You can find the following executable files:

- Model_for_app.ipynb (Main_tool) : explains the dataset, does a random forest regression and creates an app that allows you to get the value of a player based on certain parameters.
- Bonus.ipynb (Bonus_models) :  explains the dataset and does more complex machine learning models.
- under_rated_players.ipynb (Bonus_models): explains the dataset, does a random forest regression and creates a csv with the value predicted vs reality. It includes a link to a tableau dashboard so you can interact with the list and take the best decision.

## **Folder structure**
```
└── project
    ├── Bonus_models
    ├── Environment
    ├── Images
    ├── Main_tool
    ├── Raw_data
    ├── README.md
    │  
```






---


## **Pre-requisites:**

- Python 3.7 (at least)

- Sklearn 

- Pandas

- Seaborn

- Matplotlib

- os

- Time

- Conda

- Tkinter

You can find the conda environment on the file : environment.ylm



## **Instalation:**

As a rule of thumb: I do encourage you to install conda, create a working environment and download any library (mentioned above) doing : "conda install..."

Example: "conda install numpy"

## **Test execution:**

Any execution must be done from a jupyter notebook so both the model and the app works perfectly.
The machine learning model will run automatically and after it has learned , you will be able to input data in the app.





## **Usage**

1- Run all the jupyter notebook\
2- An app will pop up, input the parameters based on the following intervals:


- Parameters range: 

        - 'age' : 16-46 --> top rated players are between 23-30 years old
        - 'height_cm': 155-205
        - 'weight_kg': 49-110
        - 'nation_jersey_number': 1-99 --> best players tend to wear 1,9 or 10
        - 'shooting': 14-93 --> top forward are close to 93
        - 'passing': 20-93 --> top midfielders are close to 93
        - 'dribbling': 22-96 --> top forward are close to 96
        - 'defending': 14-90 --> top defenders are close to 90
        - 'debut_year': 1987-2020 --> assuming that on average they debut at the age of 18
3- Press the button and you will get the time of the execution and the player value\
4- Known issues : the model does not accept blank inputs\
5- Limitation: the model does only accept numerical values coming from the dataset. Ideally you can use dummy variables to increase R2 but you will not be able to create a usable GUI

![Image](https://github.com/JCGlez93/Predicting_FIFA_players_value/blob/main/app_screenshot.png)

## **To Do**

- Better explore the player position as it will probably improve the understanding of the model




## **Thanks and contact info**
Getting help from Julia Roch ,Javier Molins, Octavio García & Pedro Muñoz.
Please do email me for further questions : jcglez93@gmail.com
