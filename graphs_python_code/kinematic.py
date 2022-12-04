import numpy as np

"""l3 in equation is equal to e1"""

lambda_2 = 1.75
lambda_e = 0.25
phi_k = 10 * np.pi / 9
phi_n = np.pi
l_1 = 0.02
l_2 = lambda_2 * l_1
e_1 = lambda_e * l_1


# Координаты точек/отрезков
# Координата х точки А
def dot_a_coord_x(phi):
    """ok"""
    return l_1 * np.cos(phi)


# Координата у точки А
def dot_a_coord_y(phi):
    """ok"""
    return l_1 * np.sin(phi)


# Координата х точки B
def dot_b_coord_x(phi):
    """ok"""
    return l_1 * np.cos(phi) + np.sqrt(l_2 ** 2 - (l_1 * np.sin(phi) - e_1) ** 2)


# Координата у точки B
def dot_b_coord_y(phi):
    """ok"""
    return e_1


# Координата х точки отрезка ОА
def segment_oa_coord_x(phi):
    """ok"""
    return l_1 * np.cos(phi) / 2


# Координата у точки отрезка ОА
def segment_oa_coord_y(phi):
    """ok"""
    return l_1 * np.sin(phi) / 2


# Координата х точки отрезка AB
def segment_ab_coord_x(phi):
    """ok var: old"""
    # return l_2 * np.cos(np.arcsin(module_pi((e_1 - l_1 * np.sin(phi)) / l_2))) / 2 + l_1 * np.cos(phi)
    """ok var: new"""
    return np.sqrt(l_2 ** 2 - (l_1 * np.sin(phi) - e_1) ** 2) / 2 + l_1 * np.cos(phi)


# Координата y точки отрезка AB
def segment_ab_coord_y(phi):
    """ok"""
    return (l_1 * np.sin(phi) + e_1) / 2


"""Diff part"""


# Первая производная координат точек/отрезков
# Производная координаты х точки A
def diff_dot_a_coord_x(phi):
    """ok"""
    """
    to check 
    enter: l1cos(x)
    on: https://mathdf.com/der/ru/
    """
    return -l_1 * np.sin(phi)


# Производная координаты у точки A
def diff_dot_a_coord_y(phi):
    """ok"""
    """
    to check
    enter: l1sin(x)
    on: https://mathdf.com/der/ru/
    """
    return l_1 * np.cos(phi)


# Производная координаты х точки B
def diff_dot_b_coord_x(phi):
    """ok"""
    """
    to check
    enter: sqrt(l2^2 - (l1sin(x) - l3)^2) + l1cos(x)
    on: https://mathdf.com/der/ru/
    """
    return -l_1 * np.cos(phi) * (l_1 * np.sin(phi) - e_1) / np.sqrt(
        l_2 ** 2 - (l_1 * np.sin(phi) - e_1) ** 2
    ) - l_1 * np.sin(phi)


# Производная координаты у точки B
def diff_dot_b_coord_y(phi):
    """ok"""
    """
    to check
    enter: l3
    on: https://mathdf.com/der/ru/
    """
    return 0


# Производная координаты х отрезка ОA
def diff_segment_oa_coord_x(phi):
    """ok"""
    """
    to check
    enter: l1cosx/2
    on: https://mathdf.com/der/ru/
    """
    return -l_1 * np.sin(phi) / 2


# Производная координаты y отрезка OA
def diff_segment_oa_coord_y(phi):
    """ok"""
    """
    to check
    enter: l1sinx/2
    on: https://mathdf.com/der/ru/
    """
    return l_1 * np.cos(phi) / 2


# Производная координаты х отрезка AB
def diff_segment_ab_coord_x(phi):
    """ok var: new"""
    """
    to check
    enter: sqrt(l2^2 - (l1sin(x) - l3)^2) / 2 + l1cos(x)
    on: https://mathdf.com/der/ru/
    """
    return -l_1 * np.cos(phi) * (l_1 * np.sin(phi) - e_1) / (2 * np.sqrt(
        l_2 ** 2 - (l_1 * np.sin(phi) - e_1) ** 2
    )) - l_1 * np.sin(phi)


# Производная координаты y отрезка AB
def diff_segment_ab_coord_y(phi):
    """ok"""
    """
    to check
    enter:  (l1sin(x) + l3) / 2
    on: https://mathdf.com/der/ru/
    """
    return l_1 * np.cos(phi) / 2


"""Diff2 part"""


# Вторая производная координат точек/отрезков
# Вторая производная координаты х точки А
def diff2_dot_a_coord_x(phi):
    """ok"""
    """
    to check
    enter: -l1sin(x)
    on: https://mathdf.com/der/ru/
    """
    return -l_1 * np.cos(phi)


# Вторая производная координаты у точки А
def diff2_dot_a_coord_y(phi):
    """ok"""
    """
    to check
    enter: l1cos(x)
    on: https://mathdf.com/der/ru/
    """
    return -l_1 * np.sin(phi)


# Вторая производная координаты х точки B
def diff2_dot_b_coord_x(phi):
    """ok"""
    """
    to check
    enter: -l1cosx*(l1sinx-l3)/(sqrt(l2^2 - (l1*sinx - l3)^2 )) - l1*sinx
    on: https://mathdf.com/der/ru/
    """
    return - l_1 * ((l_1 * np.cos(phi) ** 2 - np.sin(phi) * (l_1 * np.sin(phi) - e_1)) * np.sqrt(
        l_2 ** 2 - (l_1 * np.sin(phi) - e_1) ** 2) + l_1 * np.cos(phi) ** 2 * (l_1 * np.sin(phi) - e_1) ** 2 / np.sqrt(
        l_2 ** 2 - (l_1 * np.sin(phi) - e_1) ** 2)) / (l_2 ** 2 - (l_1 * np.sin(phi) - e_1) ** 2) - l_1 * np.cos(phi)


# Вторая производная координаты у точки B
def diff2_dot_b_coord_y(phi):
    """ok"""
    """
    to check
    enter: 0
    on: https://mathdf.com/der/ru/
    """
    return 0


# Вторая производная координаты х отрезка ОА
def diff2_segment_oa_coord_x(phi):
    """ok"""
    """
    to check
    enter: -l1sin(x)/2
    on: https://mathdf.com/der/ru/
    """
    return -l_1 * np.cos(phi) / 2


# Вторая производная координаты у отрезка ОА
def diff2_segment_oa_coord_y(phi):
    """ok"""
    """
    to check
    enter: -l1cos(x)/2
    on: https://mathdf.com/der/ru/
    """
    return -l_1 * np.sin(phi) / 2


# Вторая производная координаты x отрезка AB
def diff2_segment_ab_coord_x(phi):
    """ok var: old"""
    # return (1 / 2) * (
    #         -(l_2 ** 3 * np.cos(phi) ** 2) /
    #         (4 * np.sqrt(1 - 1 / 4 * (e_1 - l_2 * np.sin(phi)) ** 2))
    #         - (l_2 ** 3 * np.cos(phi) ** 2 * (e_1 - l_2 * np.sin(phi)) ** 2) /
    #         (16 * (1 - (1 / 4) * (e_1 - l_2 * np.sin(phi)) ** 2) ** (3 / 2))
    #         - (l_2 ** 2 * np.sin(phi) * (e_1 - l_2 * np.sin(phi))) /
    #         4 * np.sqrt(1 - (1 / 4) * (e_1 - l_2 * np.sin(phi)) ** 2)
    #         - 2 * l_1 * np.cos(phi)
    # )
    """ok var: new"""
    """
    to check
    enter: -l1cos(x) * (l1 * sinx - l3) / (2 * sqrt(l2 ** 2 - (l1 * sinx - l3) ** 2)) - l1 * sinx
    on: https://mathdf.com/der/ru/
    """
    return - l_1 * ((l_1 * np.cos(phi) ** 2 - np.sin(phi) * (l_1 * np.sin(phi) - e_1)) * np.sqrt(
        l_2 ** 2 - (l_1 * np.sin(phi) - e_1) ** 2) + l_1 * np.cos(phi) ** 2 * (l_1 * np.sin(phi) - e_1) ** 2 / np.sqrt(
        l_2 ** 2 - (l_1 * np.sin(phi) - e_1) ** 2)) / (2 * (l_2 ** 2 - (l_1 * np.sin(phi) - e_1) ** 2)) - l_1 * np.cos(
        phi)


# Вторая производная координаты у отрезка AB
def diff2_segment_ab_coord_y(phi):
    """ok"""
    """
    to check
    enter: l1 * cos(x) / 2
    on: https://mathdf.com/der/ru/
    """
    return -l_1 * np.sin(phi) / 2


list_of_functions = [
    dot_a_coord_x, dot_a_coord_y, dot_b_coord_x, dot_b_coord_y,
    segment_oa_coord_x, segment_oa_coord_y, segment_ab_coord_x, segment_ab_coord_y,
    diff_dot_a_coord_x, diff_dot_a_coord_y, diff_dot_b_coord_x, diff_dot_b_coord_y,
    diff_segment_oa_coord_x, diff_segment_oa_coord_y, diff_segment_ab_coord_x, diff_segment_ab_coord_y,
    diff2_dot_a_coord_x, diff2_dot_a_coord_y, diff2_dot_b_coord_x, diff2_dot_b_coord_y,
    diff2_segment_oa_coord_x, diff2_segment_oa_coord_y, diff2_segment_ab_coord_x, diff2_segment_ab_coord_y,
]
