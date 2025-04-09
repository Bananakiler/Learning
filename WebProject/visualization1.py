# 此文件为折线图形式的可视化，main.py文件中目前使用的是这个
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import io
import base64
from sql import Find_Data

def Visualization():
     # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']


    datas = Find_Data('小张')

    # 将数据转换为DataFrame
    df = pd.DataFrame(datas)

    # 转换日期字符串为datetime类型
    df['日期'] = pd.to_datetime(df['日期'])

    # 选择要可视化的指标，这里以血压为例
    df['收缩压'] = df['血压'].apply(lambda x: int(x.split('/')[0]))
    df['舒张压'] = df['血压'].apply(lambda x: int(x.split('/')[1]))
    df['空腹血糖'] = df['空腹血糖'].astype(float)
    df['胆固醇'] = df['胆固醇'].astype(float)
    df['尿酸'] = df['尿酸'].astype(float)
    df['白细胞'] = df['白细胞'].astype(float)

    # 创建图表
    fig, ax = plt.subplots(figsize=(10, 6))

    # 绘制收缩压和舒张压的变化
    plt.plot(df['日期'], df['收缩压'], marker='o', label='收缩压')
    plt.plot(df['日期'], df['舒张压'], marker='o', label='舒张压')
    plt.plot(df['日期'], df['空腹血糖'], marker='o', label='空腹血糖')
    plt.plot(df['日期'], df['胆固醇'], marker='o', label='胆固醇')
    plt.plot(df['日期'], df['尿酸'], marker='o', label='尿酸')
    plt.plot(df['日期'], df['白细胞'], marker='o', label='白细胞')

    # 设置x轴的日期格式
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.YearLocator())

    # 旋转x轴标签使其更易读
    plt.gcf().autofmt_xdate()

    # 添加图例、标题和标签
    plt.legend()
    plt.title('小张的健康状况')
    plt.xlabel('日期')
    plt.ylabel('血压 (mmHg)')

    # 将图表保存到内存中
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    # 将图片编码为base64
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url