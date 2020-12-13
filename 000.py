num = [0xff,0xff,0xf7,0x83,0xf7,0xbb,0x17,0xbb,0x57,0xbb,0x57,0xb8,0x57,0xbf,0x17,0xbf,0xb7,0xbf,0xb7,0xbf,0x11,0x86,0xb5,0xf7,0xb5,0xf7,0xb4,7,0x87,0xff,0xff,0xff]
map = [0 for i in range(0,1000)]
for i in range(16):
    v2 = num[i]
    # print(i)
    v1 = 1
    map[16 * i + 16 - v1] = v2 & 1
    v2 = v2 >> 1
    v1 += 1
    while v1 and v1 <= 16:
        map[16 * i + 16 - v1] = v2 & 1
        v2 = v2 >> 1
        v1+=1
# print(map)

for i in range(1000):
    i = -i
    if map[i] == 1:
        print(1000 + i)
        break

mapp = map[:255]
print(mapp)
s = 'flag{'+'a'*(59-6)+"}"
# print(len(s))
print(s)
# while 1:
#     v8 = int(input())
#     v7 = int(input())
#     print(v8*16+v7)
#     print(mapp[v8*16+v7])