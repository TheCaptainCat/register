<template>
  <loading v-if="loading" />
  <div v-else-if="notFound && availableLanguagesKeys.length" class="no-page">
    <h1>{{ i18n.t("views.article.no_page") }}</h1>
    <language-selector
      :prefix="i18n.t('views.home.change_locale')"
      :languages="availableLanguagesKeys"
      @updated:locale="
        (locale) => reloadPage(locale, availableLanguages[locale], edit)
      "
    />
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
    <template v-if="edit">
      <div class="a-edit-controls flex">
        <reg-button @click="toggleEditMode">
          {{ i18n.t("global.cancel") }}
        </reg-button>
        <div class="flex-grow-1" />
        <reg-button type="success" @click="saveArticleEdits">
          {{ i18n.t("global.save") }}
        </reg-button>
      </div>
      <reg-text-area
        class="a-content-input"
        name="content"
        v-model="content"
        :dimensions="{ min: 10 }"
      />
    </template>
    <template v-else>
      <language-selector
        class="select-lang"
        v-if="availableLanguagesKeys.length"
        :prefix="i18n.t('views.home.change_locale')"
        :languages="availableLanguagesKeys"
        :size="1"
        @updated:locale="
          (locale) => reloadPage(locale, availableLanguages[locale], edit)
        "
      />
      <reg-section
        v-if="!edit && hasRole('creator')"
        :title="i18n.t('views.article.editor')"
        :background="'white'"
      >
        <reg-button icon="pencil" @click="toggleEditMode">
          {{ i18n.t("views.article.edit") }}
        </reg-button>
        <div class="flex-grow-1" />
        <language-selector
          v-if="translatablePages.length"
          :prefix="i18n.t('views.article.translate')"
          :languages="translatablePages"
          :size="1"
          @updated:locale="translateArticle"
        />
      </reg-section>
      <div v-if="!hasContent" class="no-page">
        <h1>{{ i18n.t("views.article.no_content") }}</h1>
      </div>
      <article-content
        v-else
        class="a-content"
        :lang="lang"
        :article="article"
      />
    </template>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { RouteLocationRaw } from "vue-router";
import { Article, useArticle, useArticles } from "@/composition/article";
import { useI18n } from "@/plugins/i18n";
import { FetchError } from "@/core/requests";
import { useUser } from "@/composition/user";
import RegButton from "@/components/forms/Button.vue";
import LanguageSelector from "@/components/LanguageSelector.vue";
import RegSection from "@/components/containers/Section.vue";
import Loading from "@/views/main/Loading.vue";
import RegTextArea from "@/components/forms/TextArea.vue";
import ArticleContent from "@/views/article/ArticleContent.vue";

export default defineComponent({
  name: "ViewArticle",
  components: {
    ArticleContent,
    RegTextArea,
    RegSection,
    LanguageSelector,
    RegButton,
    Loading,
  },
  props: {
    lang: { type: String, required: true },
    articleKey: { type: String, required: true },
    edit: { type: Boolean, default: false },
  },
  setup() {
    const i18n = useI18n();
    const Article = useArticle();
    const Articles = useArticles();
    const { hasRole } = useUser();
    return {
      i18n,
      Article,
      Articles,
      hasRole,
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
      availableLanguages: {},
      article: null,
      content: "",
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
    availableLanguagesKeys(): string[] {
      return Object.keys(this.availableLanguages);
    },
    translatablePages(): string[] {
      const pages = [];
      for (const lang in this.i18n.messages) {
        if (lang !== this.lang && !this.availableLanguagesKeys.includes(lang))
          pages.push(lang);
      }
      return pages;
    },
  },
  methods: {
    async fetchArticle() {
      this.loading = true;
      try {
        this.article = await this.Article.get(this.lang, this.articleKey);
        let availableLanguages: Record<string, string> = {};
        for (const lang in this.article.article.languages) {
          if (lang !== this.lang)
            availableLanguages[lang] = this.article.article.languages[lang];
        }
        this.availableLanguages = availableLanguages;
        if (this.article.last_version)
          this.content = this.article.last_version.content;
        this.notFound = false;
        this.loading = false;
      } catch (err) {
        if (err instanceof FetchError && err.code === 404) {
          this.notFound = true;
          try {
            this.availableLanguages = await this.Articles.getAvailableLanguages(
              this.articleKey
            );
          } catch (err) {
            this.availableLanguages = {};
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
    async toggleEditMode() {
      if (!this.article) return;
      if (this.article.last_version)
        this.content = this.article.last_version.content;
      await this.reloadPage(this.lang, this.article.name, !this.edit);
    },
    async reloadPage(locale: string, name: string, edit: boolean) {
      const options: RouteLocationRaw = {
        name: "ViewArticle",
        params: {
          lang: locale,
          article: this.articleKey,
          name: this.Article.formatName(name),
        },
      };
      if (edit) options.query = { edit: "1" };
      await this.$router.push(options);
    },
    async translateArticle(lang: string) {
      if (!this.article) return;
      await this.$router.push({
        name: "CreateArticle",
        params: {
          lang,
        },
        query: {
          linkTo: this.article.article.key,
        },
      });
    },
    async saveArticleEdits() {
      if (this.content.length <= 0 || !this.article) return;
      this.article = await this.Article.update(
        this.lang,
        this.article,
        this.content
      );
      await this.toggleEditMode();
    },
  },
  watch: {
    lang(value: string) {
      this.i18n.changeLocale(value);
      this.fetchArticle();
    },
    articleKey() {
      this.fetchArticle();
    },
  },
});

interface ViewArticleData {
  dateOptions: Record<string, string>;
  loading: boolean;
  notFound: boolean;
  availableLanguages: Record<string, string>;
  article: Article | null;
  content: string;
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
  .select-lang {
    margin-top: 10px;
  }
  .a-edit-controls {
    margin-top: 20px;
  }
  .a-content {
    margin-top: 20px;
  }
  .a-content-input {
    margin-top: 10px;
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
