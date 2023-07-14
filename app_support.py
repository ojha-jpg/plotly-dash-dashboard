import pandas as pd
import plotly.express as px
from dash import html

#labels
labels ={
    "Date" : "" ,
    "Power_from_gas_engine" : "Power Generation(MW) ",
    "Daily_NEA" : "Daily Power Consumption from NEA (MW) " ,
    "Total_Power" : "Total Power Consumption (MW)" ,
    "Total_power_per_ML" : "Total Power consumption per ML (Kwhr/ML)" ,
    "Raw_sew_flow" : "Raw Sewage Flow(MLD)" ,
    "Raw_sew_com_pH" : " pH" ,
    "Raw_sew_com_BOD" : " BOD (mg/l)" ,
    "Raw_sew_com_COD" : " COD (mg/l)" ,
    "Raw_sew_com_TSS" : " TSS (mg/l)" ,
    "Raw_sew_com_N" : " Ammonical Nitrogen (mg/l)" ,
    "Raw_sew_com_OG" : " Oil and Grease (mg/l)" ,
    "Raw_sew_pH" : " pH" ,
    "Raw_sew_BOD" : " BOD (mg/l)" ,
    "Raw_sew_COD" : " COD (mg/l)" ,
    "Raw_sew_TSS" : " TSS (mg/l)" ,
    "Raw_sew_TP" : " Phosphorus (mg/l)" ,
    "Raw_sew_TColi" : "Total Coliform (mg/l)" ,
    "Raw_sew_FColi" : "Fecal Coliform (mg/l)" ,
    "Grit_TSS" : " Grit TSS (mg/l)" ,
    "PST_pH" : "pH" ,
    "PST_TSS" : "TSS (mg/l)",
    "PST_BOD" : "BOD (mg/l)" ,
    "PST_COD" : "COD (mg/l)" ,
    "PST_Sludge" : "PST Sludge Volume (m3)" ,
    "SC_pH" : "pH " ,
    "SC_TSS" : "TSS (mg/l)" ,
    "SC_BOD" : "BOD (mg/l)" ,
    "SC_COD" : "COD (mg/l)" ,
    "SC_RAS" : "TSS RAS (mg/l)" ,
    "SST_pH" : "pH " ,
    "SST_TSS" : "TSS (mg/l)" ,
    "SST_BOD" : "BOD (mg/l)" ,
    "SST_COD" : "COD (mg/l)" ,
    "SST_RAS" : "TSS RAS (mg/l)" ,
    "CCT_com_pH" : "pH" ,
    "CCT_com_BOD" : "BOD (mg/l)" ,
    "CCT_com_COD" : "COD (mg/l)" ,
    "CCT_com_TSS" : "TSS (mg/l)" ,
    "CCT_com_OG" : "Oil and Grease (mg/l)" ,
    "CCT_com_N" : "Ammonical Nitrogen (mg/l)" ,
    "CCT_pH" : "pH " ,
    "CCT_BOD" : "BOD (mg/l)" ,
    "CCT_COD" : "COD (mg/l)" ,
    "CCT_TSS" : "TSS (mg/l)" ,
    "CCT_TColi" : "Total Coliform (mg/l)" ,
    "CCT_FColi" : "Fecal Coliform (mg/l)" ,
    "CCT_FRC" : " Free Residual Chlroine (mg/l)",
    "Existing_AT_pH" : "pH" ,
    "Existing_AT_DO" : "Dissolved Oxygen (mg/l)" ,
    "Existing_AT_MLSS" : "MLSS (mg/l)" ,
    "Existing_AT_MLVSS" : "MLVSS (mg/l)" ,
    "Existing_AT_SV30" : "SV30" ,
    "Existing_AT_SVI" : "Sludge Volume Index (SVI)" ,
    "New_AT_pH" : "pH" ,
    "New_AT_DO" : "Dissolved Oxygen (mg/l)" ,
    "New_AT_MLSS" : "MLSS (mg/l)" ,
    "New_AT_MLVSS" : "MLVSS (mg/l)" ,
    "New_AT_SV30" : "SV30" ,
    "New_AT_SVI" : "Sludge Volume Index (SVI)" 
}

# Load Data
def load_data():
    df = pd.read_csv("Processed_data\data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return(df)

#figures
# if condition hatauna milxa but data prepare garna parxa 

def make_graphs(df,list_of_graphs):
    figures={}
    for para in list_of_graphs:
        figname = "fig" + str(para)
        figname = px.line(df,y=para, x='Date', line_shape="spline",height=300,title = labels[para])
        figname.update_layout(
            margin=dict(l=0, r=10, t=30, b=10),
            xaxis_title=None,
            yaxis_title=None,
            title_x=0.5)
        
        if para =="CCT_pH":
            figname.add_hrect(y0=6.5, y1=8, line_width=0, fillcolor="green", opacity=0.2)
        elif para == "CCT_BOD" or para == "CCT_TSS" or para == "CCT_com_OG":
            figname.add_hrect(y0=0, y1=10, line_width=0, fillcolor="green", opacity=0.2)
            #figname.add_hline(y=10)
        elif para == "CCT_COD":
            #figname.add_hline(y=250)
            figname.add_hrect(y0=0, y1=250, line_width=0, fillcolor="green", opacity=0.2)
        elif para == "CCT_TColi":
            figname.add_hrect(y0=0, y1=500, line_width=0, fillcolor="green", opacity=0.2)
        elif para == "CCT_FColi":
                figname.add_hrect(y0=0, y1=100, line_width=0, fillcolor="green", opacity=0.2)
        elif para == "CCT_com_N":
            #figname.add_hline(y=50)
            figname.add_hrect(y0=0, y1=50, line_width=0, fillcolor="green", opacity=0.2)
        elif para == "CCT_FRC":
            #figname.add_hline(y=1)
            figname.add_hrect(y0=0, y1=1, line_width=0, fillcolor="green", opacity=0.2)
        

        figures.update({str(para):figname})
    return figures


#Landing page ko html ya bata suru 

# def landing_page_ko_html():
#     return(
#         [html.P("hahaha hora bhuniya")]
#     )
    
    
