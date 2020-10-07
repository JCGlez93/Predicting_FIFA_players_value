# Predicting_FIFA_players_value

## **Overview:**



This piece of code :


1-Extracts data from different sources \
2-Does data wrangling\
3-Executes a random forest regressor\
4-Creates an app where you can input different parameter and get the value of those players based ont the prediction.



This instructions will allow you to make a copy of the project locally.\
Check test execution to understand how  to deploy the project.


![Image](http://www.radiohc.cu/articles/7633-fifa.jpg)
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



## **Instalation:**

As a rule of thumb: I do encourage you to install conda, create a working environment and download any library (mentioned above) doing : "conda install..."

Example: "conda install numpy"

## **Test execution:**

Any execution must be done from a jupyter notebook so both the model and the app works perfectly.
The machine learning model will run automatically and after it has learned , you will be able to input data in the app.



## **Core technical concepts and inspiration**

The main reason why I created this is to understand what makes a football player more expensive based on different skills.
Can we find the new Messi on his very early stages?

Jupyter notebooks are quite good to create and run the model as you can iterate and print the result easily.
To interact with the machine learning model , I have used tkinter as the main library.

## **Usage**

1- Run all the jupyter notebook\
2- An app will pop up, input the parameters based on the following intervals:


- Parameters: 

        - 'age' : 16-46
        - 'height_cm': 155-205
        - 'weight_kg': 49-110
        - 'overall': 44-94
        - 'potential : 44-95
        - 'wage_eur': 1000-565000
        - 'international_reputation': 1-5
        - 'weak_foot': 1-5
        - 'skill_moves': 1-5
        - 'team_jersey_number': 1-99
        - 'nation_jersey_number': 1-99
        - 'pace': 21-99
        - 'shooting': 14-93
        - 'passing': 20-93
        - 'dribbling': 22-96
        - 'defending': 14-90
        - 'physic': 27-92
        - 'year': 2015-2022
3- Press the button and you will get the time of the execution and the player value\
4- Known issues : the model does not accept blank inputs\
5- Limitation: the model does only accept numerical values coming from the dataset. Ideally you can use dummy variables to increase R2 but you will not be able to create a usable GUI




        


## **Bonus**
- I created another file called bonus where I used dummy variables and created a better machine learning algorithm.\
- Feel free to use it as template for other projects



## **Thanks and contact info**
Getting help from Julia Roch & Pedro Muñoz.
Please do email me for further questions : jcglez93@gmail.com
