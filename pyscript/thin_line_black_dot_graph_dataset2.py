import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager


# 얇은 글꼴 설정
thin_font = font_manager.FontProperties(weight='light')
# 데이터 불러오기
data1 = pd.read_excel("C:\\graph_sis\\input\\2nd_graph_no1.xlsx")
data2 = pd.read_excel("C:\\graph_sis\\input\\2nd_graph_no2.xlsx")
data3 = pd.read_excel("C:\\graph_sis\\input\\2nd_graph_no3.xlsx")
data4 = pd.read_excel("C:\\graph_sis\\input\\2nd_graph_no4.xlsx")


custom_labels1 = ["pH 3", "pH 5", "pH 7.5", "pH 9"]
custom_labels2 = ["35 °C", "25 °C", "15 °C"]
custom_labels3 = ["Red", "Green", "Blue", "White"]
custom_labels4 = ["400 μmol/m²/s", "220 μmol/m²/s", "114 μmol/m²/s", "46 μmol/m²/s"]


def plot_scatter_with_errorbars(data, custom_labels, numb, legend_prefix=''):
    fig, ax = plt.subplots(figsize=(9, 6))
    cleandata = data.dropna()
    x_col_name = 'Days'
    y_cols = [col for col in cleandata.columns if col != x_col_name]
    x_col = cleandata[x_col_name]
    markers = ['o', 'o', 'v', '^', 's', 's', 'd', 'x']
    marker_size = 50
    edge_width = 0.5
    #ax.grid(True, linewidth=0.5)

    line_styles = [
        '-',
        (0, (3, 3)),
        (0, (12, 12)),
        (0, (12, 6, 3, 6)),
        (0, (18, 6)),
        (0, (12, 6, 3, 6, 3, 6))
    ]

    legend_elements = []

    for i, y_col in enumerate(y_cols):
        fill_marker = i % 2 == 0
        face_color = 'black' if fill_marker else 'white'
        line_style = line_styles[i % len(line_styles)]

        line, = ax.plot(x_col, cleandata[y_col], color='black', linewidth=0.5,
                        linestyle=line_style, marker=markers[i],
                        markerfacecolor=face_color, markeredgecolor='black',
                        markersize=np.sqrt(marker_size), markeredgewidth=edge_width)

        legend_elements.append((line, f"{legend_prefix}{custom_labels[i]}"))

    ax.set_xlabel('Cultivation time (day)', fontsize=14, fontweight='light', fontproperties=thin_font)
    ax.set_ylabel('OD (cm⁻¹)', fontsize=14, fontweight='light', fontproperties=thin_font)
    ax.set_xlim(-0.5, 11)
    ax.tick_params(axis='both', which='major', labelsize=11, width=0.5)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontweight('normal')

    legend = ax.legend(handles=[line for line, _ in legend_elements],
                       labels=[label for _, label in legend_elements],
                       prop={'size': 10}, loc='upper left',
                       handlelength=5.0)
    legend.get_frame().set_edgecolor('black')
    legend.get_frame().set_linewidth(0.5)

    for _, spine in ax.spines.items():
        spine.set_linewidth(0.5)
        spine.set_color('black')

    fig.tight_layout()
    plt.subplots_adjust(top=0.95)

    plt.savefig(f"C:\\graph_sis\\graph\\{numb}.png", dpi=600)
    #plt.show()
    plt.close()

# 사용 예시


plot_scatter_with_errorbars(data1, custom_labels1, "2nd_no1_pH")
plot_scatter_with_errorbars(data2, custom_labels2, "2nd_no2_pH")
plot_scatter_with_errorbars(data3, custom_labels3, "2nd_no3_pH")
plot_scatter_with_errorbars(data4, custom_labels4, "2nd_no4_pH")
