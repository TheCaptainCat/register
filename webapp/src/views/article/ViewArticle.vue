<template>
  <loading v-if="loading" />
  <div v-else-if="notFound && availableLanguages.length" class="no-page">
    <h1>{{ i18n.t("views.article.no_page") }}</h1>
    <div class="change-locale">
      {{ i18n.t("views.home.change_locale") }}
      <router-link
        v-for="language in availableLanguages"
        :key="language.lang"
        :to="{
          name: 'ViewArticle',
          params: {
            lang: language.lang,
            article: articleKey,
            name: Article.formatName(language.name),
          },
        }"
      >
        <span
          :class="['flag-icon', `flag-icon-${i18n.flags[language.lang]}`]"
        />
      </router-link>
    </div>
  </div>
  <div v-else-if="notFound" class="flex aic jcc not-found">
    <h1>{{ i18n.t("views.article.not_found") }}</h1>
  </div>
  <div v-else class="a-view">
    <h1 class="a-title">{{ article.name }}</h1>
    <h2 class="a-credits">
      {{
        i18n.t("views.article.created", {
          name: article.created_by.username,
          date: formatDate(article.created_on),
        })
      }}
      |
      {{
        i18n.t("views.article.updated", {
          name: article.updated_by.username,
          date: formatDate(article.updated_on),
        })
      }}
    </h2>
    <div v-if="!hasContent" class="no-page">
      <h1>{{ i18n.t("views.article.no_content") }}</h1>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Article, useArticle, useArticles } from "@/composition/article";
import { useI18n } from "@/plugins/i18n";
import Loading from "@/views/main/Loading.vue";
import { FetchError } from "@/core/requests";

export default defineComponent({
  name: "ViewArticle",
  components: { Loading },
  props: {
    lang: { type: String, required: true },
    articleKey: { type: String, required: true },
  },
  setup() {
    const i18n = useI18n();
    const Article = useArticle();
    const Articles = useArticles();
    return {
      i18n,
      Article,
      Articles,
    };
  },
  data(): ViewArticleData {
    return {
      dateOptions: {
        year: "numeric",
        month: "numeric",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
      },
      loading: true,
      notFound: false,
      availableLanguages: [],
      article: null,
    };
  },
  mounted() {
    this.i18n.changeLocale(this.lang);
    this.fetchArticle();
  },
  computed: {
    hasContent(): boolean {
      if (this.article) {
        return this.article.last_version !== null;
      }
      return false;
    },
  },
  methods: {
    async fetchArticle() {
      this.loading = true;
      try {
        this.article = await this.Article.get(this.lang, this.articleKey);
        this.notFound = false;
        this.loading = false;
      } catch (err) {
        if (err instanceof FetchError && err.code === 404) {
          this.notFound = true;
          try {
            const availableLanguages = await this.Articles.getAvailableLanguages(
              this.articleKey
            );
            this.availableLanguages = Object.keys(availableLanguages).map(
              (lang) => ({
                lang,
                name: availableLanguages[lang],
              })
            );
          } catch (err) {
            this.availableLanguages = [];
          }
          this.loading = false;
        } else {
          throw err;
        }
      }
    },
    formatDate(date: string) {
      return new Intl.DateTimeFormat(this.lang, this.dateOptions).format(
        new Date(date + "Z")
      );
    },
    changeLocale(locale: string, name: string) {
      this.$router.push({
        name: "ViewArticle",
        params: {
          lang: locale,
          article: this.articleKey,
          name: this.Article.formatName(name),
        },
      });
    },
  },
  watch: {
    lang(value: string) {
      this.i18n.changeLocale(value);
      this.fetchArticle();
    },
  },
});

interface ViewArticleData {
  dateOptions: Record<string, string>;
  loading: boolean;
  notFound: boolean;
  availableLanguages: { lang: string; name: string }[];
  article: Article | null;
}
</script>

<style lang="scss" scoped>
.a-view {
  .a-title {
    font-size: 2.5rem;
  }
  .a-credits {
    font-size: 1rem;
    opacity: 0.5;
  }
}
.no-page {
  > h1 {
    margin-top: 20px;
    font-weight: bold;
    font-size: 1.5rem;
  }
  .change-locale {
    font-size: 1.5rem;
    .flag-icon {
      margin-left: 5px;
      cursor: pointer;
    }
  }
}
.not-found {
  margin-top: 50px;
  > h1 {
    font-size: 2.5rem;
  }
}
</style>
