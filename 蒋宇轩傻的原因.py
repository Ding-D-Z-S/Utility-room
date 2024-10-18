#定义一个叫jyx_sb的函数
def jyx_sb(zmsd,wsms):      #怎么傻的 为什么傻
    """返回sb的原因"""
    a=f"{zmsd}，{wsms}"
    return a
#永久循环组
active = True
while active:
    print("\n输入off将会停止循环！")
    a=input("是否停止循环（on/off）:")

    if a == 'on':
        active = True
        active=True
        zmsd = input("请说出他为什么是sb:")
        print("**********************")
        wsms = input("为什么sb:")
        b = jyx_sb(zmsd,wsms)
        print(f"\n蒋宇轩傻逼的原因是：{b}")
        

    elif a == 'off':
        active = False

    else: 
     print("----------------------")
     print("撒比吧！让你输入(on/off)")
     print("----------------------")
