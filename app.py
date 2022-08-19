import plotly.express as px
import pandas as pd
import streamlit as st



df = pd.read_csv('df.csv')
st.set_page_config(layout="wide")

col1, col2 = st.columns((3,1))

st.sidebar.title('Dengue Fieber')

y_value = st.sidebar.selectbox('Y-Daten', sorted(df),key=1)
x_value = st.sidebar.selectbox('X-Daten', sorted(df),index=1,key=2)

df_show = df[[str(x_value) ,str(y_value)]]
col2.dataframe(df_show)
line_fig = px.scatter(df,
                    x=x_value,
                    y=y_value,
                    color='Stadt',
                    hover_data=sorted(df),
                    template='simple_white',
                    labels={'city':'Stadt'}
                    )

newnames = {'sj' : 'San Juan, Puerto Rico', 'iq' : 'Iquitos, Peru'}
line_fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))

line_fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', })


col1.plotly_chart(line_fig,  use_container_width=True)

st.markdown("""---""")


st.sidebar.markdown("""---""")

y_value_2 = st.sidebar.selectbox('Y-Daten', sorted(df),index= 18, key=3)
x_value_2 = st.sidebar.selectbox('X-Daten ', sorted(df),index=17, key=4)

col1, col2 = st.columns((3,1))

df_show_2 = df[[str(x_value_2) ,str(y_value_2)]]
col2.dataframe(df_show_2)
line_fig_2 = px.scatter(df,
                    x=x_value_2,
                    y=y_value_2,
                    color='Stadt',
                    template='simple_white',
                    labels={'city':'Stadt'}
                    )

newnames = {'sj' : 'San Juan, Puerto Rico', 'iq' : 'Iquitos, Peru'}
line_fig_2.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))

line_fig_2.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', })

col1.plotly_chart(line_fig_2,  use_container_width=True)

