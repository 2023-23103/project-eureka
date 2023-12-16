import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.

print("loading")
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0, 1, 2],
    nrows=100
)
df = df.dropna(axis=0)

st.write(df)

    
if st.button("new sheet"):
    df1 = pd.DataFrame({"A":[1,2,3],
                   "B":[3,4,5],
                   "C":[7,8,9]})
    conn.create(worksheet="abc", data=df1)
    st.success("Done")
    
if st.button("Calculate Total Orders Sum"):
    sql = 'SELECT SUM("age") as "ass" FROM "Sheet1";'
    total_orders = conn.query(sql=sql)
    st.write(total_orders)
        
        
if st.button("insert"):
    df_copy = df.copy()
    df_copy.loc[len(df)]=["aab","dog",7]
    conn.update(worksheet="Sheet1", data=df_copy)
    st.success("Worksheet Updated 🤓")