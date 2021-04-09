<template>
  <loading v-if="loading" />
  <div v-else class="create-article">
    <h1 v-if="!articles">{{ i18n.t("views.create_article.title") }}</h1>
    <h1 v-else>{{ i18n.t("views.create_article.title_link") }}</h1>
    <ul v-if="articles" class="linked-article">
      <li v-for="a in Object.keys(articles)" :key="a">
        <span :class="['flag-icon', `flag-icon-${i18n.flags[a]}`]" />
        {{ articles[a] }}
      </li>
    </ul>
    <language-selector
      class="lang-selector"
      :prefix="i18n.t('views.home.change_locale')"
      :languages="availableLanguages"
      :size="1"
      @updated:locale="changeLocale"
    />
    <reg-form class="art-name-input" inline @submit="createArticle">
      <reg-input
        class="flex-grow-1"
        name="article-name"
        :placeholder="i18n.t('views.create_article.placeholder')"
        v-model="fields.article.value"
        :error="fields.article.error"
      />
      <reg-button :loading="creating" @click="createArticle">
        {{ i18n.t("views.create_article.btn") }}
      </reg-button>
    </reg-form>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import { useField, useForm } from "vee-validate";
import * as yup from "yup";
import { useI18n } from "@/plugins/i18n";
import LanguageSelector from "@/components/LanguageSelector.vue";
import RegInput from "@/components/forms/Input.vue";
import RegButton from "@/components/forms/Button.vue";
import RegForm from "@/components/forms/Form.vue";
import { useArticle, useArticles } from "@/composition/article";
import Loading from "@/views/main/Loading.vue";
import { RouteLocationRaw } from "vue-router";

export default defineComponent({
  name: "CreateArticle",
  components: { Loading, RegForm, RegButton, RegInput, LanguageSelector },
  props: {
    lang: { type: String, required: true },
    linkTo: { type: String },
  },
  setup() {
    const i18n = useI18n();
    const { form, fields } = createForm();
    const Article = useArticle();
    const Articles = useArticles();
    return {
      i18n,
      form,
      fields,
      Article,
      Articles,
    };
  },
  data(): {
    articles: Record<string, string> | null;
    loading: boolean;
    creating: boolean;
  } {
    return {
      articles: null,
      loading: true,
      creating: false,
    };
  },
  async mounted() {
    this.i18n.changeLocale(this.lang);
    await this.loadLinkedArticles();
    this.loading = false;
  },
  computed: {
    availableLanguages(): string[] {
      const lang = Object.keys(this.i18n.messages);
      return lang.filter(
        (l) => l !== this.lang && (!this.articles || !(l in this.articles))
      );
    },
  },
  methods: {
    changeLocale(locale: string) {
      const options: RouteLocationRaw = {
        name: "CreateArticle",
        params: { lang: locale },
      };
      if (this.linkTo) options.query = { linkTo: this.linkTo };
      this.$router.push(options);
    },
    async createArticle() {
      this.creating = true;
      if ((await this.form.validate()).valid) {
        const article = await this.Article.create(
          this.lang,
          this.fields.article.value,
          this.linkTo
        );
        await this.$router.push({
          name: "ViewArticle",
          params: {
            lang: this.lang,
            key: article.article.key,
            name: this.Article.formatName(article.name),
          },
          query: {
            edit: "1",
          },
        });
      }
      this.creating = false;
    },
    async loadLinkedArticles() {
      if (!this.linkTo) return;
      this.articles = await this.Articles.getAvailableLanguages(this.linkTo);
    },
  },
  watch: {
    lang(value: string) {
      this.i18n.changeLocale(value);
    },
  },
});

const createForm = () => {
  const form = useForm({
    validationSchema: yup.object({
      article: yup.string().required(),
    }),
  });
  const { value: article, errorMessage: articleError } = useField<string>(
    "article"
  );
  return {
    form,
    fields: reactive({
      article: {
        value: article,
        error: articleError,
      },
    }),
  };
};
</script>

<style lang="scss" scoped>
.create-article {
  .linked-article {
    list-style: none;
    padding: 0;
    .flag-icon {
      margin-right: 10px;
    }
  }
  .section-title {
    margin-top: 20px;
    font-size: 1.5rem;
  }
  .flag-icon {
    margin-left: 5px;
    cursor: pointer;
  }
  .art-name-input {
    margin-top: 15px;
  }
}
</style>
