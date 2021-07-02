<template>
  <Menu />
</template>

<script lang="ts">
  import Vue from 'vue'
  import Menu from '../components/Menu.vue'

  export default Vue.extend({
    name: 'Home',

    components: {
      Menu,
    },
  })
</script>
