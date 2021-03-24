<template>
  <div class="home-page">
    <h1 class="main-title">{{ i18n.t("views.home.welcome") }}</h1>
    <h2 class="main-subtitle">{{ i18n.t("views.home.private") }}</h2>
    <reg-section
      v-if="hasRole('admin')"
      :title="i18n.t('views.home.admin.title')"
      color="red"
      background="white"
    >
      <in-link :to="{ name: 'AdminUserList' }">
        {{ i18n.t("views.home.admin.manage_users") }}
      </in-link>
    </reg-section>
    <h2 class="section-title flex">
      {{ i18n.t("views.home.articles.title") }}
      <span class="flex-grow-1" />
      <reg-input name="new-article" v-model="newArticle" />
      <reg-button v-if="hasRole('creator')" @click="createArticle">
        {{ i18n.t("views.home.articles.create") }}
      </reg-button>
    </h2>
    <loading v-if="Articles.state.loading" />
    <h3 v-else-if="Articles.state.articles.length <= 0">
      {{ i18n.t("views.home.articles.empty") }}
    </h3>
    <ul v-else>
      <li v-for="article in Articles.state.articles" :key="article.article">
        {{ article.name }}
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
import { useArticle, useArticles } from "@/composition/article";
import Loading from "@/views/main/Loading.vue";
import RegButton from "@/components/forms/Button.vue";
import RegInput from "@/components/forms/Input.vue";

export default defineComponent({
  name: "Home",
  components: { RegInput, RegButton, Loading, RegSection, InLink },
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
  data() {
    return {
      newArticle: "",
    };
  },
  mounted() {
    this.Articles.state.loading = true;
    this.getArticles();
  },
  methods: {
    async getArticles() {
      this.Articles.state.articles =
        (await this.Articles.getFromLang(this.i18n.locale.value)) || [];
      this.Articles.state.loading = false;
    },
    async createArticle() {
      const article = this.Article.create(
        this.i18n.locale.value,
        this.newArticle
      );
      console.log(article);
    },
  },
  watch: {
    "i18n.locale.value"() {
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
    margin-top: 20px;
    font-size: 1.5rem;
  }

  section {
    margin-top: 30px;
  }
}
</style>
