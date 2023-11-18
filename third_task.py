import pandas as pd
import matplotlib.pyplot as plt

filename = 'inputData/gender-height-weight.xlsx'
labels = ['A-рост', 'M-рост', 'S-рост', 'A-вес', 'M-вес', 'S-вес']
headers = ['Общая выборка', 'Выборка мужчин', 'Выборка женщин']


def calculate_math_wait(data_frame, column):
    math_wait = []
    for key, value in data_frame[column].value_counts().items():
        math_wait.append(key * (value / data_frame[column].count()))

    return sum(math_wait)


if __name__ == "__main__":
    data = pd.read_excel(filename)
    data["height"] = [height * 2.54 for height in data["height"]]
    data["weight"] = [weight * 0.45 for weight in data["weight"]]

    result = pd.DataFrame([
            [data["height"].mean(), data[data["gender"] == 1]["height"].mean(), data[data["gender"] == 2]["height"].mean()],
            [calculate_math_wait(data, 'height'), calculate_math_wait(data[data["gender"] == 1], 'height'), calculate_math_wait(data[data["gender"] == 2], 'height')],
            [data["height"].var(), data[data["gender"] == 1]["height"].var(), data[data["gender"] == 2]["height"].var()],
            [data["weight"].mean(), data[data["gender"] == 1]["weight"].mean(), data[data["gender"] == 2]["weight"].mean()],
            [calculate_math_wait(data, "weight"), calculate_math_wait(data[data["gender"] == 1], "weight"), calculate_math_wait(data[data["gender"] == 2], "weight")],
            [data["weight"].var(), data[data["gender"] == 1]["weight"].var(), data[data["gender"] == 2]["weight"].var()]
        ],
        labels,
        headers
    )

    print(result)

    plt.figure()

    plt.subplot(1, 3, 1)
    plt.scatter(data["height"], data["weight"], edgecolor='red', s=25, marker='^')
    plt.xlabel('Рост')
    plt.ylabel('Вес')
    plt.title("Зависимости веса от роста, общий")

    plt.subplot(1, 3, 2)
    plt.scatter(data[data['gender'] == 1]["height"], data[data["gender"] == 1]["weight"], edgecolors='green', s=25)
    plt.xlabel('Рост')
    plt.ylabel('Вес')
    plt.title("Зависимости веса от роста, мужчины")

    plt.subplot(1, 3, 3)
    plt.scatter(data[data['gender'] == 2]["height"], data[data["gender"] == 2]["weight"], edgecolors='yellow', s=25)
    plt.xlabel('Рост')
    plt.ylabel('Вес')
    plt.title("Зависимости веса от роста, женщины")
    plt.tight_layout()

    plt.show()

    plt.subplot(1, 2, 1)
    plt.hist(data[data["gender"] == 2]["weight"], bins=15)
    plt.subplot(1, 2, 2)
    plt.hist(data[data["gender"] == 2]["height"], bins=15)
    plt.show()
