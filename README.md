# OEC-2021: ZBY1 Tracker

## Purpose

To help with infection control, the ZBY1 Tracker will output a list of students who have/most likely contracted the virus. This will simulate a day in the high school to determine help determine who should stay home for the next day of school.

## How To Run

1. Install PyCharm, Excel-rd, OpenPy-Excel
1. Install pandas using `pip install pandas` or in PyCharm Plugins
1. Clone the repository with `git clone https://github.com/austincolepage/OEC2021-TEAM-PHP`
1. Open the folder in PyCharm
1. Press the Run Button on `main.py`

## Classes

### **`Day(period1, period2, period3, period4)`**

`periods`: this is a list of all the periods in a day
`courseNames`: this is a dictionary/map that holds the previous period's courses  
`void determineSpread()`: this function calculates the spread throughout the day including all 4 periods

### **`Course(name, section)`**

`name`: this is the name of the class  
`section`: this is the section for the course  
`peopleInClass`: this is a list of all the people in the class  
`infectedPeople`: this is a list of all the **infected** people in the class
`void addPerson(Person)`: this function adds a person to the class as well as to the list of the people infected in the class if they are infected.  
`void updatedInfected()`: this function updates the list of the infected people in the class

### **`Person(id, lname, fname, grade, extracCurricular, conditions, infected)`**

`id`: this is the persons id  
`fname`: this is the first name of the person  
`lname`: this is the last name of the person  
`grade`: this is the grade/age of the person (a TA would be assigned a grade of 16)  
`extraCurricular`: this is a list of the person's extra curricular activities  
`conditions`: this is a list of conditions if the person has any  
`sickness`: this determines how likely you are to contract the virus  
`infected`: this states whether the person is infected or not  
`gradeFactor`: this takes into consideration your age which can affect how likely you are to contract the virus  
`healthFactor`: this takes into consideration how likely you are to contract the virus due to health complications  
`threshold`: this is the point at which we determine that your chances of contracting ZBY1 is pretty much 100%  
`void updateInfection(totalPoints)`: this function updates the chances of the person getting sick  
it takes in the number of points(aka contagiousness from others) and then calculates how sick they are based on their health issues and age.
