import pandas as pd
import plotly.express as px

def info_tab(df: pd.DataFrame):
    # Calculate the number of rows
    row_length = df.shape[0]
    
    # Calculate missing values, unique values, and duplicates for each column
    nulls = df.apply(lambda col: col.isnull().sum())
    unique = df.apply(lambda col: col.nunique())
    duplicates = df.apply(lambda col: col.duplicated().sum())
    
    null_percentage = (nulls/row_length)*100
    unique_percentage = (unique/row_length)*100
    duplicate_percentage = (duplicates/row_length)*100

    # Create a summary DataFrame
    df_summary = pd.DataFrame({
        'Columns': df.columns,
        'Null %': null_percentage,
        'Unique %': unique_percentage,
        'Duplicate %': duplicate_percentage
    })
    
    # Plot the results using Plotly Express
    fig = px.bar(df_summary, 
                 x=['Unique %','Null %','Duplicate %'], 
                 y= 'Columns', 
                 title="Data Quality Checks",
                 orientation="h",
                 barmode='group',
                 opacity=0.9, 
                 text_auto=True,
                 width=900,
                 height=1000
                )
    
    # Update graph formatting
    fig.update_layout(
        title="Data Quality Checks",
        xaxis_title="Percentage",
        yaxis_title="Columns",
        legend_title="Legend",
        title_x=0.5,
        font=dict(
            family="Arial",
            size=14,
            color="Black"
        ),
        legend=dict(
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        )
    )
    fig.show()
