import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# PAGE HEADER


st.image('gambor.jpg', width=1000)

st.date_input("Select a date")

st.title("Welcome to our Dashboard")
st.markdown("### Prepared by : Umar Malik and Aiman Afif")

# LOAD DATA

df = pd.read_csv("GamingData.csv")


df.columns = df.columns.str.lower().str.strip()

# RAW DATA

st.subheader("Raw Data")
st.write(df)


# OBJECTIVE 1


st.header("Objective 1")
st.write(
    "To analyze the relationship between gaming addiction score and stress level among students."
)

# Pie Chart
stress_counts = df['stress_level'].value_counts()

fig1, ax1 = plt.subplots(figsize=(7,7))

ax1.pie(
    stress_counts,
    labels=stress_counts.index,
    autopct='%1.1f%%'
)

ax1.set_title("Distribution of Stress Levels")

st.pyplot(fig1)

# GroupBy Analysis
st.subheader("Analysis")

objective1 = (
    df.groupby('stress_level')['addiction_score']
    .agg(['count', 'mean', 'min', 'max', 'std'])
)

st.write(objective1)


# OBJECTIVE 2


st.header("Objective 2")
st.write(
    "To identify whether study hours and gaming hours influence academic performance."
)

# Categorize Study Hours

df['study_category'] = pd.cut(
    df['study_hours'],
    bins=[0,2,4,6,24],
    labels=['Low','Moderate','High','Very High']
)

avg_grades = (
    df.groupby('study_category')['grades']
    .mean()
)

# Bar Chart
fig2, ax2 = plt.subplots(figsize=(8,6))

avg_grades.plot(
    kind='bar',
    ax=ax2
)

ax2.set_title("Average Grades by Study Hours Category")
ax2.set_xlabel("Study Hours Category")
ax2.set_ylabel("Average Grades")

st.pyplot(fig2)

# GroupBy Analysis
st.subheader("Analysis")

objective2 = (
    df.groupby('study_category')['grades']
    .agg(['count', 'mean', 'min', 'max', 'std'])
)

st.write(objective2)


# OBJECTIVE 3


st.header("Objective 3")
st.write(
    "To analyze the impact of sleep hours and gaming activity on students' grades."
)

# Categorize Sleep Hours

df['sleep_category'] = pd.cut(
    df['sleep_hours'],
    bins=[0,6,24],
    labels=['Low Sleep','High Sleep']
)

# Density Plot
fig3, ax3 = plt.subplots(figsize=(8,6))

df[df['sleep_category'] == 'Low Sleep']['grades'].plot(
    kind='density',
    ax=ax3,
    label='Low Sleep'
)

df[df['sleep_category'] == 'High Sleep']['grades'].plot(
    kind='density',
    ax=ax3,
    label='High Sleep'
)

ax3.set_title("Grade Distribution by Sleep Category")
ax3.set_xlabel("Grades")
ax3.set_ylabel("Density")
ax3.legend()

st.pyplot(fig3)

# GroupBy Analysis
st.subheader("Analysis")

objective3 = (
    df.groupby('sleep_category')['grades']
    .agg(['count', 'mean', 'min', 'max', 'std'])
)

st.write(objective3)


# SCATTER PLOT


st.header("Scatter Plot Gaming VS Study")

st.write(
    "Choose your preferable x-axis and y-axis."
)


numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Dropdowns for x and y axes
x_column = st.selectbox(
    "x-axis",
    numeric_columns,
    key="scatter_x"
)

y_column = st.selectbox(
    "y-axis",
    numeric_columns,
    index=1,
    key="scatter_y"
)

# Interactive Plotly scatter plot
fig4 = px.scatter(
    df,
    x=x_column,
    y=y_column,
    title=f"{y_column} vs {x_column}",
    hover_data=df.columns
)

st.plotly_chart(fig4, use_container_width=True)

st.image('aiman.jpg', width=1000)

st.markdown("---")
st.success("BSMS1306 Data Analytics Mini Project Dashboard")
