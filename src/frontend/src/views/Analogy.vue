<template>
  <div>
    <v-container>
      <v-row class="text-center pt-5">
        <v-col class="my-7" cols="6">
          <h1 class="display-2 font-weight-bold mb-3">Analogy game</h1>
        </v-col>
        <v-col cols="3">
          <v-hover v-slot="{ hover }">
            <v-card
              :elevation="hover ? 16 : 2"
              :class="{ 'on-hover': hover }"
              :color="hover ? '#ff9800' : '#8bc34a'"
              class="mx-auto"
              max-width="300"
            >
              <v-card-text class="py-10">
                <p class="text-h3 text--primary">Random</p>
                <div class="text--primary">Choose random words</div>
              </v-card-text>
            </v-card>
          </v-hover>
        </v-col>
        <v-col cols="3">
          <v-hover v-slot="{ hover }">
            <v-card
              :elevation="hover ? 16 : 2"
              :class="{ 'on-hover': hover }"
              :color="hover ? '#ff9800' : '#8bc34a'"
              class="mx-auto"
              max-width="300"
            >
              <v-card-text class="py-10">
                <p class="text-h3 text--primary">User set</p>
                <div class="text--primary">
                  Select words from user validated set
                </div>
              </v-card-text>
            </v-card>
          </v-hover>
        </v-col>
        <v-col cols="12"></v-col>
        <v-col cols="2">
          <v-card
            elevation="8"
            class="mx-auto d-flex align-center justify-center"
            max-width="300"
            height="200"
          >
            <v-form class="d-flex align-center justify-center pa-4">
              <v-text-field height="100" class="text-h4" v-model="wordIs"></v-text-field>
            </v-form>
          </v-card>
        </v-col>
        <v-col cols="1" fill-height class="d-flex align-center justify-center"
          ><h1>is to</h1></v-col
        >
        <v-col cols="2">
          <v-card
            elevation="8"
            class="mx-auto d-flex align-center justify-center pa-4"
            max-width="300"
            height="200"
          >
            <v-form class="d-flex align-center justify-center pa-4">
              <v-text-field height="100" class="text-h4" v-model="wordTo"></v-text-field>
            </v-form>
          </v-card>
        </v-col>
        <v-col cols="1" fill-height class="d-flex align-center justify-center"
          ><h1>as</h1></v-col
        >
        <v-col cols="2">
          <v-card
            elevation="8"
            class="mx-auto d-flex align-center justify-center pa-4"
            max-width="300"
            height="200"
          >
            <v-form class="d-flex align-center justify-center pa-4">
              <v-text-field height="100" class="text-h4" v-model="wordAsIs"></v-text-field>
            </v-form>
          </v-card>
        </v-col>
        <v-col cols="1" fill-height class="d-flex align-center justify-center"
          ><h1>to</h1></v-col
        >
        <v-col cols="3">
          <v-card
            @click="getAnalogy()"
            elevation="8"
            class="mx-auto d-flex align-center justify-center pa-4"
            max-width="300"
            height="200"
          >
            <v-card-text class="d-flex align-center justify-center">
              <p class="text-h2 text--primary">{{wordAsTo.name}}</p>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12 my-8"> </v-col>
        <v-col col="2"></v-col>
        <v-col cols="4">
          <v-hover v-slot="{ hover }">
            <v-card
              :elevation="hover ? 16 : 2"
              :class="{ 'on-hover': hover }"
              :color="hover ? 'green' : 'white'"
              class="mx-auto"
              max-width="300"
            >
              <v-card-text class="py-10">
                <p class="text-h2 text--primary">Valid</p>
              </v-card-text>
            </v-card>
          </v-hover>
        </v-col>
        <v-col cols="4">
          <v-hover v-slot="{ hover }">
            <v-card
              :elevation="hover ? 16 : 2"
              :class="{ 'on-hover': hover }"
              :color="hover ? 'red' : 'white'"
              class="mx-auto"
              max-width="300"
            >
              <v-card-text class="py-10">
                <p class="text-h2 text--primary">Not valid</p>
              </v-card-text>
            </v-card>
          </v-hover>
        </v-col>
        <v-col col="2"></v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import DataService from "../services/dataService";

@Component
export default class Analogy extends Vue {
  wordIs: string = "";
  wordTo: string = "";
  wordAsIs: string = "";
  wordAsTo: string = "";

  async getAnalogy(): Promise<any> {
    console.log("Hello");
    
    const res = await DataService.getAnalogies(this.wordIs, this.wordTo, this.wordAsIs);
    this.wordAsTo = res.data[0];
  }
}
</script>