def reverse(S,start,stop):
    if start <stop-1:
        S[start],S[stop]=S[stop-1],S[start]
        reverse(S,start+1,stop-1)
        