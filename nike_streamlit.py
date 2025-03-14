import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Nike 2024 Global Market Data Analyze", page_icon=":chart_with_upwards_trend:",layout="wide")

st.title(" :chart_with_upwards_trend: Nike 2024")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)


#add data
fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding = "ISO-8859-1")
else:
    os.chdir(r"./")
    df = pd.read_csv("nike_sales_2024.csv", encoding = "ISO-8859-1")
       

#download database
"""Data source:"""
for_download = pd.read_csv("nike_sales_2024.csv", encoding = "ISO-8859-1")
# Convert DataFrame to CSV (in-memory)
csv_data = for_download.to_csv(index=False).encode("utf-8")

# Create a download button in Streamlit
st.download_button(
    label="Download nike_sales_2024 as CSV",
    data=csv_data,
    file_name="nike_sales_2024.csv",
    mime="text/csv"
)


df["Datetime"] = pd.to_datetime("2024 " + df["Month"], format="%Y %B", errors="coerce") \
              .dt.to_period("M") \
              .dt.to_timestamp("M")
              
# To convert a specific value to a Python datetime:
df["Datetime"] = df["Datetime"].dt.to_pydatetime()
# sidebar
st.sidebar.header("Choose the filter: ")

# Create for region
region = st.sidebar.multiselect("Pick your Region", df["Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]
    
#set the month order
sort_month = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
df2["Month"] = pd.Categorical(df2["Month"], categories=sort_month, ordered=True)
unique_months = df2["Month"].unique()
ordered_months = [m for m in sort_month if m in unique_months]
# create a column layout
month = st.sidebar.multiselect("Select Month", ordered_months)
# filter the data based on the selected month
if not month:
    df3 = df2.copy()
else:
    df3 = df2[df2["Month"].isin(month)]

st.subheader("Data for the selected Region and Month:")
st.dataframe(df3.iloc[:,:-1], use_container_width=True) # del last column, let the streamlit organized the column format




filtered_df = df.copy()  # start with the full dataset

if region:
    filtered_df = filtered_df[filtered_df["Region"].isin(region)]
if month:
    filtered_df = filtered_df[filtered_df["Month"].isin(month)]

#Revenue by Main Category  and  Revenue by Sub Category
col1, col2= st.columns((2))

main_category_df = filtered_df.groupby(by = ["Main_Category"], as_index = False)["Revenue_USD"].sum()
with col1:
    st.subheader("Revenue by Main Category")
    fig = px.bar(main_category_df, x = "Main_Category", y = "Revenue_USD", text = ['${:,.2f}'.format(x) for x in main_category_df["Revenue_USD"]],
                 template = "seaborn")
    st.plotly_chart(fig,use_container_width=True, height = 200)
    
    #add MainCategory_ViewData label under fig
    with st.expander("MainCategory_ViewData"):
        st.write(main_category_df.style.background_gradient(cmap="Blues"))
        csv = main_category_df.to_csv(index = False, float_format="%.2f").encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "MainCategory.csv", mime = "text/csv",
                            help = 'Click here to download the data as a CSV file')
    
sub_category_df = filtered_df.groupby(by = ["Sub_Category"], as_index = False)["Revenue_USD"].sum()
with col2:
    st.subheader("Revenue by Sub Category")
    fig = px.bar(sub_category_df, x = "Sub_Category", y = "Revenue_USD", text = ['${:,.2f}'.format(x) for x in sub_category_df["Revenue_USD"]],
                 template = "seaborn")
    st.plotly_chart(fig,use_container_width=True, height = 200)

    #add SubCategory_ViewData label under fig
    with st.expander("SubCategory_ViewData"):
        st.write(sub_category_df.style.background_gradient(cmap="Greens"))
        csv = sub_category_df.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "SubCategory.csv", mime = "text/csv",
                            help = 'Click here to download the data as a CSV file')

#Revenue by product line and Revenue by Price Tier
col3, col4 = st.columns((2))     
product_line_df = filtered_df.groupby(by = ["Product_Line"], as_index = False)["Revenue_USD"].sum()
with col3:
    st.subheader("Revenue by product line")
    fig = px.bar(product_line_df, x = "Product_Line", y = "Revenue_USD", text = ['${:,.2f}'.format(x) for x in product_line_df["Revenue_USD"]],
                 template = "seaborn")
    fig.update_layout(xaxis=dict(tickangle=45))  #rotation 45 degree
    st.plotly_chart(fig,use_container_width=True, height = 200)
    
    #add ProductLine_ViewData label under fig
    with st.expander("ProductLine_ViewData"):
        st.write(product_line_df.style.background_gradient(cmap="Blues"))
        csv = product_line_df.to_csv(index = False, float_format="%.2f").encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "ProductLine.csv", mime = "text/csv",
                            help = 'Click here to download the data as a CSV file')
        
price_tier_df = filtered_df.groupby(by = ["Price_Tier"], as_index = False)["Revenue_USD"].sum()
with col4:
    st.subheader("Revenue by Price Tier")
    fig = px.bar(price_tier_df, x = "Price_Tier", y = "Revenue_USD", text = ['${:,.2f}'.format(x) for x in price_tier_df["Revenue_USD"]],
                 template = "seaborn")
    st.plotly_chart(fig,use_container_width=True, height = 200)
    
    #add PriceTier_ViewData label under fig
    with st.expander("PriceTier_ViewData"):
        st.write(price_tier_df.style.background_gradient(cmap="Blues"))
        csv = price_tier_df.to_csv(index = False, float_format="%.2f").encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "PriceTier.csv", mime = "text/csv",
                            help = 'Click here to download the data as a CSV file')


#Time Series Analysis
filtered_df["Period"] = pd.to_datetime(filtered_df["Datetime"]).dt.to_period("M")
st.subheader("Time Series Analysis")
#when no region is selected as default all countries
if  not region or len(region) > 1:
# group data by both Period and Region
    linechart = (filtered_df.groupby(["Period", "Region"], as_index=False)["Revenue_USD"].sum())
    linechart = linechart.sort_values("Period")
    linechart["month_year"] = linechart["Period"].dt.strftime("%Y : %b")

    fig2 = px.line(
            linechart,
            x="month_year",
            y="Revenue_USD",
            color="Region",
            labels={"Revenue_USD": "Revenue (USD)", "Region": "Region"},
            height=500,
            width=1000,
            template="gridon"
        )
# when people select the region and month
else:
    linechart = (filtered_df.groupby("Period", as_index=False)["Revenue_USD"].sum())
    linechart = linechart.sort_values("Period")
    linechart["month_year"] = linechart["Period"].dt.strftime("%Y : %b")
    
    fig2 = px.line(
        linechart,
        x="month_year",
        y="Revenue_USD",
        labels={"Revenue_USD": "Revenue (USD)"},
        height=500,
        width=1000,
        template="gridon"
    )

st.plotly_chart(fig2, use_container_width=True) 

# sxpandable section to view and download the time series data.
with st.expander("View Data of TimeSeries:"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.iloc[:-1].to_csv(index=False).encode("utf-8")
    st.download_button("Download Data", data=csv, file_name="TimeSeries.csv", mime="text/csv")

# crea the hierarchinal treemap
st.subheader("Hierarchical view of Revenue using TreeMap")
fig3 = px.treemap(
    filtered_df,
    path=["Region", "Main_Category", "Sub_Category", "Product_Line", "Price_Tier"],
    values="Revenue_USD",
    hover_data=["Revenue_USD"],
    color="Sub_Category",  # Colors based on Sub_Category
    
)
fig3.update_layout(width=800, height=650)
st.plotly_chart(fig3, use_container_width=True)

# monthly Sub_Category revenue summary table 
import plotly.figure_factory as ff

st.subheader("Monthly Sub-Category Sales Summary")
with st.expander("Summary_Table"):
    # adjust the selected columns
    df_sample = df[0:11][["Region", "Main_Category", "Product_Line", "Price_Tier", "Month", "Revenue_USD"]]
    fig = ff.create_table(df_sample, colorscale="Cividis")
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### Monthly Sub_Category Table")
    filtered_df["month"] = filtered_df["Datetime"].dt.month_name()
    
    # create a pivot table: rows are Sub_Category and columns are month names
    sub_category_summary = pd.pivot_table(data=filtered_df, values="Revenue_USD", index=["Sub_Category"], columns="month")
    st.write(sub_category_summary.style.background_gradient(cmap="Blues"))


