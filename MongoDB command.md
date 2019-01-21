### MongoDB



##### 1) MongoDB 실행

```
C:\Users\예지 > mongo
```



##### 2) Database 목록 보기

```
> show dbs
```



##### 3) 해당 Database 사용

```
> use numtest
```

여기서의 numtest는 **db 이름**이다.



##### 4) Database 내의 모든 document 조회

```
> db.numtest.find()
```



##### 5) 모든 document 조회 값을 예쁘게 나타내기

```
> db.numtest.find().pretty 
```



##### 6) 비교(Comparison) 연산자

| operator | 설명                                                  |
| -------- | ----------------------------------------------------- |
| $eq      | (equals) 주어진 값과 일치하는 값                      |
| $gt      | (greater than) 주어진 값보다 큰 값                    |
| $gte     | (greater than or equals) 주어진 값보다 크거나 같은 값 |
| $lt      | (less than) 주어진 값보다 작은 값                     |
| $lte     | (less than or equals) 주어진 값보다 작거나 같은 값    |
| $ne      | (not equal) 주어진 값과 일치하지 않는 값              |
| $in      | 주어진 배열 안에 속하는 값                            |
| $nin     | 주어진 배열 안에 속하지 않는 값                       |



##### 7) 예제. likes 값이 10보다 크고 30보다 작은 document 조회

```
> db.numtest.find({"likes":{$gt:10, $lt:30}}).pretty()
```

 

##### 8) $where 연산자

```
> db.numtest.find({$where:"this.comments.length == 0"})
```

**$where**연산자를 통해 **javascript expression** 사용 가능



##### 9) $elemMatch 연산자

$elemMatch 연산자는 Embedded Documents 배열을 쿼리할 때 사용.

Embedded document란, **document 안에 배열 형태**로 있는 document를 말함.

**mongodb는 기존 쿼리 Join 대신 Embedded document를 활용할 수 있음**

```
> db.numtest.find({"comments": {$elemMatch:{"name": Charlie}}})
```



Embedded document 배열이 아니라 아래 Document의 "name" 처럼 한개의 Embedded document일 경우에는,

```
 {
    "username": "velopert",
    "name": { "first": "M.J.", "last": "K."},
    "language": ["korean", "english", "chinese"]
  }
```

아래와 같이 쿼리해야 한다.

```
> db.numtest.find({ "name.first": "M.J."})
```





참고: https://velopert.com/479