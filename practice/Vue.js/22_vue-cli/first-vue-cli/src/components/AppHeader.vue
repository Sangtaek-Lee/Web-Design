<!-- 파일 이름 : 대문자로 시작, 파스칼 케이스, 한단어가 아닌 두단어 이상 사용 -->
<!---->
<template>
  <header>
    <h1>Header</h1>
    <button @click="sendEvent">send</button>
  </header>
</template>

<script>
export default {
  data: ()=> {
    return {
      headerText: 'text'
    }
  },
  props: {
    propsdata: String,
  },
  methods: {
    sendEvent() {
      this.$emit('update', this.headerText)
    },
  },
}
</script>

<style>

</style>