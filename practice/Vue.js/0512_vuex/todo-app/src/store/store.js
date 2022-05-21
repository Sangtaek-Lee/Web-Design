// npm install vuex@3.6.2 --save  //설치
// src
import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

const storage = {
  fetch() {                         // 내부통신 (외부통신은 axious)
    const todos = []
    if(localStorage.length > 0) {
      for (let i = 0; i < localStorage.length; i++) {
        const todoItem = localStorage.getItem(localStorage.key(i))
        todos.push(JSON.parse(todoItem))
      }
    }
    return todos
  }                 
}

export const store = new Vuex.Store({             // export const 로 접근을 가능하게 ( export default 는 더 큰 scope 를 가르킨다. )
  // CODE HERE
  state: {
    headerText: 'My Todo List',
    todos: storage.fetch(),
  },
  mutations: {
    addTodo(state, item) {
      const todoObj = {
        item,
        completed: false,
      }
      localStorage.setItem(item, JSON.stringify(todoObj))
      state.todos.push(todoObj)
    },
    removeTodo(state, payload) {
      localStorage.removeItem(payload.todoItem)
      state.todos.splice(payload.idx, 1)
    },
    clearAll(state) {
      localStorage.clear()
      state.todos = []
    },
    toggleTodo(state, idx) {
      state.todos[idx].completed = !state.todos[idx].completed
      localStorage.removeItem(state.todos[idx].item)
      localStorage.setItem(state.todos[idx].item, JSON.stringify(state.todos[idx]))
    },
  }

})




// // -------------------------------------
// // vue way
// data: {
//   message: 'hello'
// }
// //use
// <p>{{ message }}</p>
// // -------------------------------------
// // vuex way
// state: {
//   message: 'hello'
// }
// //use
// <p>{{ this.$store.state.message }}</p>
// // -------------------------------------


// // getters == computed ---------------------------
// state {
//   myNum: 10
// },
// getters: {
//   getNum(state){            // 기본 인자로 state를 받아야 한다.
//     return state.myNum
//   },
//   doubleNum(state){
//     return state.myNum * 2
//   },
// }
// <p>{{ this.$state.getters.getNum }}</p>
