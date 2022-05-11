<template>
  <div>
    <input type="text" @keypress.enter="inputKeyword" />
  </div>
</template>

<script>
export default {
  methods: {
    inputKeyword(event) {
      this.$emit('input-search', event.target.value)
    },
  },

}
</script>

<style>

</style>