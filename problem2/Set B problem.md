## Set B problem

using mongoDB and Apache kafka

------------------------------
<br>


### problem 8) 
    producer가 뿌린 data를 consumer가 mongoDB에 저장



<br>

### problem 9)
    producer가 data를 생성하고, consumer는 data가 빠짐없이 잘 왔는지 체크해서 mongoDB에
    저장. 오지 않은 data는 collection에 * 로 표기.
    ++ 지정한 range (0~100)을 넘어서는 data는 저장하지 않고 무시



<br>



### problem 10)
    두 개의 producer를 생성한 후, consumer는 매 초마다 받은 data를 비교.
    ++ mongoDB에 저장하고, plot 그래프로 표현해서 비교
