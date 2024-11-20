import seaborn as sns
import matplotlib as plt
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv(r"C:\Users\A2Z\Desktop\Feedback\Project\Dashboard\Data\shopping_trends.csv")

st.title("Customer Feedback")

st.sidebar.header("Filter Options")


gender = st.sidebar.multiselect("Gender",
                                options=df['Gender'].unique(),
                                default=df["Gender"].unique())

min_age, max_age = st.sidebar.slider("Age",
                                     min_value = int(df['Age'].min()),
                                     max_value=int(df['Age'].max()),
                                     value = (int(df['Age'].min()),int(df['Age'].max())))

Category = st.sidebar.multiselect("Category",
                                  options=df['Category'].unique(),
                                  default=df['Category'].unique())
    
filtered_dataset = df[
    (df['Gender'].isin(gender))&
    (df['Category'].isin(Category))&
    (df['Age']>=min_age)&
    (df['Age']<=max_age)
]
st.dataframe(filtered_dataset)

st.success('Age and frequency purchase graph')
fig = px.scatter(df,df['Age'],df['Frequency of Purchases'])
st.plotly_chart(fig)



st.write("Distribution Of Purchase Amount")
fig = px.histogram(df, x='Purchase Amount (USD)')
st.plotly_chart(fig)

st.error("Types Of Item")
fig = px.pie(df,df['Item Purchased'])
st.plotly_chart(fig)

st.success("Relationship between Previous Purchase and Frequency Of Purchases")
fig = px.histogram(df,df['Previous Purchases'],df['Frequency of Purchases'], color='Previous Purchases')
st.plotly_chart(fig)


fig = px.sunburst(df, path=['Category','Size','Color'],title='Item Purchase by Category,Size,Color')
st.plotly_chart(fig)

st.error('Review Rating by Payment Method')
fig= px.box (df, x='Payment Method',y='Review Rating', color='Payment Method')
st.plotly_chart(fig)

st.success("Purchase Amount by Shipping Type")
fig = px.violin(df, x='Shipping Type', y='Purchase Amount (USD)', box=True, points="all" )
st.plotly_chart(fig)

fig = px.pie(df, names='Subscription Status', title="Subscription Status Distribution")
st.plotly_chart(fig)

fig= px.box (df, x='Gender',y='Item Purchased', color='Gender',title='Item Purchased by Gender')
st.plotly_chart(fig)