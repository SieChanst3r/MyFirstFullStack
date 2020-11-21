<template>
    <div>
    <button @click="deletePost()">Delete</button>

    </div>
</template>

<script>
import axios from "axios"

    export default {
        name: "DeletePost",
        props:{
            postsid: {
                type: Number,
                requried: true,
            },
        },
        methods: {
            deletePost: function() {
               axios.request({
                    url: "http://firstwedapp.ml/api/posts",
                    method: "Delete",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    data: {
                        id: this.postsid
                    },                      
               }).then((response) => {
                   console.log(response)
               }).catch((error) => {
                   console.log(error)
               })
            }
        },
    };
</script>

<style scoped>

</style>