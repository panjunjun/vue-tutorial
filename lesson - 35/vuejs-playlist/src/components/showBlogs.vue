<template>
  <div id="show-blogs">
    <h1>All Blog Articles</h1>
    <div class="single-blog" v-for="(blog, index) in blogs" :key="index">
        <h2>{{blog.title | to-uppercase}}</h2>
        <article>{{blog.body | snippet}}</article>
    </div>
  </div>
</template>

<script>
 
export default {
  data () {
    return {
      blogs: []
    }
  },
  methods: {

  },
  created () {
    this.$http.get("https://jsonplaceholder.typicode.com/posts").then(
      function(data) {
        this.blogs = data.body.slice(0,10);
      }
    )
  }
}
</script>

<style scoped>
#show-blogs {
    max-width: 800px;
    margin: 0 auto;
}
.single-blog {
    padding: 20px;
    margin: 20px 0;
    box-sizing: border-box;
    background: #eee;
}
</style>
