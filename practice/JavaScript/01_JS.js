// let a = 0
// while (a < 10) {
//   a+=1
//   console.log(a)
// }

// for (let a=1;a<11;a+=1) {
//   console.log(a)
// }

// for in key 값을 반환
// const fruits = ['apple','banana']

// for (const fruit in fruits) {
//   console.log(fruit);
// }

// for (fruit of fruits) {
//   console.log(fruit);
// }


//함수 선언식
// function add(a, b) {
//   return a + b
// }
// console.log(add(1, 2));


//함수 표현식
// let add = function (a, b) {
//   return a + b 
// }
// console.log(add(1, 2));

// const array = [
//   { height: 10 , width: 30},
//   { height: 20 , width: 90},
//   { height: 54 , width: 32},
// ]

// const areas = []

// array.forEach(element => {
//   console.log(element);
//   areas.push(element['height']*element['width'])
//   console.log(areas);
// });

// const heights = array.map((elem) => {
//   return elem.height
// })
// console.log(heights);

// const myArr = [1,2,3,4,5,6,7,8,9]

// const newArr = myArr.filter((elem)=>{
//   return elem % 2
// })

// console.log(newArr);

// const numbers = [15,25,35,45,55,65,75,85,95]

// const newArr = numbers.filter((elem)=> {
//   return elem >= 50
// })

// console.log(newArr);

// const myArr = [1,2,3,4,5]
// const rlt = myArr.reduce((acc, elem)=>{
//   console.log(acc);
//   return (elem*2) + acc
// }, 0)
// console.log(rlt);

// const myArr = [1,2,3,4,5]
// const rlt = myArr.find((elem) => {
//   return elem > 3
// })
// console.log(rlt);

// const avengers = [
//   { name : 'Tony Stark', age: 45 },
//   { name : 'Steve Rogers', age: 32 },
//   { name : 'Thor', age: 40 },
// ]

// const rlt = avengers.find((elem) => {
//   return elem.age >= 40
// })
// console.log(rlt);

// ------------------------------------
// const myArr = [1,2,3,4,5]
// const rlt = myArr.some((elem) => {
//   console.log(elem);
//   return elem > 3
// })
// console.log(rlt)

//------------------------------

// const myArr = [1,2,3,4,5,[6,7,8]]
// console.log(_.sampleSize(myArr, 2));

// // console.log(_.reverse(myArr));

// const myRange = _.range(1, 12,5)
// console.log(myRange);

// // 깊은 복사 TEST
// const copyArr =_.cloneDeep(myArr)
// const copyArr_1 = myArr
// // 원본 변경
// myArr[5][2] = 9
// console.log(myArr);
// console.log(copyArr);
// console.log(copyArr_1);
