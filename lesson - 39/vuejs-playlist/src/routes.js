import showBlogs from "./components/showBlogs.vue";
import listBlogs from "./components/listBlogs.vue";
import addBlog from "./components/addBlog.vue";

export default [
    {path: "/", component: showBlogs},
    {path: "/add", component: addBlog},
    {path: "/list", component: listBlogs}
]