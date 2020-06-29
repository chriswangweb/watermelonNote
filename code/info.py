import math
print ("小明不知道选择题ABCD哪个选项时的熵 : ", math.log(4,2))
print ("告诉小明C有一半几率是正确提供的信息 : ", math.log(4,2)-(1/6*math.log(6,2)+1/6*math.log(6,2)+1/2*math.log(2,2)+1/6*math.log(6,2)))
print ("小明知道C有一半几率是正确后的熵 : ", 1/6*math.log(6,2)+1/6*math.log(6,2)+1/2*math.log(2,2)+1/6*math.log(6,2))