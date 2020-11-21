<template>
  <div id="app">
    <create-post></create-post>
    <view-posts></view-posts>

  </div>
</template>

<script>
import CreatePost from './components/CreatePost.vue'
import ViewPosts from "./components/ViewPosts.vue"


export default {
  name: 'App',
  components: {
    ViewPosts,
    CreatePost,

  }
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
