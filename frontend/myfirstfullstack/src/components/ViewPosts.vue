<template>
    <div>
        <h1 @click="getPosts()">GET POSTS</h1>
        <div class="post-container" v-for="post in posts" :key="post[2]">
            <h2> {{ post[1] }} </h2>
            <p> {{ post[0] }} </p>
            <p> {{ post[3] }} </p>
            <update-post :postsid="post[2]"></update-post>
            <delete-post :postsid="post[2]"><delete-post>

        </div>
    </div>
</template>

<script>
import axios from "axios";
import UpdatePost from "./UpdatePost.vue"
import DeletePost from "./DeletePost.vue"

    export default {
        data() {
            return {
                posts: [],
            };
        },
        components: {
            UpdatePost,
            DeletePost,
        },
        methods: {
            getPosts: function() {
                axios.request({
                    url: "http://firstwedapp.ml/api/posts",
                    method: "GET"
                }).then((response) => {
                    console.log(response)
                    this.posts = response.data
                }).catch((error) => {
                    console.log(error)
                })
            }
        },
    };
</script>

<style scoped>

</style>