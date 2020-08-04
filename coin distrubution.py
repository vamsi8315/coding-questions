def solution(number):
   no5=(number-4)//5
   if((number-5*no5)%2==0):
       num_of_one=2
   else:
        num_of_one=1
   no_of_two=(number-5*no5-num_of_one)//2
   
  num=int(input())
  solution(number)
