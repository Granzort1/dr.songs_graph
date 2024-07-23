import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


def plot_scatter_with_errorbars(data, custom_labels, numb):
    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(6, 4))
    cleandata = data.dropna()
    x_col_name = 'Days'
    y_cols = [col for col in cleandata.columns if col != x_col_name]
    x_col = cleandata[x_col_name]
    markers = ['o', 's', 'D', '^', 'p', 'h', 'd', 'x']
    colors = ['black', 'blue', 'red', 'green', 'purple', 'orange', 'navy']
    marker_size = 35  # 마커 크기 조정
    edge_width = 2    # 엣지 두께 조정
    # 라벨 색인을 위한 변수
    ax.grid(True)
    # 임계값 설정
    threshold = 1e-10

    for i in range(0, len(y_cols), 3):
        scatter_col = y_cols[i]
        ymin_col = y_cols[i + 1]
        ymax_col = y_cols[i + 2]


        # scatter 그리기
        ax.plot(x_col, cleandata[scatter_col], color=colors[i // 3], linewidth=2, alpha=0.7)
        ax.scatter(x_col, cleandata[scatter_col], marker=markers[i // 3], color='None', edgecolor=colors[i // 3], s=marker_size, linewidths=edge_width, label=custom_labels[i // 3], alpha=0.9)

        # 에러바 계산
        yerr_lower = cleandata[scatter_col] - cleandata[ymin_col]
        yerr_upper = cleandata[ymax_col] - cleandata[scatter_col]

        # 임계값을 사용하여 매우 작은 값이면 0으로 처리
        yerr_lower = np.where(np.abs(yerr_lower) < threshold, 0, yerr_lower)
        yerr_upper = np.where(np.abs(yerr_upper) < threshold, 0, yerr_upper)

        # 에러바 그리기
        ax.errorbar(x_col, cleandata[scatter_col],
                    yerr=[yerr_lower, yerr_upper],
                    fmt='none', color='gray', capsize=5)


    # 축 설정
    ax.set_xlabel('Cultivation time (day)', fontsize=16, fontweight='bold')
    ax.set_ylabel('OD (cm⁻¹)', fontsize=16, fontweight='bold')
    ax.set_xlim(0, 14)
    # 눈금 설정
    # 눈금 설정
    ax.tick_params(axis='both', which='major', labelsize=11)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontweight('bold')

    # 레전드 설정
    legend = ax.legend(prop={'size': 10, 'weight': 'bold'}, loc='upper left')
    legend.get_frame().set_edgecolor('black')  # 레전드 테두리 색상 설정
    legend.get_frame().set_linewidth(2)  # 레전드 테두리 두께 설정

    # 축 테두리 설정
    for _, spine in ax.spines.items():
        spine.set_linewidth(2)
        spine.set_color('black')
    # 레이아웃 조정
    fig.tight_layout()
    plt.subplots_adjust(top=0.95)


    plt.savefig(f"C:\\graph_sis\\graph\\{numb}.png", dpi=1000)
    plt.show()
    plt.close()

# 사용 예시


plot_scatter_with_errorbars(data1, custom_labels1, "1번")
plot_scatter_with_errorbars(data21, custom_labels21, "2.1번")
plot_scatter_with_errorbars(data22, custom_labels22, "2.2번")
plot_scatter_with_errorbars(data31, custom_labels31, "3.1번")
plot_scatter_with_errorbars(data32, custom_labels32, "3.2번")
plot_scatter_with_errorbars(data4, custom_labels4, "4번")