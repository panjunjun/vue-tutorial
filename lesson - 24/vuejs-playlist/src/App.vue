<template>
  <div>
    <app-header :title="title" @changeTitle="updateTitle($event)"></app-header>
    <app-ninjas :ninjas="ninjas"></app-ninjas>
    <app-footer :title="title" :copyright="copyright"></app-footer>
  </div>

</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import Ninjas from './components/Ninjas.vue';

export default {
  components: {
    "app-header": Header,
    "app-footer": Footer,
    "app-ninjas": Ninjas
  },
  data () {
    return {
      ninjas: [
        {name: "Ryu", speciality: "Vue Components", show: false},
        {name: "Crystal", speciality: "HTML Wizardry", show: false},
        {name: "Hitoshi", speciality: "Click Events", show: false},
        {name: "Tango", speciality: "Conditionals", show: false},
        {name: "Kami", speciality: "Webpack", show: false},
        {name: "Yoshi", speciality: "Data Diggin", show: false},
      ],
      title: "Vue Ninjas!",
      copyright: "Copyright 2018 panjunxi"
    }
  },
  methods: {
    updateTitle (updatedObject) {
      this.title = updatedObject.title;
      this.copyright = updatedObject.copyright;
    }
  }
}
</script>

<style scoped>

</style>
