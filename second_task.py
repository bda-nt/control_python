import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

radius = 4
num_circle_points = 360


def monte_carlo_pi(number_points, num_digits_after_decimal_points=4):
    # Получение координат точек для круга и квадрата
    square_x = [1 * radius, -1 * radius, -1 * radius, 1 * radius, 1 * radius]
    square_y = [1 * radius, 1 * radius, -1 * radius, -1 * radius, 1 * radius]

    circle_x = (np.cos(np.pi * np.arange(num_circle_points + 1) / 180) * radius)
    circle_y = (np.sin(np.pi * np.arange(num_circle_points + 1) / 180) * radius)

    # Генерация рандомных точек и их раскраска
    df_monte_carlo_pi = pd.DataFrame(columns=['x', 'y', 'r', 'Location', 'CurrentPi'])
    df_monte_carlo_pi['x'] = np.random.default_rng().uniform(-radius, radius, (number_points,))
    df_monte_carlo_pi['y'] = np.random.default_rng().uniform(-radius, radius, (number_points,))
    df_monte_carlo_pi['r'] = np.sqrt(df_monte_carlo_pi['x'] ** 2 + df_monte_carlo_pi['y'] ** 2)
    df_monte_carlo_pi.loc[df_monte_carlo_pi['r'] <= radius, 'Location'] = 'Inside'
    df_monte_carlo_pi.loc[df_monte_carlo_pi['r'] > radius, 'Location'] = 'Outside'
    df_monte_carlo_pi['CurrentPi'] = 4 * (df_monte_carlo_pi['Location'] == 'Inside').cumsum() / (df_monte_carlo_pi.index - 1)

    # Подсчет числа пи и процент ошибки
    pi_value = np.round(np.array(df_monte_carlo_pi['CurrentPi'])[-1], num_digits_after_decimal_points)
    pi_error = np.round(round(100 * ((pi_value - np.pi) / np.pi), 4), num_digits_after_decimal_points)

    # Отображение точек на рисунке
    plt.figure(figsize=(8, 8))
    plt.plot(square_x, square_y, color='#000000')
    plt.plot(circle_x, circle_y, color='#0000CC')
    sns.scatterplot(x='x', y='y', data=df_monte_carlo_pi, hue='Location', palette='colorblind')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Расположение рандомных точек')
    plt.show()

    # Вывод сообщения на экран
    print(f'Pi is approximately {pi_value}')
    print(f'This is {pi_error}% off the true value.')


if __name__ == "__main__":
    monte_carlo_pi(1000)
