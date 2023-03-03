import matplotlib.pyplot as plt
from scipy.stats import sigmaclip
import seaborn as sns


def build_category_graf(data_f, column):
    """
    Строит набор графиков для категориального признака
    :param data_f:
    :param column:
    :return:
    """
    n_data = data_f[column].value_counts()
    fig = plt.figure(figsize=(20, 10))
    # Adds subplot on position 1
    ax = fig.add_subplot(121)
    # Adds subplot on position 2
    ax2 = fig.add_subplot(122)
    ax.pie(n_data.values, labels=n_data.index)
    ax.legend(bbox_to_anchor=(0.9, 1))
    ax.set_title(f"Круговая диаграмма {column}")
    ax2.bar(x=n_data.index, height=n_data.values)
    ax2.set_title(f"Столбчатая диаграмма {column}")
    plt.setp([ax2], xlabel='значения выборки', ylabel='частота')
    ax2.tick_params(labelrotation=330)
    plt.show()


def build_numeric_graph(data_f, column):
    """
    Строит набор графиков для числового признака
    :param data_f: исходный фрейм данных
    :param column: название колонки
    """
    num = data_f[column].dropna()
    fig = plt.figure(figsize=(17, 5))
    ax = fig.add_subplot(131)
    ax2 = fig.add_subplot(133)
    ax3 = fig.add_subplot(132)
    ax.set_title(f"Гистограмма {column}")
    ax3.set_title(f"Оценка функции плотности {column}")
    ax2.set_title(f"Диаграмма 'ящик с усами' {column}")
    plt.setp([ax, ax3], xlabel='значения выборки')
    plt.setp([ax2], ylabel='номер выборки', xlabel='разброс значений')
    plt.setp([ax], ylabel='частота')
    plt.setp([ax3], ylabel='вероятность')
    try:
        ax.hist(num, bins=50)
        ax2.boxplot(x=num, data=data_f, vert=False)
        num.plot.kde()
        plt.show()
    except TypeError:
        print("График не может быть построен, т.к."
              " содержит некорректные значения")


def build_three_hists(data_f, columns):
    """
    Строит гистограммы для трёх числовых параметров
    :param data_f: исходный фрейм с данными
    :param columns:
    """
    fig = plt.figure(figsize=(17, 5))
    ax = fig.add_subplot(131)
    ax2 = fig.add_subplot(133)
    ax3 = fig.add_subplot(132)
    ax.hist(data_f[columns[0]], bins=25)
    ax2.hist(data_f[columns[1]], bins=25)
    ax3.hist(data_f[columns[2]], bins=25)
    ax.set_title("Гистограмма 1 числового параметра")
    ax3.set_title("Гистограмма 2 числового параметра")
    ax2.set_title("Гистограмма 3 числового параметра")
    plt.setp([ax, ax2, ax3], xlabel='значения выборки', ylabel='частота')
    plt.show()


def compare_category_graf(data_1, data_2, column_1, column_2):
    """
    Сопоставляет графики двух категориальных признаков
    :param data_1: первый фрейм данных
    :param data_2: второй фрейм данных
    :param column_1: столбец первого фрейма
    :param column_2: столбец второго фрейма
    :return:
    """
    n_data_1 = data_1[column_1].value_counts()
    n_data_2 = data_2[column_2].value_counts()
    fig = plt.figure(figsize=(20, 15))
    # Adds subplot on position 1
    ax = fig.add_subplot(221)
    # Adds subplot on position 2
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    ax.pie(n_data_1.values, labels=n_data_1.index)
    ax.legend(bbox_to_anchor=(0.9, 1))
    ax.set_title(f"Круговая диаграмма {column_1 + ' до изменения'}")
    ax2.bar(x=n_data_1.index, height=n_data_1.values)
    ax2.set_title(f"Столбчатая диаграмма {column_1 + ' до изменения'}")
    plt.setp([ax2, ax4], xlabel='значения выборки', ylabel='частота')
    ax3.pie(n_data_2.values, labels=n_data_2.index)
    ax3.legend(bbox_to_anchor=(0.9, 1))
    ax3.set_title(f"Круговая диаграмма {column_1 + ' после изменения'}")
    ax4.bar(x=n_data_2.index, height=n_data_2.values)
    ax4.set_title(f"Столбчатая диаграмма {column_1 + ' после изменения'}")
    ax.tick_params(labelsize="small", labelrotation=330)
    ax2.tick_params(labelrotation=330)
    ax4.tick_params(labelrotation=330)
    plt.setp([ax2], xlabel='значения выборки', ylabel='частота')
    plt.show()


def quantile_method(data_frame, column):
    """
    Удаляет пропуски методом квантилей
    :param data_frame: исходный фрейм данных
    :param column: название колонки для вычисления
    :return: обновлённый фрейм данных
    """
    q25 = data_frame[column].quantile(0.25)
    q75 = data_frame[column].quantile(0.75)
    delta = q75 - q25
    low, high = [(q25 - 1.5 * delta), (q75 + 1.5 * delta)]
    dropped_values = data_frame[column][(data_frame[column] < low) |
                                        (data_frame[column] > high)]
    data_frame = data_frame.drop(dropped_values.index)
    return data_frame


def sigma_method(data_frame, column):
    """
    Удаляет пропуски методом сигм
    :param data_frame: фрейм данных
    :param column: название колонки фрейма
    :return: обновлённый фрейм данных
    """
    data = data_frame.dropna()
    _, low, high = sigmaclip(data[column], 3, 3)
    # c < mean(c) - std(c)*low c > mean(c) + std(c)*high
    # (std - стандартное отклонение)
    dropped_values = data_frame[column][(data_frame[column] < low) |
                                         (data_frame[column] > high)]
    data_frame = data_frame.drop(dropped_values.index)
    return data_frame
