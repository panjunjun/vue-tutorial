<template>
  <div id="single-blog">
      <h1>{{blog.title}}</h1>
      <article>{{blog.content}}</article>
      <p>Author: {{blog.author}}</p>
      <ul>
          <li v-for="(category, index) in categoryDisplay" :key=index>{{category}}</li>
      </ul>
  </div>
</template>

<script>
export default {
    data () {
        return {
            id: this.$route.params.id,
            blog: {},
            catetory: []
        }
    },
    created () {
        this.$http.get("http://localhost:8000/blog/?id=" + this.id).then(function(data){
            this.blog = data.body;
        })
    },
    computed: {
        categoryDisplay () {
            return (this.blog.category || "").split(",");
        }
    }
}
</script>

<style scoped>
#single-blog {
    max-width: 960px;
    margin: 0 auto;
    padding: 20px;
    background: #eee;
    border: 1px dotted #aaa;
}
</style>
