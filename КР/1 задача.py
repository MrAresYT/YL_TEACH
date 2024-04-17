from sys import stdin


out = []

for st in stdin.readlines():
    st = st.split()
    for i in st:
        if st.count(i) > 1 and i not in out:
            out.append(i)
            print(i)
