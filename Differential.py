degree = ["", "", "²", "³", "⁴"]


def diff(A, output=True):
    result = [A[i]*(len(A)-i-1) for i in range(len(A)-1)]
    if output:
        out = ""
        for i in range(len(result)):
            out += f"{['+',''][result[i]<0 or i==0]}{result[i]}"
            if i != len(result)-1:
                out += f"x{degree[len(result)-i-1]}"
        print(out)
    return result


diff([2, -3, -12, 0])
