<template>
  <h1>Welcome to the Register!</h1>
  <p>Select a community:</p>
  <div v-if="languageState.loading">Loading languages, please wait...</div>
  <div v-else-if="!languageState.languages.length">No communities found!</div>
  <ul v-else>
    <li v-for="language in languageState.languages" :key="language.name">
      <router-link
        :to="{ name: 'LanguageHome', params: { language: language.name } }"
      >
        {{ language.name }}
      </router-link>
    </li>
  </ul>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import {
  newLanguageState,
  getLanguages,
} from "@/composition/language/functions";

export default defineComponent({
  name: "Home",
  setup() {
    const state = reactive({});
    const languageState = newLanguageState();

    return {
      state,
      languageState,
      getLanguages,
    };
  },
  async mounted() {
    await this.getLanguages(this.languageState);
  },
});
</script>

<style lang="scss" scoped></style>
