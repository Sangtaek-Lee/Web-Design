const member = {
  name: 'taek',
  age: '29',
  sId: '201314185',
}

const member2 = {
  name: 'sang',
  age: '29',
  sId: '201314185',
}
// 멤버객체를 만드려면 같은 구조를 계속해서 사용해야 한다. 이를 생성장 함수로 대체 할 수 있다.

function Member(name, age, sId){
  this.name = name
  this.age = age
  this.sId = sId
}


const memeber3 = new Member('isaac', 21, 202212345)
memeber3
//>>>>>> Member {name: 'isaac', age: 21, sId: 202212345}

// 1. 생성자 함수는 함수의 이름을 반드시 대문자로 시작해야함
// 2. 생성자 함수를 사용할 때는 앞에 new라는 키워드를 사용함