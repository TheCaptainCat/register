<template>
  <loading v-if="loading" />
  <div class="content" v-else v-html="content" />
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { Article, useArticle } from "@/composition/article";
import Loading from "@/views/main/Loading.vue";

export default defineComponent({
  name: "ArticleContent",
  components: { Loading },
  props: {
    lang: { type: String, required: true },
    article: { type: Object as PropType<Article>, required: true },
  },
  setup() {
    const Article = useArticle();
    return {
      Article,
    };
  },
  async mounted() {
    await this.fetchContent();
  },
  data(): { loading: boolean; content: string | null } {
    return {
      loading: true,
      content: null,
    };
  },
  methods: {
    async fetchContent() {
      this.loading = true;
      this.content = await this.Article.getContent(this.lang, this.article);
      this.loading = false;
    },
  },
});
</script>

<style lang="scss" scoped>
.content {
  :deep(h1) {
    font-size: 2rem;
  }
}
</style>
