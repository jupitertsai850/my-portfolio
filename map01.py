

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:15:13 2021

@author: user
"""


#在地圖上標點

# 讀取資料
import pandas as pd

# 指定欄位標題
df = pd.read_excel("sampleHOUSE.xlsx",sheet_name="工作表1")
#usecols=["年別", "細分", "合計"]
          
from folium.plugins import MarkerCluster
import folium
# 創建地圖
m = folium.Map(location=[25.0431, 121.539723],zoom_start=8)
# 將資料點加到地圖上
marker_cluster = MarkerCluster().add_to(m)


resolution, width, height = 75, 10, 5
######################################################
def pic(district,district_label):
    import pandas as pd
    df0 = pd.read_excel("全部行政區整理.xlsx",sheet_name="工作表1")
    # resolution, width, height = 75, 10, 5
    station = '42'
    #png = 'mpld3_{}.png'.format(station)設定像素
    import base64
    import matplotlib.pyplot as plt
    x2 = df0["time"]
    y2 = df0[district]
    x3 = df0["time"]
    y3 = df0["taipei"]
    fig, ax = plt.subplots()
    ax.plot(x2, y2, 'r-', label = district_label)
    ax.plot(x3, y3, 'b--', label = '台北市成交均價')
    
    import matplotlib.ticker as ticker
    #設定x軸顯示密度
    ticker_spacing = 5
    ax.xaxis.set_major_locator(ticker.MultipleLocator(ticker_spacing))
    plt.xticks(rotation = 45)
    
    #設定x y軸顯示文字
    ax.set_ylabel('成交均價(萬)')
    ax.set_xlabel("year")
    
    #顯示圖例
    ax.legend()
    # 將字體換成SimHei
    plt.rcParams['font.sans-serif'] = ['SimSun']
    # 修復負號顯示問題
    plt.rcParams['axes.unicode_minus']=False
    png = 'mpld3_{}.png'.format(station)
    fig.savefig(png, dpi=resolution)
    encoded = base64.b64encode(open(png,'rb').read()).decode()
    return encoded
################################################################
encoded_Daan = pic("Daan","大安區成交均價")
encoded_Songshan = pic("Songshan","松山區成交均價")
encoded_Zhongzheng = pic("Zhongzheng","中正區成交均價")
encoded_Beitou = pic("Beitou","北投區成交均價")
encoded_Xinyi = pic("Xinyi","信義區成交均價")
encoded_Datong = pic("Datong","大同區成交均價")
encoded_Zhongshan = pic("Zhongshan","中山區成交均價")
encoded_Wanhua = pic("Wanhua","萬華區成交均價")
encoded_Neihu = pic("Neihu","內湖區成交均價")
encoded_Nangang = pic("Nangang","南港區成交均價")
encoded_Wenshan = pic("Wenshan","文山區成交均價")
encoded_Shilin = pic("Shilin","士林區成交均價")

#######################################################
def makemap():
    from folium import IFrame   
    # click = "<br><img src='data:image/png;base64,{}'>".format
    # information = "地址:"+row["地址"]+"<br>"+"房型:"+row["房型"]+"<br>"+"樓層:"+str(row["樓層"])+"<br>"+"坪數:"+str(row["坪數"])+"<br>"+"總價:"+str(row["總價"])+"萬"
    iframe = IFrame(html=html, width=500, height=395)
    
    # pp= folium.Html(click, script=True)
    # popup = folium.Popup(pp, max_width=2650)
    popup = folium.Popup(iframe, max_width=900, parse_html = True)
    folium.Marker(
        #標記作標位置
        location=[row["緯度"], row["經度"]],
        #在標記中添加資訊:坪數、金額、房型...
        #target='_blank'新開起一個分頁
        popup = popup,
        tooltip = str(row["單價"])+"萬",
        #設定標記樣式
        icon=folium.map.Icon(color='orange',icon='fa-home', prefix='fa')
    ).add_to(marker_cluster)
    

# <img src="//fps.hfcdn.com/v1/image/?key=NF58Ko5oaCstxtuy8FKKGW6affjpxVuYK_84uBC_YRTdEjWtZq-gLIe6hKQhd2KYzhxlNAx_tGVI54tDXXIxDa64od0jAbOZrBTGt_NC0NxMCtyFz-LqpYF32GTxpmDwu98NT3cksTOdfCdPPdyK1_N9HMTZXsUAyjpali26c6J_UcZAyQ6OY8h6hel3VR43ENfxb3ybinD1pLSJbiNqVK0HvUCdwmIej3oTKAUpGV_uaBnxbTilp1fX2bWndLGVD65c9FXqRr4LLeFhDWsjpnxVDzqECz6hkx18ZiGb0bSDbRH1vKF2evD98w8XKTbClCu7_yjYz6HULES1bYZTjYyTPs4omUl0IxdffhJyRF3RtY2itbcg_RIdJYyVH7G3bJENeZqhwTM&amp;width=1024&amp;height=768" onerror="PicFilter(this, 0);">


for index,row in df.iterrows():
    if row["總價"]>0:
        url = row['網址']
        loc = row["地址"]
        room = row["房型"]
        floor = row["樓層"]
        num = row["坪數"]
        price = row["總價"]
        unit_price = row["單價"]
        district = row["行政區"]

        if district == "大安區":                      
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Daan, width=200, height=100)
            makemap()    

        elif district == "士林區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Shilin, width=200, height=100)
            makemap()    

        elif district == "中正區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Zhongzheng, width=200, height=100)
            makemap()     
            
        elif district == "北投區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Beitou, width=200, height=100)
            makemap()
            
        elif district == "內湖區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Neihu, width=200, height=100)
            makemap()           
 
        elif district == "文山區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Wenshan, width=200, height=100)
            makemap()
            
        elif district == "萬華區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Wanhua, width=200, height=100)
            makemap()    
            
        elif district == "信義區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Xinyi, width=200, height=100)
            makemap() 
        elif district == "大同區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Datong, width=200, height=100)
            makemap()     
        elif district == "中山區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Zhongshan, width=200, height=100)
            makemap()              
        elif district == "南港區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Nangang, width=200, height=100)
            makemap()            
        elif district == "松山區":  
            click = f"<b>詳細資訊: </b><a href={url} target='_blank'>click here</a><br>"+f"<b>地址: </b><a>{loc}</a><br>"+f"<b>樓層: </b><a>{floor}</a><br>"+f"<b>房型: </b><a>{room}</a><br>"+f"<b>坪數: </b><a>{num}</a><br>"+f"<b>總價: </b><a>{price}</a><b>萬</b><br>"+f"<b>單價: </b><a>{unit_price}</a><b>萬/坪</b><br>"
            svg = "<img src='data:image/png;base64,{}'>".format
            html = click+svg(encoded_Songshan, width=200, height=100)
            makemap()   
            
m.add_child(folium.GeoJson(data=(open("COUNTY_MOI_1090820.json", "r", encoding="utf-8-sig")).read()))

m.save("maptest02.html")




