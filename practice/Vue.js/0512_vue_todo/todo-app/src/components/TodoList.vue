<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in tododata" :key="`${idx}`">
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
    props: {
      tododata: Array,
    },
    methods: {
      removeTodo(todo, idx) {
        // console.log('11');
        this.$emit('removeTodo', todo.item, idx)
        
      },
      toggleTodo(idx) {
        this.$emit('toggleTodo', idx)
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