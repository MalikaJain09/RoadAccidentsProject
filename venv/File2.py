from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from  scipy import stats



class Accidents:

    dic={"Andhra Pradesh":1,"Arunachal Pardesh":2,"Assam":3,"Bihar":4, "Chattisgarh":5, "Goa":6, "Gujarat":7, "Haryana":8, "Himachal Pradesh":9,
         "Jammu & Kashmir":10, "Jharkhand":11, "Karnatka":12, "Kerala":13, "Madhya Pradesh":14, "Maharashtra":15, "Manipur":16, "Meghalaya":17,
         "Mizoram":18, "Nagaland":19, "Odisha":20, "Punjab":21, "Rajasthan":22, "Sikkim":23, "Tamil Nadu":24, "Tripura":25, "Uttar Pradesh":26,
         "Uttarakhand":27, "West Bengal":28, "A & N Islands":29, "Chandigarh":30, "D & N Haveli":31, "Daman & Diu":32, "Delhi(UT)":33, "Lakshadeep":34,
         "Puducherry":35}


    def dataAccidents(self,state):

        y = Accidents.dic[state]
        data = pd.read_csv("Traffic accidents by time of occurrence 2001-2014.csv")
        l1= data.Total.values
        l2= data.Year.values



        total_Road_accidents = []
        years = []
        for i in range((y-1)*36, y*36, 3):
            m = l1[i]
            #print(i)
            total_Road_accidents.append(m)
            z = l2[i]
            years.append(z)

        print(total_Road_accidents)
        print(years)

        total_RailRoad_accidents = []

        for i in range((y-1)*36+1, y*36+1, 3):
            m = l1[i]
            total_RailRoad_accidents.append(m)

        print(total_RailRoad_accidents)

        total_other_railway_accidents = []
        for i in range((y-1)*36+2, y*36+2, 3):
            m = l1[i]
            total_other_railway_accidents.append(m)

        print(total_other_railway_accidents)




        y1 = total_Road_accidents
        y2 = total_RailRoad_accidents
        y3 = total_other_railway_accidents

        x1 = years



        plt.subplot(3, 1, 1)
        plt.plot(x1, y1, 'o-')
        plt.title("{} Accidents(2001-2012)".format(state))
        plt.ylabel('Road Accidents')

        plt.subplot(3, 1, 2)
        plt.plot(x1, y2, '.-')
        plt.ylabel('RailRoad Accidents')

        plt.subplot(3, 1, 3)
        plt.plot(x1, y3, '.-')
        plt.xlabel('Years')
        plt.ylabel('Other Railway Accidents')
        plt.savefig('{} Accidents(2001-2014)'.format(state))

        plt.show()



    def dataTwoAccidents(self,state1,state2):


        data = pd.read_csv("Traffic accidents by time of occurrence 2001-2014.csv")
        l1= data.Total.values
        l2= data.Year.values

        y1 = Accidents.dic[state1]
        y2 = Accidents.dic[state2]

        total_Road_accidents1 = []
        years = []
        for i in range((y1-1)*36, y1*36, 3):
            m = l1[i]
            #print(i)
            total_Road_accidents1.append(m)
            z = l2[i]
            years.append(z)

        print(total_Road_accidents1)
        print(years)

        total_RailRoad_accidents1 = []

        for i in range((y1-1)*36+1, y1*36+1, 3):
            m = l1[i]
            total_RailRoad_accidents1.append(m)

        print(total_RailRoad_accidents1)

        total_other_railway_accidents1 = []
        for i in range((y1-1)*36+2, y1*36+2, 3):
            m = l1[i]
            total_other_railway_accidents1.append(m)

        print(total_other_railway_accidents1)


        total_Road_accidents2 = []

        for i in range((y2-1)*36, y2*36, 3):
            m = l1[i]
            #print(i)
            total_Road_accidents2.append(m)


        print(total_Road_accidents2)
        print(years)

        total_RailRoad_accidents2 = []

        for i in range((y2-1)*36+1, y2*36+1, 3):
            m = l1[i]
            total_RailRoad_accidents2.append(m)

        print(total_RailRoad_accidents2)

        total_other_railway_accidents2 = []
        for i in range((y2-1)*36+2, y2*36+2, 3):
            m = l1[i]
            total_other_railway_accidents2.append(m)

        print(total_other_railway_accidents2)

        y1a = total_Road_accidents1
        y2a = total_RailRoad_accidents1
        y3a = total_other_railway_accidents1

        y1b = total_Road_accidents2
        y2b = total_RailRoad_accidents2
        y3b = total_other_railway_accidents2

        x1 = years

        plt.subplot(3, 1, 1)
        plt.plot(x1, y1a, 'o-',label=state1)
        plt.plot(x1, y1b, 'o-',label=state2)
        plt.title("{} vs {} Accidents(2001-2012)".format(state1,state2))
        plt.ylabel('Road Accidents')
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(x1, y2a, '.-',label=state1)
        plt.plot(x1, y2b, '.-',label=state2)
        plt.ylabel('RailRoad Accidents')
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(x1, y3a, '.-',label=state1)
        plt.plot(x1, y3b, '.-',label=state2)
        plt.xlabel('Years')
        plt.ylabel('Other Railway Accidents')
        plt.legend()

        plt.savefig('{} vs {} Accidents(2001-2014)'.format(state1,state2))

        plt.show()

    def YearWise(self, year):



        data = pd.read_csv("Traffic accidents by time of occurrence 2001-2014.csv")
        l1 = data.Total.values
        l2 = data.Year.values

        y = np.where(l2 == year)
        x = list(y)
        j1 = []
        for i in range(0, len(y[0]), 3):
            print(i)
            print(x[0][i])
            j1.append(x[0][i])

        print(j1)

        roadAccidentsValues = []

        for i in range(len(j1)):
            roadAccidentsValues.append(l1[j1[i]])
        print(roadAccidentsValues)

        j2 = []
        for i in range(1, len(y[0]), 3):
            print(i)
            print(x[0][i])
            j2.append(x[0][i])

        print(j2)

        rail_roadAccidentsValues = []

        for i in range(len(j2)):
            rail_roadAccidentsValues.append(l1[j2[i]])
        print(rail_roadAccidentsValues)

        j3 = []
        for i in range(2, len(y[0]), 3):
            print(i)
            print(x[0][i])
            j3.append(x[0][i])

        print(j3)

        other_railwayAccidentsValues = []

        for i in range(len(j3)):
            other_railwayAccidentsValues.append(l1[j3[i]])
        print(other_railwayAccidentsValues)

        dic = ["AP", "AR", "AS", "BR", "CG", "GA", "GJ", "HR", "HP", "JK", "JH", "KA", "KL", "MP", "MH", "MN", "ML",
               "MZ", "NL", "OR", "PB", "RJ", "SK", "TN", "TR", "UP", "UT", "WB", "AN", "CH", "DH", "DD", "DL", "LD",
               "PY"]

        
        plt.subplot(3, 1, 1)
        plt.bar(dic, roadAccidentsValues,label="Road Accidents in {}".format(year))
        plt.legend()
        
        plt.ylabel('Road Accidents')


        plt.subplot(3, 1, 2)
        plt.bar(dic, rail_roadAccidentsValues,label="Rail Road Accidents in {}".format(year))
        plt.legend()
        
        plt.ylabel(' Rail Road Accidents')

        plt.subplot(3, 1, 3)
        plt.bar(dic, other_railwayAccidentsValues,label="Other Railway Accidents in {}".format(year))
        plt.legend()
        plt.xlabel("Name Of States")
        plt.ylabel('Other Railway  Accidents')

        plt.savefig('Accidents in INDIA in {}'.format(year))

        plt.show()

    def Pie(self, state, specificYear):

        y = Accidents.dic[state]
        data = pd.read_csv("Traffic accidents by time of occurrence 2001-2014.csv")
        l1 = data.Total.values
        l2 = data.Year.values

        total_Road_accidents = []
        years = []
        for i in range((y - 1) * 36, y * 36, 3):
            m = l1[i]
            # print(i)
            total_Road_accidents.append(m)
            z = l2[i]
            years.append(z)

        print(total_Road_accidents)
        print(years)

        total_RailRoad_accidents = []

        for i in range((y - 1) * 36 + 1, y * 36 + 1, 3):
            m = l1[i]
            total_RailRoad_accidents.append(m)

        print(total_RailRoad_accidents)

        total_other_railway_accidents = []
        for i in range((y - 1) * 36 + 2, y * 36 + 2, 3):
            m = l1[i]
            total_other_railway_accidents.append(m)

        print(total_other_railway_accidents)
        indexYear=years.index(specificYear)
        print(indexYear)
        pieList = []
        pieList.append(total_Road_accidents[indexYear])
        pieList.append(total_RailRoad_accidents[indexYear])
        pieList.append(total_other_railway_accidents[indexYear])

        labels = 'Road Accidents', 'RailRoad Accidents', 'Other Railway Accidents'
        fig1, ax1 = plt.subplots()
        ax1.pie(pieList, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')

        plt.show()
