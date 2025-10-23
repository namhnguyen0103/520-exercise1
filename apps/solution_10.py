# def mars_days_off(n: int):
#     full_weeks = n // 7
#     extra_days = n % 7

#     min_off = full_weeks * 2
#     max_off = min_off + min(2, extra_days)

#     print(min_off, max_off)

# # Example usage:
# if __name__ == "__main__":
#     n = int(input())
#     mars_days_off(n)


n=int(input())
r=n%7
d=n//7
print(2*d+max(0,r-5),2*d+min(r,2))