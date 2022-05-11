<template>
<!--main.js 에서 정의해 줬다-->
  <div> <!--최상위 root는 1개만 존재해야 한다.--> <!---->
    <div>{{ context }}</div>
    <app-header :propsdata="context" @update="updateEvent"></app-header>
  </div>
</template>

<script>
  import AppHeader from './components/AppHeader.vue'
  export default {
    data: () => {
      return {
        context: 'hello vue!'
      }
    },
    components: {
      AppHeader,
    },
    methods: {
      updateEvent(data) {
        this.context = data
      },
    }
  }
</script>

<style>

</style>