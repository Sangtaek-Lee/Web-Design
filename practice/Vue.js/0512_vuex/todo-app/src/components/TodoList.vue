<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in this.$store.state.todos" :key="`${idx}`">
        <span :class="{ completed: todo.completed}" @click="toggleTodo(idx)"> <!-- v-bind class 토글하기 class="{class명: Boolean 값}" 참이면  class on-->
          {{todo.item}}
        </span>          
        <i class="fa-solid fa-trash removeIcon" @click="removeTodo(todo, idx)"></i>
      </li>
    </ul>
  </div>

</template>

<script>
  export default {
    methods: {
      removeTodo(todo, idx) {
        const obj = {
          todoItem: todo.item,
          idx: idx
        }
        this.$store.commit('removeTodo', obj)
      },
      toggleTodo(idx) {
        this.$store.commit('toggleTodo', idx)
      },
    }
  }
</script>

<style>
 li {
   display: flex;
   height: 30px;
 }
 .removeIcon {
   color: black;
   margin-left: auto;
 }
 .completed {
   text-decoration: line-through;
   color: gray;
 }
</style>