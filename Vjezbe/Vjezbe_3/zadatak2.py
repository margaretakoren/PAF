#Napišite funkciju koja uzima broj iteracija N te N puta zbraja 1/3 pa zatim N puta oduzima 1/3 broju 5. Ispišite konačni rezultat za 200, 2000 i 20000 iteracija. Objasnite rezultat koji ste dobili.

def calculate_result(N):
    result = 0
    for _ in range(N):
        result += 1/3
    for _ in range(N):
        result -= 1/3
    result -= 5
    return result

iterations = [200, 2000, 20000]
for N in iterations:
    final_result = calculate_result(N)
    print(f"Za {N} iteracija, konačni rezultat je: {final_result}")
