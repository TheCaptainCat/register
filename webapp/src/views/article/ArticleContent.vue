<template>
  <loading v-if="loading" />
  <div class="content" v-else>
    <content-parser :content="content" :lang="lang" />
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { Article, useArticle } from "@/composition/article";
import Loading from "@/views/main/Loading.vue";
import ContentParser from "@/components/article/ContentParser.vue";

export default defineComponent({
  name: "ArticleContent",
  components: { ContentParser, Loading },
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
  :deep(a) {
    color: blue;
  }
}
</style>
