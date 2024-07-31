def return_bool(b: bool) -> str:
    res: str = "yes" if b else "no";
    return res;


def return_zugi(nl: list[int]) -> list[str]:
    res_l: list[str] = ["odd" if num%2 else "even" for num in nl];
    return res_l;

print(return_bool(True), return_bool(False));
print(return_zugi([5, 3, 2, 10, 15, 14, 14]));

