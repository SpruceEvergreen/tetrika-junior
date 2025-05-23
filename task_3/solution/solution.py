####################################### Примечание #######################################
# В условиях не было обговорено, можно ли создавать функции кроме appearance, поэтому первый
# вариант appearance содержит повторяющиеся куски кода.
# Во втором варианте (строка 115) была создана функция check_merge_intervals, для оптимизации повторяющегося кода.
# Для теста используется pytest

####################################### Вариант 1 #######################################
def appearance(intervals: dict[str, list[int]]) -> int:
    # разбивка интервалов lesson на пары
    n = 2
    lesson_interval = [intervals["lesson"][0], intervals["lesson"][1]]

    # разбивка интервалов pupil на пары, отсеивание интервалов, которые находятся за пределами
    # интервалов lesson
    checked_intervals_pupil = []
    paired_intervals_pupil = [intervals["pupil"][i:i + n] for i in range(0, len(intervals["pupil"]), n)]

    for pair in paired_intervals_pupil:
        overlap = max(0, min(lesson_interval[1], pair[1]) - max(lesson_interval[0], pair[0]))
        if overlap > 0:
            checked_intervals_pupil.append(pair)

    # разбивка интервалов tutor на пары, отсеивание интервалов, которые находятся за пределами
    # интервалов lesson
    checked_intervals_tutor = []
    paired_intervals_tutor = [intervals["tutor"][i:i + n] for i in range(0, len(intervals["tutor"]), n)]

    for pair in paired_intervals_tutor:
        overlap = max(0, min(lesson_interval[1], pair[1]) - max(lesson_interval[0], pair[0]))
        if overlap > 0:
            checked_intervals_tutor.append(pair)

    overlaps = []

    # merging пересекающихся интервалов pupil
    checked_intervals_pupil.sort(key=lambda interval: interval[0])
    merged_intervals_pupil = [checked_intervals_pupil[0]]
    for current in checked_intervals_pupil:
        previous = merged_intervals_pupil[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged_intervals_pupil.append(current)

    # # merging пересекающихся интервалов tutor
    checked_intervals_tutor.sort(key=lambda interval: interval[0])
    merged_intervals_tutor = [checked_intervals_tutor[0]]
    for current in checked_intervals_tutor:
        previous = merged_intervals_tutor[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged_intervals_tutor.append(current)

    # сравнивание интервалов lesson, tutor, pupil на общее время в секундах
    for tutor_interval in merged_intervals_tutor:
        for pupil_interval in merged_intervals_pupil:
            # вариант 1
            # latest_start = max(pupil_interval[0], tutor_interval[0])
            # earliest_end = min(pupil_interval[1], tutor_interval[1])
            # overlap = max(0, min(earliest_end, lesson_interval[1]) - max(latest_start, lesson_interval[0]))

            # вариант 2
            overlap = max(0, min(pupil_interval[1], tutor_interval[1], lesson_interval[1]) - max(pupil_interval[0],
                                                                                                 tutor_interval[0],
                                                                                                 lesson_interval[0]))


            overlaps.append(overlap)

    # суммирование полученных пересекающихся интервалов
    result = sum(overlaps)

    return result

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

####################################### Вариант 2 #######################################
# def check_merge_intervals(intervals, lesson_interval) -> list:
#     # отсеивание интервалов, которые находятся за пределами интервалов lesson
#     checked_intervals = []
#
#     for pair in intervals:
#         overlap = max(0, min(lesson_interval[1], pair[1]) - max(lesson_interval[0], pair[0]))
#         if overlap > 0:
#             checked_intervals.append(pair)
#
#     # merging пересекающихся интервалов
#     checked_intervals.sort(key=lambda interval: interval[0])
#     merged_intervals = [checked_intervals[0]]
#     for current in checked_intervals:
#         previous = merged_intervals[-1]
#         if current[0] <= previous[1]:
#             previous[1] = max(previous[1], current[1])
#         else:
#             merged_intervals.append(current)
#
#     return merged_intervals
#
#
# def appearance(intervals: dict[str, list[int]]) -> int:
#     # разбивка интервалов на пары
#     n = 2
#     lesson_interval = [intervals["lesson"][0], intervals["lesson"][1]]
#     paired_intervals_pupil = [intervals["pupil"][i:i + n] for i in range(0, len(intervals["pupil"]), n)]
#     paired_intervals_tutor = [intervals["tutor"][i:i + n] for i in range(0, len(intervals["tutor"]), n)]
#
#     merged_intervals_pupil = check_merge_intervals(paired_intervals_pupil, lesson_interval)
#     merged_intervals_tutor = check_merge_intervals(paired_intervals_tutor, lesson_interval)
#
#     # сравнение интервалов lesson, tutor, pupil на общее время в секундах
#     overlaps = []
#     for tutor_interval in merged_intervals_tutor:
#         for pupil_interval in merged_intervals_pupil:
#             # вариант 1
#             # latest_start = max(pupil_interval[0], tutor_interval[0])
#             # earliest_end = min(pupil_interval[1], tutor_interval[1])
#             # overlap = max(0, min(earliest_end, lesson_interval[1]) - max(latest_start, lesson_interval[0]))
#
#             # вариант 2
#             overlap = max(0, min(pupil_interval[1], tutor_interval[1], lesson_interval[1]) - max(pupil_interval[0],
#                                                                                                  tutor_interval[0],
#                                                                                                  lesson_interval[0]))
#
#             overlaps.append(overlap)
#
#     # суммирование полученных пересекающихся интервалов
#     result = sum(overlaps)
#
#     return result
#
# tests = [
#     {'intervals': {'lesson': [1594663200, 1594666800],
#              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
#              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
#      'answer': 3117
#     },
#     {'intervals': {'lesson': [1594702800, 1594706400],
#              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
#              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
#     'answer': 3577
#     },
#     {'intervals': {'lesson': [1594692000, 1594695600],
#              'pupil': [1594692033, 1594696347],
#              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
#     'answer': 3565
#     },
# ]
#
# if __name__ == '__main__':
#    for i, test in enumerate(tests):
#        test_answer = appearance(test['intervals'])
#        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
