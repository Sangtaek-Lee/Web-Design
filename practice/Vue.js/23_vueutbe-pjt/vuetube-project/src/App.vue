<template>
  <div id="app">
    <h1>My First Vuetube Project</h1>
    <header>
      <search-bar @input-search="inputKeyword"></search-bar>
    </header>
    <section>
      <video-detail :video="selecteVideo"></video-detail>
      <video-list :videoList="videoList" @select-video="onVideoSelect"></video-list>
    </section>
    <section>
      
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'
require('dotenv').config()

const API_KEY = ''
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: () => {
    return {
      keyword: '',
      videoList: [],
      selecteVideo: null,
    }
  },
  methods: {
    inputKeyword(keyword) {
      this.keyword = keyword
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          q: keyword,
          type: 'video',
          part: 'snippet',
        },
      })
      .then( (res) => {
        this.videoList = res.data.items
        // console.log(res);
      })
      .catch(err => {
        console.log(err);
      })
    },
    onVideoSelect(video) {
      this.selecteVideo = video
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
