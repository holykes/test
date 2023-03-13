# # #### 비트 반전 구현 ####
# # led=0b1111
# # leds=bin(0b1111)

# # print('원래상태', end='\t')
# # for i in leds[2:]:
# #     if i=='1':
# #         print('💡',end='')
# #     else:
# #         print('⬛',end='')
# # print()
# # # leds 비트 반전(1101->0010)
# # print('반전상태', end='\t')
# # x=f'{led ^ 0b1111:04b}'
# # for i in x:
# #     if i=='1':
# #         print('💡',end='')
# #     else:
# #         print('⬛',end='')


# #### 비트 반전 구현 v2 ####
# num=int(input('숫자: '))

# led=num
# leds=bin(num)
# print('원래상태', end='\t')
# if led<8:
#     print('⬛',end='')

# for i in leds[2:]:
#     if i=='1':
#         print('💡',end='')
#     else:
#         print('⬛',end='')
# print()
# # leds 비트 반전(1101->0010)
# print('반전상태', end='\t')
# x=f'{led ^ 0b1111:04b}'
# for i in x:
#     if i=='1':
#         print('💡',end='')
#     else:
#         print('⬛',end='')

num=int(input('10진수 입력: '))
print(bin(num))
print(oct(num))
print(hex(num))

