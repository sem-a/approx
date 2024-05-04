import approx as ap
from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog
from params import *
import time as t
import matplotlib.pyplot as plt
import os

def approx():
    start_time = t.time()

    save_folder = 'results'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    n = get_n()
    h = get_h()
    mu = get_mu()
    cell_size = get_cell()

    start_point_arr = np.array( [[1, 1]] )

    solution = ap.method_euler(start_point_arr[0], n, h, mu)

    matrix_size, start_point_polygon = ap.calc_grid_size(cell_size, solution)

    start_point_arr = ap.calc_start_point(start_point_polygon, matrix_size, cell_size)

    grid = np.zeros((matrix_size, matrix_size), dtype=ap.dtype_for_matrix)

    repeat_points = np.zeros((0), dtype=ap.dtype_for_repeat_points) # an array of points 
                                                                # that change repeatedly

    repeat_points_temp = np.zeros((1), dtype=ap.dtype_for_repeat_points)

    grid, repeat_points = ap.create_grid(grid, repeat_points, matrix_size, repeat_points_temp, cell_size, start_point_arr, ap.dtype_for_repeat_points)
    
    end_time = t.time()
    print(f"Время выполнения программы: {end_time - start_time} сек.\nРазмер клетки: {cell_size}\nРазмер матрицы: {len(grid)}")

    # Сохранение данных grid в файл
    grid_filename = os.path.join(save_folder, f'{matrix_size}.txt')
    np.savetxt(grid_filename, grid[::-1], fmt='%s')

    # Сохранение данных repeat_points в файл
    repeat_points_filename = os.path.join(save_folder, f'repeat_of_{matrix_size}.txt')
    with open(repeat_points_filename, "w") as my_file:
        for string in reversed(repeat_points):
            my_file.write(f'{string}\n')

    # Сохранение графика
    plt_filename = os.path.join(save_folder, f'{matrix_size}.svg')
    plt.savefig(plt_filename)


def change_func():
    print('Изменить функцию')

# Функция для изменения параметров
def change_param():

    while True:
        # Создаем список выбора с помощью radiolist_dialog
        result = radiolist_dialog(
            title='Изменить параметры',
            text='Выберите параметр для изменения:',
            values=[
                ('ch_h', f'Изменить h (Текущее значение: h = {get_h()})'),
                ('ch_mu', f'Изменить mu (Текущее значение: mu = {get_mu()})'),
                ('ch_cell', f'Изменить cell_size (Текущее значение: cell_size = {get_cell()})'),
                ('back', 'Назад'),
            ],
        ).run()

        if result == 'ch_h':
            new_h = input_dialog(title="Изменить h", text="Введите новое значение для h:").run()
            if new_h is not None:
                set_h(float(new_h))
        elif result == 'ch_mu':
            new_mu = input_dialog(title="Изменить mu", text="Введите новое значение для mu:").run()
            if new_mu is not None:
                set_mu(float(new_mu))
        elif result == 'ch_cell':
            new_cell_size = input_dialog(title="Изменить cell_size", text="Введите новое значение для cell_size:").run()
            if new_cell_size is not None:
                set_cell(float(new_cell_size))
        elif result == 'back':
            break

# Функция для запуска интерактивного меню
def run_menu():
    # Создаем список выбора с помощью radiolist_dialog
    result = radiolist_dialog(
        title='Аппроксимация непрерывной модели мультивибратора моделью с конечным множеством состояний',
        text='Выберите опцию:',
        values=[
            ('approx', 'Аппроксимировать'),
            ('ch_params', 'Изменить параметры'),
            ('ch_system', 'Изменить систему'),
            ('exit', 'Выход'),
        ],
    ).run()

    return result

# Основная функция
def main():
    while True:
        # Запускаем меню и получаем результат
        selected = run_menu()

        # Проверяем результат и выполняем соответствующее действие
        if selected == 'approx':
            approx()
            # Здесь должен быть код для аппроксимации с использованием текущих параметров h, mu и cell_size
        elif selected == 'ch_params':
            change_param()
        elif selected == 'ch_system':
            change_func()
        elif selected == 'exit':
            # Выход из программы
            break

# Запускаем основную функцию
if __name__ == '__main__':
    main()