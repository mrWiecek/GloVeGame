<template>
  <v-app
    id="main"
    :style="{ background: $vuetify.theme.themes[theme].background }"
  >
    <v-app-bar app color="bar" dark dense>
      <div class="d-flex align-center">
        <v-img
          contain
          alt="GloVe Game Logo"
          class="shrink mr-2"
          src="./assets/logo.png"
          transition="scale-transition"
          width="40"
        />
      </div>
      <v-toolbar-items v-for="item in appBarItems" :key="item.to">
        <v-btn
          :to=item.to
          text
          class="hidden-xs-only"
          exact
        >
          <span class="mr-2">{{ item.name }}</span>
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>

    <v-footer color="bar">
      <v-spacer />
      <div>
        Icons made by
        <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons"
          >Smashicons</a
        >
        from
        <a href="https://www.flaticon.com/" title="Flaticon"
          >www.flaticon.com</a
        >
      </div>
    </v-footer>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class App extends Vue {
  appBarItems = [
    {to: '/', name: "Home"},
    {to: 'Analogy', name: "Analogy"},
    {to: 'Closest', name: "Closest"},
  ]

  get theme(): string {
    return this.$vuetify.theme.dark ? "dark" : "light";
  }
}
</script>
