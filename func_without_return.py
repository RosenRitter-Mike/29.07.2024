import statistics as st
# # a
# def my_ascending(a: int = 0, b: int = 0) -> None:
#     """ function receives 2 params of int type (default 0 ,0) and prints all integers between them """
#     for i in range(min(a, b), max(a, b) +1):
#         print(i);
#
#
# my_ascending(-12, 7);
# # help(my_ascending());
#
#
# # b
# def my_details(s: str = "AI is the best") -> None:
#     """ function receives a string and prints first mid and last char"""
#     print(f"first: {s[0]}, mid: {s[len(s)//2]}, last: {s[len(s) - 1]}");
#
#
# my_details();
# #help(my_details())
#
# # c
# def say_bool(b: bool = False) -> None:
#     """ function receives a bool (default = False) prints yes if True and no if False """
#     print("yes") if b else print("no");
#
#
# say_bool(True);
# say_bool(False);
# # help(say_bool())
#
#
# # d
# def print_zugi(nl: list[int]) -> None:
#     """ function receives a list of int and prints for each of them if they are even or odd  """
#     for  num in nl:
#         print("odd", end=", ") if num%2 else print("even", end=", ");
#
#
# print_zugi([5, 3, 2, 10, 15, 14, 14]);
# # help(print_zugi())


# e
def my_statistics(grades: list[int]) -> None:
    """ function receives a list of int representing  grades and prints statistical data  """
    sc_laude: int = 0;
    fail: int = 0;
    for grade in grades:
        if grade > 90:
            sc_laude += 1;
        if grade < 55:
            fail += 1;
    print(f"lowest grade: {min(grades)}, highest grade: {max(grades)}, mean grade: {st.mean(grades)}, median grade: {st.median(grades)}"
          f"\nfailing students: {fail}, suma_cum_laude students: {sc_laude}\nstandard deviation: {st.pstdev(grades)}");

# help(my_statistics())