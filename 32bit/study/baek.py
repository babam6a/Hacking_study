def calculate(N) :
    ans = 0
    if N%5 == 0 :
        ans = N/5
    else :
        use = N
        if use %3 == 0:
            use -= 5
            ans += 1
        while use%3 != 0 :
            use -= 5
            ans += 1
            if use %3 == 0:
                ans = ans + (use/3)
                break
            if use<0 :
                if N%3 == 0:
                    ans = N/3
                else :
                    ans = -1
                break
    return ans

Answer = calculate(int(input()))
print(Answer)
