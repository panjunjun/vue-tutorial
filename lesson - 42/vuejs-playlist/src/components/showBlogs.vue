<template>
  <div id="show-blogs">
    <h1>All Blog Articles</h1>
    <input type="text" placeholder="search block" v-model="search"/>
    <div class="single-blog" v-for="(blog, index) in filteredBlog" :key="index">
        <router-link :to="'/blog/' + blog.id">
          <h2 v-rainbow>{{blog.title | toUpperCase}}</h2>
        </router-link>
        <article>{{blog.body | snippet}}</article>
    </div>
  </div>
</template>

<script>
import searchMixin from "../mixins/searchMixin";

export default {
  data () {
    return {
      blogs: [],
      search: ""
    }
  },
  methods: {

  },
  computed: {

  },
  created () {
    this.$http.get("https://jsonplaceholder.typicode.com/posts").then(
      function(data) {
        this.blogs = data.body.slice(0,10);
      }
    )
  },
  filters: {
    toUpperCase (value) {
      return value.toUpperCase();
    }
  },
  directives: {
    rainbow: {
      bind(el, binding, vnode){
        el.style.color = "#" + Math.random().toString().slice(2, 8);
      }
    }
  },
  mixins: [searchMixin]
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
