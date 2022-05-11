<template>
  <div v-if="video">
    <iframe :src="videoURI" frameborder="0"></iframe>r
  </div>
</template>

<script>
export default {
  props: {
    video: Object
  },
  computed: {
    videoURI() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
  },
}

</script>

<style>

</style>