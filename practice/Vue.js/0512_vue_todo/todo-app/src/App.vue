<template>
  <div id="app">
    <todo-header></todo-header>
    <todo-input @addTodo="addTodo"></todo-input>
    <todo-list :tododata="todos" @removeTodo="removeTodo" @toggleTodo="toggleTodo"></todo-list>
    <todo-footer @clearAll="clearAll"></todo-footer>
  </div>
</template>

<script>
import TodoHeader from './components/TodoHeader.vue'
import TodoInput from './components/TodoInput.vue'
import TodoList from './components/TodoList.vue'
import TodoFooter from './components/TodoFooter.vue'


export default {
  name: 'App',
  data() {
    return {
      todos: [],
    }
  },
  components: {
    TodoHeader,
    TodoInput,
    TodoList,
    TodoFooter,
  },
  created() {
    if(localStorage.length > 0) {
      for (let i = 0; i < localStorage.length; i++) {
        console.log(localStorage.key(i))  // key 값

        const todoItem = localStorage.getItem(localStorage.key(i))
        this.todos.push(JSON.parse(todoItem))    // value 값
      }
    }
    // console.log('created');
  },
  methods: {
    addTodo(item) {
      const todoObj = {
        item,
        completed: false,
      }
      localStorage.setItem(item, JSON.stringify(todoObj))
      this.todos.push(todoObj)
    },
    removeTodo(todoItem, idx) {
      localStorage.removeItem(todoItem)
      this.todos.splice(idx, 1)
    },
    
    clearAll() {
      localStorage.clear()
      this.todos = []
    },
    toggleTodo(idx) {
      this.todos[idx].completed = !this.todos[idx].completed
      localStorage.removeItem(this.todos[idx].item)
      localStorage.setItem(this.todos[idx].item, JSON.stringify(this.todos[idx]))
    },
  },
}
</script>

<style>
body {
  background-color: white;
  text-align: center;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
