import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def show_graph():
    df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
    df.plot.bar(stacked=True)
    plt.show()


def dots_graph():
    midwest = pd.read_csv(
        "https://raw.githubusercontent.com/selva86/datasets/"
        "master/midwest_filter.csv")

    # Prepare Data
    # Create as many colors as there are unique midwest['category']
    categories = np.unique(midwest['category'])
    colors = [plt.cm.tab10(i / float(len(categories) - 1)) for i in
              range(len(categories))]

    # Draw Plot for Each Category
    plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

    for i, category in enumerate(categories):
        plt.scatter('area', 'poptotal',
                    data=midwest.loc[midwest.category == category, :],
                    s=20, c=colors[i], label=str(category))

    # Decorations
    plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
                  xlabel='Area', ylabel='Population')

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
    plt.legend(fontsize=12)
    plt.show()


if __name__ == "__main__":
    data = pd.read_excel(
        "C:\\Users\\fongr\\Documents\\Мои документы\\Второй курс\\python\\scientificProject\\data\\first_practice_dataframe.xlsx",
        sheet_name="Sheet1")
    print(data)
