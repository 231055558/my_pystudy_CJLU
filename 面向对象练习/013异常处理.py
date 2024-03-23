# raise BaseException("haha")#自定义异常
class MyErr(BaseException):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    raise MyErr("不知道怎么错了")
except MyErr as e:
    print(e)
    raise MyErr("就这样了")