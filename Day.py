# DAY CLASS - Used to represent a day at the school. This class holds all the periods and simulates the spread
class Day():
    def __init__(self, period1, period2, period3, period4):
        # Array to hold all the periods in chronological order
        self.periods = [period1, period2, period3, period4]
        # Dictionary to hold the courses along with the values of infected and non-infected students
        self.courseNames = {}
        # This function is used to loop through the periods and simulate a day at the schoo
        self.determineSpread()

    # This function loops through the periods in a day, and then all the unique classes happeneing during that period and calculates points to assign to people in that class
    def determineSpread(self):
        # Loop through periods
        for period in self.periods:
            # Loop over courses
            for course in period:
                # We use this function to determine if someone has passed a threshold of sickness (ex: 50 points) and then append them to the infected people array
                course.updatedInfected()

                # Get course name and append the section
                courseName = course.name + " " + course.section
                peopleInClass = course.peopleInClass  # Get people in class list
                infectedPeople = course.infectedPeople  # Get infected people in class list
                # These two variables are used to get the old values of infected and non-infected people in the class
                oldInfectedPeople = 0
                oldPeople = 0

                # Check if this is a concurrent period or not (such as period 2 or period 4) by seeing if this class has been added to the dictionary
                if courseName not in self.courseNames:
                    self.courseNames[courseName] = [
                        oldInfectedPeople, len(peopleInClass)]
                # If it is not a concurrent course, then we add it into the dictionary with the name as the key and the value as the infected and non-infected people
                else:
                    oldPeople = self.courseNames[courseName][1]
                    oldInfectedPeople = self.courseNames[courseName][0]
                    # Delete from dictionary since germs will be cleaned at lunch
                    del self.courseNames[courseName]

                # This is where points are calculated. Points by contact means that you recieve points for coming into close contact with someone who is infected. Points are determined mathematically
                pointsByContact = ((len(infectedPeople) *
                                    3) / len(peopleInClass)) * 100
                # Points by germs means you recieve points based on germs on a uncleaned surface. We calculate this by using the previous classes ratio of sick people to non-sick people but it is only calculated when there has been a previous class
                if oldInfectedPeople == 0:
                    pointsByGerms = 0
                else:
                    pointsByGerms = (oldInfectedPeople /
                                     (oldPeople + oldInfectedPeople)) * 100

                totalSickPoints = pointsByContact + pointsByGerms  # Total the points

                # Loop through the people in that class and add the sick points to their student class
                for person in peopleInClass:
                    person.updateInfection(totalSickPoints)