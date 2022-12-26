import pandas as pd
import numpy as np

def main():
    symptoms = pd.read_csv("symptom.csv", sep=";")
    diseases = pd.read_csv("desieases.csv", sep=";")
    init_symptoms = np.random.randint(0,2, symptoms.shape[0])
    print(init_symptoms)
    probability = np.zeros(diseases.shape[0] - 1)
    for i in range(len(probability)):
        for j in range(len(init_symptoms)):
            if init_symptoms[j] == 1:
                probability[i] *= symptoms.iloc[i][j]
        probability[i] *= diseases.iloc[i][i] / diseases.iloc[diseases.shape[0]][1]
main()