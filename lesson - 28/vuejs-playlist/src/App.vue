<template>
  <div>
    <keep-alive>
      <component :is="component"></component>
    </keep-alive>
    <button @click="component = 'form-one' ">Show Form One</button>
    <button @click="component = 'form-two'">Show Form Two</button>
  </div>
</template>

<script>
import formOne from './components/formOne.vue';
import formTwo from './components/formTwo.vue';

export default {
  components: {
    "form-one": formOne,
    "form-two": formTwo 
  },
  data () {
    return {
      component: "form-two"
    }
  },
  methods: {
  }
}
</script>

<style scoped>
body{
    margin: 0;
    font-family: "Nunito SemiBold";
}
</style>
