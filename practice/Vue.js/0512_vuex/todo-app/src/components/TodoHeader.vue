<template>
  <h1 class="shadow">{{ this.$store.state.headerText }}</h1>
</template>

<script>
export default {

}
</script>

<style scoped>
  h1 {
    color: blanchedalmond;
    font-weight: 900;
    margin: 2rem 0 1.5rem;
  }
  .shadow {
    box-shadow: 5px 10px 5px rgba(0, 0, 0, 0.5);
  }
</style>