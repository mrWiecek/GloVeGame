<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4" cols="12">
        <h1 class="display-2 font-weight-bold mb-3">Welcome to GloVe Game</h1>
        <p class="subheading font-weight-regular">
          It's a simple game based on the GloVe word vectors pre trained model.
        </p>
        <h2>Please select one of the options below:</h2>
      </v-col>
      <v-col cols="3"></v-col>
      <v-col v-for="card in menuCards" :key="card.title" cols="3">
        <v-hover  v-slot="{ hover }">
          <v-card
            :elevation="hover ? 16 : 2"
            :class="{ 'on-hover': hover }"
            :color="hover ? '#ff9800' : '#8bc34a'"
            :to=card.to
            class="mx-auto"
            max-width="300"
            height="300"  
          >
            <v-card-text class="py-10">
              <p class="text-h3 text--primary">{{ card.title }}</p>
              <div class="text--primary">
                {{ card.description }}
              </div>
            </v-card-text>
          </v-card>
        </v-hover>
      </v-col>
      <v-col cols="3"></v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class MainManu extends Vue {
  menuCards = [
    { title: "Analogy", to: "Analogy", description: "Game where you need to guess closest analogy." },
    { title: "Closest", to: "Closest", description: "Game where you need to guess closest word." },
  ];
}
</script>
