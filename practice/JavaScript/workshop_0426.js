// // 주어진 문자열이 회문인지 판별하는 isPalindrome 함수를 완성하시오.
// function isPalindrome(str) {
//   const myStr = str.replaceAll(' ', '')
//   const myStrReverse = myStr.split('').reverse().join('')
//   return myStr === myStrReverse
// }

// // 출력
// console.log(
//   isPalindrome('a santa at nasa'),  // true
//   isPalindrome('google')  // false
// )


// //-----------------------------------------------------------
// // 1. 해당 코드를 template string 을 활용하여 리팩토링하시오.
// const name = 'Tom'
// console.log(`Hi, my name is ${name}`);
// // 2. 해당 코드를 arrow function 으로 리팩토링하시오.
// // function add(x, y) {
// //   return x + y
// // }

// const add = (x, y) => {
//   return x + y
// }
// console.log(add(2, 3))

// // function square(x) {
// //   return x ** 2
// // }

// const square = (x) => {
//   return x ** 2
// }
// console.log(square(3))


// // 3. 해당 코드의 메서드 introduce 를 function 키워드 없이 리팩토링하시오.
// // const tom = {
// //   name: 'Tom',
// //   introduce: function () {
// //     console.log('Hi, my name is' + this.name)
// //   }
// // }
// const tom = {
//   name: 'Tom',
//   introduce () {
//     console.log('Hi, my name is' + this.name)
//   }
// }
// tom.introduce()


// // 4. 해당 코드를 key, value를 한번씩만 작성하도록 리팩토링하시오.
// const url = 'https://test.com'
// const data = { message: 'Hello World!' }

// const request = { url, data }
// console.log(request.data);



//-------------------------------------------------------------
/* 
1. forEach 메서드를 활용해 모든 사용자들의 이름을 출력하시오.
2. filter 메서드를 활용해 결혼한 사람들만 모아 marriedUsers 상수에 할당하시오.
3. find 메서드를 활용해 이름이 'Tom'인 사람만 tom 상수에 할당하시오.
4. map 메서드를 활용해 모든 사용자에게 isAlive 키를 추가하고 true로 설정한 뒤, newUsers 상수에 할당하시오.
5. reduce 메서드를 활용해 모든 사용자들의 계좌잔액을 totalBalance 상수에 할당하시오.
*/

// const users = [
//   { name: 'Jack', age: 31, isMarried: true, balance: 100, },
//   { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
//   { name: 'Ash', age: 25, isMarried: true, balance: 300, },
//   { name: 'Robert', age: 27, isMarried: false, balance: 400, },
//   { name: 'Tom', age: 35, isMarried: true, balance: 500, },
// ]
// // 1
// users.forEach((elem) => {
//   console.log(elem.name);
// })
// // 2
// const marriedUsers = users.filter((elem) => {
//   return elem.isMarried
// })
// console.log(marriedUsers);
// // 3
// const tom = users.find((elem) => {
//   return elem.name === 'Tom'
// })
// console.log(tom);
// // 4
// const newUsers = users.map((elem) => {
//   return elem.isAlive = true
// })
// console.log(users);
// console.log(newUsers);
// // 5 
// const totalBalance = users.reduce((acc, elem) => {
//   return elem.balance + acc
// }, 0)
// console.log(totalBalance);


// 1-1. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
const savedFile = {
  name: 'profile',
  extension: 'jpg',
  size: 29930
}

const { name, extension, size } = savedFile
console.log(`The file ${name}.${extension} is size of ${size} bytes.`)

// function fileSummary(file) {
//   console.log(`The file ${file.name}.${file.extension} is size of ${file.size} bytes.`)
// }

// fileSummary(savedFile)

// 1-2. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
const data = {
  username: 'myName',
  password: 'myPassword',
  email: 'my@mail.com',
}

// const username = data.username
// const password = data.password
// const email = data.email
const { username, password, email } = data

console.log(username, password, email)


// 2. Rest operator를 활용해 아래 코드를 리팩토링 하시오.
// function addNumbers(a, b, c, d, e) {
//   const numbers = [a, b, c, d, e];
//   return numbers.reduce((sum, number) => {
//     return sum + number
//   }, 0)
// }
function addNumbers(a, ...restArgs) {
  const numbers = [a, ...restArgs];
  return numbers.reduce((sum, number) => {
    return sum + number
  }, 0)
}


console.log(addNumbers(1, 2, 3, 4, 5))


// 3-1. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
const defaultColors = ['red', 'green', 'blue'];
const favoriteColors = ['navy', 'black', 'gold', 'white']
const palette = defaultColors.concat(favoriteColors);
console.log(palette);

// // 3-2. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
const info1 = { name: 'Tom', age: 30 }
const info2 = { isMarried: true, balance: 3000 }
const fullInfo = Object.assign(info1, info2)

console.log(fullInfo)