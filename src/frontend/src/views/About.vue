<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h4>{{ body.title }}</h4>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import Test from "../types/Test";
import TestService from "../services/testService";
// import DataService from "../services/testService";

@Component 
export default class About extends Vue {
  body: Test = {
    userId: -1,
    id: -1,
    completed: false,
    title: ""
  }

  async mounted() {
    this.body = await this.hello()
    console.log(this.body.title);
  }

  async hello(): Promise<Test> {
    const res = await TestService.getHello();
    return res.data
  }
}
</script>