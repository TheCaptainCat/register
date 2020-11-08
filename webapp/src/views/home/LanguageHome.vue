<template>
  <h1>{{ language }}</h1>
  <section v-if="pageListState.loading">
    Loading articles...
  </section>
  <section v-else>
    <ul>
      <li v-for="page in pageListState.pages" :key="page.name">
        <router-link
          :to="{
            name: 'Article',
            params: { language: page.language, id: page.article }
          }"
        >
          {{ page.name }}
        </router-link>
      </li>
    </ul>
    <button @click="createArticle('test')">Create article</button>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import usePage from "@/composition/page/functions";

export default defineComponent({
  name: "LanguageHome",
  props: {
    language: {
      type: String,
      required: true
    }
  },
  setup() {
    const { newPageListState, getPagesByLanguage } = usePage();
    const pageListState = newPageListState(true);

    return {
      pageListState,
      getPagesByLanguage
    };
  },
  async mounted() {
    await this.getPagesByLanguage(this.pageListState, this.language);
  }
});
</script>

<style lang="scss" scoped></style>
