import streamlit as st
import pandas as pd
import numpy as np

def process_data(df_all_original, df_KSA):
    df_all = df_all_original.copy()
    df_all=df_all[df_all["Mecra Türü"]=="TV"].reset_index(drop=True)
    df_all=df_all[~df_all["Başlangıç Saati"].isna()].reset_index(drop=True)
    df_all.insert(0, "country", "turkey")
    df_all=df_all.rename(columns={"Tarih":"c_trans_date"})
    df_all.insert(2, "tv_program_from_hour", 0)
    df_all.insert(3, "tv_program_from_minute", 0)
    df_all.insert(4, "tv_program_from_second", 0)
    df_all=df_all.drop(columns=["Yıl","AY","Haftanın Günleri","Mecra Türü"])
    df_all.insert(5, "tv_spot_start_time_hour", df_all["Başlangıç Saati"].astype(str).apply(lambda x: int(x[-8:-6])))
    df_all.insert(6, "tv_spot_start_time_minute", df_all["Başlangıç Saati"].astype(str).apply(lambda x: int(x[-5:-3])))
    df_all.insert(7, "tv_spot_start_time_second", df_all["Başlangıç Saati"].astype(str).apply(lambda x: int(x[-2:])))
    df_all.insert(8, "tv_ad_15_minutes_interval", 0)
    df_all.insert(9, "booking_agency", "STARCOM MEDIA VEST GROUP")
    df_all.insert(10, "distributor", df_all["Reklam Veren"])
    df_all.insert(11, "sector_code", 0)
    df_all.insert(12, "sector", df_all["Ana Sektör"])
    df_all.insert(13, "category_code", 0)
    df_all.insert(14, "category", df_all["KATEGORİ"])
    df_all.insert(15, "product_code", 0)
    df_all.insert(16, "product", df_all["Ürün Türü"])
    df_all.insert(17, "brand_code", 0)
    df_all.insert(18, "brand", df_all["Marka"])
    df_all.insert(19, "subbrand_code", 0)
    df_all.insert(20, "subbrand", df_all["Ürün - Hizmet"])
    df_all.insert(21, "spot", df_all["Spot Tipi"])
    df_all.insert(22, "tv_program_name", "program")
    df_all.insert(23, "break_number", 1)
    df_all.insert(24, "total_breaks_in_program", 1)
    df_all.insert(25, "spot_number", df_all["Spotun Kuşak İçindeki Sırası"].apply(lambda x: int(x.split(" / ")[0])))
    df_all.insert(26, "total_spots_in_break", df_all["Spotun Kuşak İçindeki Sırası"].apply(lambda x: int(x.split(" / ")[1])))
    df_all.insert(27, "page_number", np.nan)
    df_all.insert(28, "total_pages_in_publication", np.nan)
    df_all.insert(29, "press_ad_color", np.nan)
    df_all.insert(30, "visual_size", np.nan)
    df_all.insert(31, "press_size", np.nan)
    df_all.insert(32, "ad_language", "TR")
    df_all.insert(33, "ad_picture_name", "no_picture")
    df_all.insert(34, "media", "television")
    df_all.insert(35, "type_descr", "SATELLITE")
    df_all.insert(36, "medium", df_all["Ana Yayın"])
    df_all.insert(37, "sub_medium_code", 0)
    df_all.insert(38, "sub_medium_descr", df_all["Ana Yayın"])
    df_all.insert(39, "frequency", df_all["Adet"])
    df_all.insert(40, "space", df_all["Süre"])
    df_all.insert(41, "amount", df_all["RA Tutar TL"])
    df_all.insert(42, "brand_agency", "publicis")
    df_all.insert(43, "promotion_sponsorship", df_all["Reklam Türü"].apply(lambda x: "sponsorship" if x=="TANITIM" else "regular"))
    df_all.insert(44, "tv_program_to_hour", 0)
    df_all.insert(45, "tv_program_to_minute", 0)
    df_all.insert(46, "tv_program_to_second", 0)
    df_all.insert(47, "tv_program_type", "general")
    df_all.insert(48, "cost_of_30", 0)
    df_all.insert(49, "bwa_program", 1)
    df_all.insert(50, "country_code", "tr")
    df_all.insert(51, "spot_visual_code", 0)
    df_all.insert(52, "media_code", 1)
    df_all.insert(53, "medium_code", 0)
    df_all.insert(54, "final_media_type", "tv")
    df_all.insert(55, "program_domain", "general")
    df_all.insert(56, "program_sub_type", "general")
    df_all.insert(57, "actual_ad_size", np.nan)
    df_all.insert(58, "user_defined_field",  np.nan)
    df_all.insert(59, "producer",  df_all["Reklam Veren"])
    df_all.insert(60, "program_duration", 100)
    df_all.insert(61, "dealer_corporate", "corporate")
    df_all.insert(62, "dd", pd.DatetimeIndex(df_all["c_trans_date"]).day)
    df_all.insert(63, "mm", pd.DatetimeIndex(df_all["c_trans_date"]).month)
    df_all.insert(64, "yy", pd.DatetimeIndex(df_all["c_trans_date"]).year)
    df_all["spots_2_numbers"]=df_all["spot_number"].astype(str)+"_"+df_all["total_spots_in_break"].astype(str)
    df_all.insert(65, "spot_position", df_all["spots_2_numbers"].apply(lambda x: "first spot" if int(x.split("_")[0])<3 else "before last spot" if (int(x.split("_")[1])-int(x.split("_")[0]))<2 else "middle spots"))
    df_all.insert(66, "spot_duration", df_all["Süre"])
    df_all.insert(67, "subject", "general")
    df_all.insert(68, "ipsos_estimated_expenditure", 0)
    df_all.insert(69, "internet_website_category", np.nan)
    df_all.insert(70, "internet_device", np.nan)
    df_all.insert(71, "internet_channel", np.nan)
    df_all.insert(72, "internet_visual_digital_type", np.nan)
    df_all.insert(73, "visual_campaign", np.nan)
    df_all.insert(74, "campaign_status", np.nan)
    df_all.insert(75, "campaigns_count", 0)
    df_all.insert(76, "origin_country_by_brand", "TR")
    df_all.insert(77, "origin_country_by_subbrand", "TR")
    df_all.insert(78, "target_by_product", "TOTAL POPULATION")
    df_all.insert(79, "program_detail", "general")
    df_all.insert(80, "program_status", "recorded")
    df_all.insert(81, "ADDED_DAY", pd.DatetimeIndex(df_all["c_trans_date"]).day)
    df_all.insert(82, "ADDED_MONTH", pd.DatetimeIndex(df_all["c_trans_date"]).month)
    df_all.insert(83, "ADDED_YEAR", pd.DatetimeIndex(df_all["c_trans_date"]).year)
    def get_value(row):
        situation = row['KATEGORİ']
        if situation == 'VMS':
            return row['GRP 20+ ABC1C2']
        elif (situation == 'ORAL CARE') or (situation == 'ORALCARE'):
            return row['GRP 20-44 ABC1C2']
        else:
            return row['GRP 20+ ABC1C2']
    df_all.insert(84, "TURMAR23/Target: Haleon Arabs/DOW/TSG/GRP", df_all.apply(lambda row: get_value(row), axis=1))
    df_all.insert(85, "UAEMAR23/Target: HAleon LA/DOW/TSG/GRP", np.nan)
    df_all=df_all.iloc[:,:86]
    # Convert the 'Date' column to datetime
    df_all["c_trans_date"] = pd.to_datetime(df_all["c_trans_date"])

    # Format the 'Date' column as 'dd/mm/yy'
    df_all["c_trans_date"] = df_all["c_trans_date"].dt.strftime('%d/%m/%y')

    ### convert tv_spot_start_time_hour to 2:25 hours format, if not already.
    df_all['tv_spot_start_time_hour'] = df_all['tv_spot_start_time_hour'].apply(lambda x: int(x))
    distinct_values_in_spot_hour = df_all[['tv_spot_start_time_hour']].drop_duplicates()['tv_spot_start_time_hour'].to_list()
    if 0 in distinct_values_in_spot_hour:
        df_all.loc[df_all['tv_spot_start_time_hour'] == 0 , 'tv_spot_start_time_hour'] = 24
    if 1 in distinct_values_in_spot_hour:
        df_all.loc[df_all['tv_spot_start_time_hour'] == 1 , 'tv_spot_start_time_hour'] = 25

    columns_difference = set(df_KSA.columns).difference(set(df_all.columns))

    return df_all, columns_difference

def main():
    st.title("Turkey Data Processing App")

    # Upload files
    uploaded_all_file = st.file_uploader("Upload Turkey Data File (Excel)", type=["xlsx"])
    uploaded_ksa_file = st.file_uploader("Upload KSA Data File (Excel)", type=["xlsx"])

    if uploaded_all_file and uploaded_ksa_file:
        # Read the uploaded files into Pandas DataFrames
        df_all_original = pd.read_excel(uploaded_all_file, sheet_name="Total Spot Listesi")
        df_all = df_all_original.copy()

        df_KSA_original = pd.read_excel(uploaded_ksa_file, sheet_name="March PAn Aab")
        df_KSA = df_KSA_original.copy()

        # Process the data
        df_all_processed, columns_difference = process_data(df_all, df_KSA)

        # Display the columns difference
        st.write("Columns in df_KSA but not in df_all:")
        st.write(columns_difference)

        # Provide a download button for the processed data
        st.markdown(f"### Download Processed Data")
        st.download_button('Download file',data=pd.DataFrame.to_csv(df_all_processed,index=False), mime='text/csv')

if __name__ == "__main__":
    main()
