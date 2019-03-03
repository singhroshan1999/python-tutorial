
def memoize(func):
    memo = {}
    def helper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return helper

@memoize
def cube(n):
    return (n*n*n)

print(cube(234545234523452345234534252354))
print(cube(856785674575634532453215435456))

print(cube(234545234523452345234534252354))
print(cube(856785674575634532453215435456))
