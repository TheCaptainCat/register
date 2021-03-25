<template>
  <div class="home-page">
    <h1 class="main-title flex">{{ i18n.t("views.home.welcome") }}</h1>
    <h2 class="main-subtitle">{{ i18n.t("views.home.private") }}</h2>
    <reg-section
      v-if="hasRole('admin')"
      :title="i18n.t('views.home.admin.title')"
      color="red"
      :background="'white'"
    >
      <in-link :to="{ name: 'AdminUserList' }">
        {{ i18n.t("views.home.admin.manage_users") }}
      </in-link>
    </reg-section>
    <language-selector
      class="lang-selector"
      :prefix="i18n.t('views.home.change_locale')"
      :languages="availableLanguages"
      :size="1"
      @updated:locale="changeLocale"
    />
    <h2 class="section-title flex">
      {{ i18n.t("views.home.articles.title") }}
      <span class="flex-grow-1" />
      <router-link :to="{ name: 'CreateArticle', params: { lang } }">
        <reg-button v-if="hasRole('creator')">
          {{ i18n.t("views.home.articles.create") }}
        </reg-button>
      </router-link>
    </h2>
    <loading v-if="Articles.state.loading" />
    <h3 v-else-if="Articles.state.articles.length <= 0">
      {{ i18n.t("views.home.articles.empty") }}
    </h3>
    <ul v-else>
      <li v-for="article in sortedArticles" :key="article.article">
        <in-link
          :to="{
            name: 'ViewArticle',
            params: {
              lang,
              key: article.article,
              name: Article.formatName(article.name),
            },
          }"
        >
          {{ article.name }}
        </in-link>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useI18n } from "@/plugins/i18n";
import { InLink } from "@/components";
import RegSection from "@/components/containers/Section.vue";
import { useUser } from "@/composition/user";
import { PartialArticle, useArticle, useArticles } from "@/composition/article";
import Loading from "@/views/main/Loading.vue";
import RegButton from "@/components/forms/Button.vue";
import LanguageSelector from "@/components/LanguageSelector.vue";

export default defineComponent({
  name: "ArticleHome",
  components: { LanguageSelector, RegButton, Loading, RegSection, InLink },
  props: {
    lang: { type: String, required: true },
  },
  setup() {
    const i18n = useI18n();
    const { hasRole } = useUser();
    return {
      i18n,
      hasRole,
      Article: useArticle(),
      Articles: useArticles(),
    };
  },
  mounted() {
    this.i18n.changeLocale(this.lang);
    this.Articles.state.loading = true;
    this.getArticles();
  },
  computed: {
    sortedArticles(): PartialArticle[] {
      const articles = this.Articles.state.articles;
      return articles.sort((a: PartialArticle, b: PartialArticle) =>
        a.name.toLowerCase() > b.name.toLowerCase() ? 1 : -1
      );
    },
    availableLanguages(): string[] {
      const lang = Object.keys(this.i18n.messages);
      return lang.filter((l) => l !== this.lang);
    },
  },
  methods: {
    async getArticles() {
      this.Articles.state.articles = await this.Articles.getFromLang(this.lang);
      this.Articles.state.loading = false;
    },
    changeLocale(locale: string) {
      this.$router.push({ name: "ArticleHome", params: { lang: locale } });
    },
  },
  watch: {
    lang(value: string) {
      this.i18n.changeLocale(value);
      this.Articles.state.loading = true;
      this.getArticles();
    },
  },
});
</script>

<style lang="scss" scoped>
@import "../../styles/variables";

.home-page {
  .main-title {
    font-size: 1.75rem;
  }
  .main-subtitle {
    font-size: 1.25rem;
    opacity: 0.75;
  }
  .section-title {
    margin-top: 15px;
    font-size: 1.5rem;
  }
  .flag-icon {
    margin-left: 5px;
    cursor: pointer;
  }
  .language-selector {
    margin-top: 15px;
  }
  section {
    margin-top: 30px;
  }
}
</style>
