import matplotlib.pyplot as plt
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
    ax.hist(data_f[columns[0]])
    ax2.hist(data_f[columns[1]])
    ax3.hist(data_f[columns[2]])
    ax.set_title("Гистограмма 1 числового параметра")
    ax3.set_title("Гистограмма 2 числового параметра")
    ax2.set_title("Гистограмма 3 числового параметра")
    plt.setp([ax, ax2, ax3], xlabel='значения выборки', ylabel='частота')
    plt.show()


def compare_category_graf(data_1, data_2, column_1, column_2, column_name):
    """
    Сопоставляет графики двух категориальных признаков
    :param data_1: первый фрейм данных
    :param data_2: второй фрейм данных
    :param column_1: столбец первого фрейма
    :param column_2: столбец второго фрейма
    :param column_name: название сопоставляемых
    :return:
    """
    n_data_1 = data_1[column_1].value_counts()
    n_data_2 = data_2[column_2].value_counts()
    fig = plt.figure(figsize=(15, 10))
    # Adds subplot on position 1
    ax = fig.add_subplot(221)
    # Adds subplot on position 2
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    ax.pie(n_data_1.values, labels=n_data_1.index)
    ax.legend(bbox_to_anchor=(0.9, 1))
    ax.set_title(f"Круговая диаграмма {column_name + ' 1'}")
    ax2.bar(x=n_data_1.index, height=n_data_1.values)
    ax2.set_title(f"Столбчатая диаграмма {column_name + ' 1'}")
    plt.setp([ax2], xlabel='значения выборки', ylabel='частота')
    ax3.pie(n_data_2.values, labels=n_data_2.index)
    ax3.legend(bbox_to_anchor=(0.9, 1))
    ax3.set_title(f"Круговая диаграмма {column_name + ' 2'}")
    ax4.bar(x=n_data_2.index, height=n_data_2.values)
    ax4.set_title(f"Столбчатая диаграмма {column_name + ' 2'}")
    plt.setp([ax2], xlabel='значения выборки', ylabel='частота')
    plt.show()


def compare_numeric_graph(data_1, data_2, column_1, column_2, column_name):
    """
    Сопоставляет графики двух числовых признаков
    :param data_1: первый фрейм данных
    :param data_2: второй фрейм данных
    :param column_1: столбец первого фрейма
    :param column_2: столбец второго фрейма
    :param column_name: название сравниваемого параметра
    """
    num_1 = data_1[column_1].dropna()
    num_2 = data_2[column_2]
    fig = plt.figure(figsize=(17, 10))
    ax = fig.add_subplot(231)
    ax2 = fig.add_subplot(233)
    ax3 = fig.add_subplot(232)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(236)
    ax6 = fig.add_subplot(235)
    ax.hist(num_1, bins=100)
    ax.set_title(f"Гистограмма {column_name} числового параметра")
    ax2.boxplot(x=num_1, data=data_1)
    ax3.set_title(f"Оценка функции плотности {column_name} "
                  f"числового параметра")
    ax2.set_title(f"Диаграмма 'ящик с усами' {column_name} "
                  f"числового параметра")
    sns.kdeplot(num_1)
    ax4.hist(num_2, bins=100)
    ax4.set_title(f"Гистограмма {column_name} числового параметра")
    ax5.boxplot(x=num_2, data=data_2)
    ax6.set_title(f"Оценка функции плотности {column_name} "
                  f"числового параметра")
    ax5.set_title(f"Диаграмма 'ящик с усами' {column_name} "
                  f"числового параметра")
    sns.kdeplot(num_2)
    plt.setp([ax, ax3, ax4, ax6], xlabel='значения выборки')
    plt.setp([ax2, ax5], xlabel='номер выборки', ylabel='разброс значений')
    plt.setp([ax, ax4], ylabel='частота')
    plt.setp([ax3, ax6], ylabel='вероятность')
    plt.show()
