"""11) джентльмен пригласил даму в гости, но вместо кода цифрового замка своего подъезда отправил
ей такое сообщение: «В последовательности 52186 все четные цифры нужно разделить на 2, а из
нечетных вычесть 1. Затем удалить из полученной последовательности первую и последнюю
цифры». Определите код цифрового замка.
1) 104
2) 107
3) 218
4) 401"""
ans_d = {
    "104": 1,
    "107": 2,
    "218": 3,
    "401": 4,
}
sequence = "52186"
ans = ""
for i in sequence:
    if int(i) % 2 == 0:
        ans += str(int(i) // 2)
    else:
        ans += str(int(i) - 1)
print(ans_d[ans[1:-1]])
