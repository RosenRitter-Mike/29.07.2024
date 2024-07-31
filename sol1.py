from func_without_return import my_statistics


# def get_int(s: str) -> int:
#     while True:
#         try:
#             num: int = int(s);
#             return num;
#         except Exception as e:
#             print(f"An {e} -- Error -- has occurred, non numerical data.");
#             break;



grades: list[int] = [];
grade: int = None;
while grade != -99:
    # grade = get_int(input("input the grade: "));
    grade = int(input("input the grade: "))
    if grade < 0 or grade > 100:
        continue;
    else:
        grades.append(grade);

my_statistics(grades);

