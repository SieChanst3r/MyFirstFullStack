<template>
    <div>
        <p>Post Name</p>
        <input v-model="postsName" type="text"/>
        <p>Post Content</p>
        <textarea v-model="postsContent"></textarea>
        <button @click="createPost()">Submit</button>
    </div>
</template>

<script>
import axios from "axios"

    export default {
        
        data() {
            return {
                postsContent: "",
                postsName: "",
                
            }
        },
        methods: {
            createPost: function() {
                axios.request({
                    url: "http://firstwedapp.ml/api/posts",
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    data: {
                        content: this.postsContent,
                        name: this.postsName
                    }                  
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