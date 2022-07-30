import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config(page_title="UAS-1900018287-RaihanHadiNafi",
                   page_icon=":bar_chart:", layout="wide")

df = pd.read_excel(
    io="penindakan-pelanggaran-lantas-2021-maret.xlsx",
    engine="openpyxl",
)
# Add 'hour' column to dataframe

data = ['bap_tilang', 'stop_operasi', 'bap_polisi', 'stop_operasi_polisi',
        'penderekan', 'ocp_roda_dua', 'ocp_roda_empat', 'angkut_motor']
df['total'] = df[data].sum(axis=1)
# view dataframe on page


# SIDEBAR
st.sidebar.header("Please Filter Here:")
wilayah = st.sidebar.multiselect(
    "Select The wilayah Type :",
    options=df["wilayah"].unique(),
    default=df["wilayah"].unique()
)


df_selection = df.query(
    "wilayah == @wilayah "
)

st.markdown("""---""")  # markdown


st.title("Data Penindakan Pelanggaran 2021 - Maret")


st.markdown("""---""")
st.dataframe(df_selection)


total_penindakan = (
    df_selection.groupby(by=["wilayah"]).sum()[
        ["total"]].sort_values(by="wilayah")
)
fig_total = px.bar(
    total_penindakan,
    x="total",
    y=total_penindakan.index,
    orientation="h",
    title="<b>Total Penindakan Pelanggaran Lalu Lintas</b>",
    color_discrete_sequence=["#EB1D36"] * len(total_penindakan),
    template="plotly_white",
)
fig_total.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_total, use_container_width=True)
total = int(df_selection["total"].sum())
st.subheader(f"Total Kasus: {total:,} Kasus")
st.markdown("""---""")

fig_penindakan = px.pie(
    df,
    names='wilayah',
    values='total',
    title="<b>Total</b>",
    hole=0.5,
)
st.plotly_chart(fig_penindakan, use_container_width=True)

total = int(df_selection["total"].sum())
st.subheader(f"Total Kasus : {total:,} Kasus")
st.markdown("""---""")

# bap_tilang
fig_bap_tilang_line = px.line(
    df,
    x='bap_tilang',
    y='wilayah',
    orientation="h",
    title=f"<b>Kasus Penilangan</b><br>",
)
st.plotly_chart(fig_bap_tilang_line, use_container_width=True)

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
