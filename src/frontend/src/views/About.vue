<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h4>{{ body.userId }}</h4>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import Test from "@/types/Test";
import TodoService from "@/services/todoService";
// import DataService from "@/services/testService";

@Component
export default class About extends Vue {
  body = {};

  async mounted() {
    this.body = await this.hello()
  }

  async hello(): Promise<Test> {
    const res = await TodoService.getHello();
    return res.data
  }
}
</script>