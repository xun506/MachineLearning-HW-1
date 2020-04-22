str1_=str(input("请输入一串字符:"))
dict_={}
for i in str1_:
    if i == ' ':
        continue
    dict_[i]=str1_.count(i)
print('字符统计结果:',dict_)