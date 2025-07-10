'''
In addition to the ways described in the course material, the number of balanced parenthesis sequences of length n can be counted efficiently using the following formula:
$$\frac{1}{n/2+1}{n \choose n/2},$$
where n is assumed to be even. Here {a \choose b} is a binomial coefficient that can be computed using the formula
$$\frac{a!}{b!(a-b)!}.$$
For example, when n=6, the formula produces the following result
$$\frac{1}{6/2+1}{6 \choose 6/2}=\frac{20}{4}=5.$$
In a file formula.py, implement the function count_sequences that returns the number of balanced parenthesis sequences.
The function should be efficient even if n is large.
'''

def count_sequences(n):
    pass

if __name__ == "__main__":
    print(count_sequences(1)) # 0
    print(count_sequences(2)) # 1
    print(count_sequences(3)) # 0
    print(count_sequences(4)) # 2
    print(count_sequences(5)) # 0
    print(count_sequences(6)) # 5

    print(count_sequences(42)) # 24466267020
    print(count_sequences(1000)) # 539497486917039060909410566119711128734834348196703167679426896420410037336371644508208550747509720888947317534973145917768881736628103627844100238921194561723883202123256952806711505149177419849031086149939116975191706558395784192643914160118616272189452807591091542120727401415762287153293056320