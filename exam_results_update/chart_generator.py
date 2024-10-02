"""chart_generator.py

该 module 用于从传入的 `exam_results.csv` 中更新考试成绩趋势图表。
"""

import os
import subprocess

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties

# 指定字体文件路径
FONT_PATH = "HarmonyOS_Sans_SC_Regular.ttf"

if not os.path.exists(FONT_PATH):
    print(f"字体文件 {FONT_PATH} 不存在，开始下载...")
    subprocess.run(["python", "font_getter.py"], check=True)
else:
    print(f"字体文件 {FONT_PATH} 已存在，跳过下载。")

# 加载字体
font = FontProperties(fname=FONT_PATH, size=12)

# 设置全局字体
plt.rcParams["font.serif"] = [font.get_name()]
plt.rcParams["axes.unicode_minus"] = False  # 使负号正常显示

# 读取 CSV 文件
FILE_PATH = "exam_results.csv"
df = pd.read_csv(FILE_PATH)

# 转换日期列的数据类型
df["日期"] = pd.to_datetime(df["日期"])

# 设置日期作为索引
df.set_index("日期", inplace=True)

# 绘制各科目成绩趋势
plt.figure(figsize=(9, 6))  # 调整图表大小
for subject in ['语文', '数学', '英语', '物理', '化学', '生物']:
    plt.plot(df.index, df[subject], marker='o', label=subject)
plt.title('各科目成绩趋势', fontproperties=font)
plt.xlabel('日期', fontproperties=font)
plt.ylabel('分数', fontproperties=font)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., prop=font)  # 将图例放在外部
plt.grid(True)
plt.tight_layout()  # 调整布局
plt.savefig('scores_trend.png')

# 绘制各科目排名趋势
plt.figure(figsize=(9, 6))  # 调整图表大小
for subject_rank in ['语文排名', '数学排名', '英语排名', '物理排名', '化学排名', '生物排名']:
    plt.plot(df.index, df[subject_rank], marker='o', label=subject_rank)
plt.title('各科目排名趋势', fontproperties=font)
plt.xlabel('日期', fontproperties=font)
plt.ylabel('排名', fontproperties=font)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., prop=font)  # 将图例放在外部
plt.grid(True)
plt.tight_layout()  # 调整布局
plt.gca().invert_yaxis()  # 反转 y 轴
plt.savefig('ranks_trend.png')

# 绘制总分及排名趋势
fig, ax1 = plt.subplots(figsize=(9, 6))

# 绘制总分
ax1.set_xlabel("日期", fontproperties=font)
ax1.set_ylabel("总分", color="#5BCEFA", fontproperties=font)
ax1.plot(df.index, df["总分"], marker="o", label="总分", color="#5BCEFA")
ax1.tick_params(axis="y", labelcolor="#5BCEFA")

# 创建第二个 y 轴
ax2 = ax1.twinx()
ax2.set_ylabel("排名", color="#F5A9B8", fontproperties=font)
ax2.plot(df.index, df["总分排名"], marker="o", label="总分排名", color="#F5A9B8")
ax2.tick_params(axis="y", labelcolor="#F5A9B8")

# 设置标题和图例
plt.title("总分及排名趋势", fontproperties=font)
fig.tight_layout()  # 调整布局
ax1.legend(loc="upper left", prop=font)
ax2.legend(loc="upper right", prop=font)

# 保存和显示图表
plt.savefig("total_scores_and_ranks_trend.png")
