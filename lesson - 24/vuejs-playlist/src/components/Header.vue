<template>
    <header>
        <h1 @click="changeTitle">{{title}}</h1>
    </header>
</template>

<script>
    export default {
        props: {
            title: {
                type: String
            }
        },
        data() {
            return {
                toggle: true,
                myTitle: this.title
            }
        },
        methods: {
            changeTitle () {
                this.$emit("changeTitle", {title: "Vue Wizards", copyright: "Copyright 2018 panshuai"});
            }
        }
    }
</script>

<style scoped>
    header {
        background: lightgreen;
        padding: 10px;
    }
    
    h1 {
        color: #222;
        text-align: center;
    }
</style>
