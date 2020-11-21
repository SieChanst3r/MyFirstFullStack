<template>
    <div>
        <p>Post Name</p>
        <input v-model="postsName" type="text"/>
        <p>Post Content</p>
        <textarea v-model="postsContent"></textarea>
        <button @click="updatePost()">Submit</button>
    </div>
</template>

<script>
import axios from "axios"

    export default {
        name: "UpdatePost",
        data() {
            return {
                postsContent,
                postsName: "",
                
            };
        },
        props: {
            postsid: {
                type: Number,
                requried: true,
            },
        },
        methods: {
            updatePost: function() {
               axios.request({
                    url: "http://firstwedapp.ml/api/posts",
                    method: "PATCH",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    data: {
                        content: this.postsContent,
                        name: this.postsName,
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