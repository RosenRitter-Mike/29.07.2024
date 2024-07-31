import func_with_return as fwr

avg1: float = fwr.my_avg(90, 99);
print(f"my_avg(90, 99): {avg1}");

head1: str = fwr.my_headline("python has conquered the world");
print(head1 * 2);

res_con: list[int] = fwr.concat_list([1, 2], [3, 4, 5, 6], [7, 8, 9]);
print(res_con, len(res_con));

