<template>
  <article v-if="pageState.loading">
    Loading article...
  </article>
  <article v-else>
    <h1>{{ pageState.page.name }}</h1>
    <p>
      Created on {{ pageState.page.created_on }} by
      {{ pageState.page.created_by.username }}
    </p>
    <p>
      Updated on {{ pageState.page.updated_on }} by
      {{ pageState.page.updated_by.username }}
    </p>
    <button @click="fetchContent">Get content</button>
    <hr />
    <article-content
      :version="pageState.page.last_version"
      @add-version="addVersion"
    />
  </article>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import usePage from "@/composition/page/functions";
import ArticleContent from "@/views/article/Content.vue";

export default defineComponent({
  name: "Article",
  components: {
    ArticleContent
  },
  props: {
    language: {
      type: String,
      required: true
    },
    id: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const state = reactive({});
    const { newPageState, getPage, addVersion, fetchContent } = usePage();
    const pageState = newPageState(true);
    const articleId = parseInt(props.id);

    return {
      state,
      articleId,
      pageState,
      getPage,
      addVersion: async (content: string) =>
        await addVersion(pageState, articleId, props.language, content),
      fetchContent: async () => await fetchContent(articleId, props.language)
    };
  },
  async mounted() {
    await this.getPage(this.pageState, this.articleId, this.language);
  }
});
</script>

<style lang="scss" scoped></style>
