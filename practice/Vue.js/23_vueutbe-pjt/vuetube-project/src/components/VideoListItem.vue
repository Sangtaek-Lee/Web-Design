<template>
  <li @click="selectVideo">
    <img :src="video.snippet.thumbnails.default.url" alt="thumbnail">
    {{ video.snippet.title }}
  </li>
</template>

<script>
export default {
  props: {
    video: Object,
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.video)
    }
  }
}
</script>

<style>

</style>