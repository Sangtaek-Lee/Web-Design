<template>
  <ul>
    <video-list-item v-for="video in videoList" :key="video.id.videoId" :video="video" @select-video="onSelectVideo">
    </video-list-item>
  </ul>
</template>

<script>
import VideoListItem from './VideoListItem.vue'
export default {
  components: {
    VideoListItem,
  },
  props: {
    videoList: Array,
  },
  methods: {
    onSelectVideo(video) {
      console.log(video)
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>