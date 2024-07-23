import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager


# 얇은 글꼴 설정
thin_font = font_manager.FontProperties(weight='light')
# 데이터 불러오기
data1 = pd.read_excel("C:\\graph_sis\\input\\test1.xlsx")
data21 = pd.read_excel("C:\\graph_sis\\input\\test21.xlsx")
data22 = pd.read_excel("C:\\graph_sis\\input\\test22.xlsx")
data31 = pd.read_excel("C:\\graph_sis\\input\\test31.xlsx")
data32 = pd.read_excel("C:\\graph_sis\\input\\test32.xlsx")
data4 = pd.read_excel("C:\\graph_sis\\input\\test4.xlsx")

custom_labels1 = ["42:10", "42:1", "140:1"]
custom_labels21 = ["4:1", "8:1", "16:1", "42:1", "70:1", "140:1"]
custom_labels22 = ["42:0.1", "42:0.5", "42:1", "42:2", "42:8", "42:16"]
custom_labels31 = ["4:1", "8:1", "16:1", "42:1"]
custom_labels32 = ["4:16", "8:16", "16:16", "42:16"]
custom_labels4 = ["10%", "25%", "50%", "100%"]


def plot_scatter_with_errorbars(data, custom_labels, numb, legend_prefix=''):
    fig, ax = plt.subplots(figsize=(9, 6))
    cleandata = data.dropna()
    x_col_name = 'Days'
    y_cols = [col for col in cleandata.columns if col != x_col_name]
    x_col = cleandata[x_col_name]
    markers = ['o', 'o', 'v', '^', 's', 's', 'd', 'x']
    marker_size = 50
    edge_width = 0.5
    ax.grid(True, linewidth=0.5)
    threshold = 1e-10

    # 수정된 선 스타일 정의
    line_styles = [
        '-',
        (0, (3, 3)),
        (0, (12, 12)),
        (0, (12, 6, 3, 6)),
        (0, (18, 6)),
        (0, (12, 6, 3, 6, 3, 6))
    ]

    # 레전드 요소를 저장할 리스트 추가
    legend_elements = []

    for i in range(0, len(y_cols), 3):
        scatter_col = y_cols[i]
        ymin_col = y_cols[i + 1]
        ymax_col = y_cols[i + 2]

        fill_marker = (i // 3) % 2 == 0
        face_color = 'black' if fill_marker else 'white'
        line_style = line_styles[i // 3 % len(line_styles)]

        # 마커와 선을 함께 그리도록 수정
        line, = ax.plot(x_col, cleandata[scatter_col], color='black', linewidth=0.5,
                        linestyle=line_style, marker=markers[i // 3],
                        markerfacecolor=face_color, markeredgecolor='black',
                        markersize=np.sqrt(marker_size), markeredgewidth=edge_width)

        # 레전드 요소 생성 및 저장
        legend_elements.append((line, f"{legend_prefix}{custom_labels[i // 3]}"))

        yerr_lower = cleandata[scatter_col] - cleandata[ymin_col]
        yerr_upper = cleandata[ymax_col] - cleandata[scatter_col]

        yerr_lower = np.where(np.abs(yerr_lower) < threshold, 0, yerr_lower)
        yerr_upper = np.where(np.abs(yerr_upper) < threshold, 0, yerr_upper)

        ax.errorbar(x_col, cleandata[scatter_col],
                    yerr=[yerr_lower, yerr_upper],
                    fmt='none', color='black', capsize=5, alpha=0.5, linewidth=0.5)

    ax.set_xlabel('Cultivation time (day)', fontsize=14, fontweight='light', fontproperties=thin_font)
    ax.set_ylabel('OD (cm⁻¹)', fontsize=14, fontweight='light', fontproperties=thin_font)
    ax.set_xlim(-0.5, 14)
    ax.tick_params(axis='both', which='major', labelsize=11, width=0.5)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontweight('normal')

    # 수정된 레전드 생성 방식
    legend = ax.legend(handles=[line for line, _ in legend_elements],
                       labels=[label for _, label in legend_elements],
                       prop={'size': 10}, loc='upper left',
                       handlelength=5.0)  # 여기서 handlelength 값을 조정
    legend.get_frame().set_edgecolor('black')
    legend.get_frame().set_linewidth(0.5)

    for _, spine in ax.spines.items():
        spine.set_linewidth(0.5)
        spine.set_color('black')

    fig.tight_layout()
    plt.subplots_adjust(top=0.95)

    plt.savefig(f"C:\\graph_sis\\graph\\{numb}.png", dpi=300)
    plt.show()
    plt.close()

# 사용 예시


plot_scatter_with_errorbars(data1, custom_labels1, "1번", legend_prefix='N to P Ratio ')
plot_scatter_with_errorbars(data21, custom_labels21, "2.1번", legend_prefix='N to P Ratio ')
plot_scatter_with_errorbars(data22, custom_labels22, "2.2번", legend_prefix='N to P Ratio ')
plot_scatter_with_errorbars(data31, custom_labels31, "3.1번", legend_prefix='N to P Ratio ')
plot_scatter_with_errorbars(data32, custom_labels32, "3.2번", legend_prefix='N to P Ratio ')
plot_scatter_with_errorbars(data4, custom_labels4, "4번", legend_prefix='Concentration of BG11 medium ')