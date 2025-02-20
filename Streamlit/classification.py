import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# @st.cache_data
# def load_data():
#     iris = load_iris()
#     df = pd.DataFrame(iris.data, columns=iris.feature_names)
#     df['species'] = iris.target
#     return df, iris.target_names

# df,target_names=load_data()

# model = RandomForestClassifier()
# model.fit(df.iloc[:,:-1],df['species'])

# st.sidebar.title("input features")
# sepal_length = st.sidebar.slider("sepal length", float(df['sepal length(cm)'].min()),float(df['sepal length(cm)'].max()))
# sepal_width = st.sidebar.slider("sepal width", float(df['sepal width(cm)'].min()),float(df['sepal width(cm)'].max()))
# petal_length = st.sidebar.slider("petal length", float(df['petal length(cm)'].min()),float(df['petal length(cm)'].max()))
# petal_width = st.sidebar.slider("petal width", float(df['petal width(cm)'].min()),float(df['petal width(cm)'].max()))


# input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# predication = model.predict(input_data)
# predicted_species = target_names[predication[0]]

# st.write("prediction")
# st.write("The predicted species is: {predicted_species}")

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

# Print column names for debugging
print(df.columns)

# Train the RandomForest model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# Sidebar input features
st.sidebar.title("Input Features")

# Use correct column names
sepal_length = st.sidebar.slider("Sepal length", 
    float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))

sepal_width = st.sidebar.slider("Sepal width", 
    float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))

petal_length = st.sidebar.slider("Petal length", 
    float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))

petal_width = st.sidebar.slider("Petal width", 
    float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

# Prepare input data for prediction
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Make prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]  # Fix: use indexing, not function call

# Display the result
st.write("### Prediction")
st.write(f"The predicted species is: **{predicted_species}**") 