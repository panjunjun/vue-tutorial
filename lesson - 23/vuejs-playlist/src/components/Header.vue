<template>
    <header>
        <h1 @click="changeTitle">{{myTitle}}</h1>
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
                if (this.toggle) {
                    this.myTitle = "Vue Wizards"
                }
                else {
                    this.myTitle = this.title
                }
                this.toggle = !this.toggle
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
