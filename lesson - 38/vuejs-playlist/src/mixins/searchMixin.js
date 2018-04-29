export default {
    computed: {
        filteredBlog () {
            return this.blogs.filter((blog) => {
                return blog.title.match(this.search);
            });
        }
    }
}