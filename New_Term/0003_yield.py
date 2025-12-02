L = [1,2,3,4,5,6,7,8]
def all_pairs(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            yield (L[i], L[j])
gen = all_pairs(L)
for x,y in gen:
    print(x,y)


# def simple_generator():
#     yield 1
#     yield 2
#     yield 3

# # Create a generator object
# gen = simple_generator()

# # Retrieve values one by one
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3

# # Using a for loop to iterate over the generator
# for value in simple_generator():
#     print(value)