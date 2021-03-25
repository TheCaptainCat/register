<template>
  <div class="create-article">
    <h1>{{ i18n.t("views.create_article.title") }}</h1>
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
      <reg-button :loading="state.loading" @click="createArticle">
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
import { useArticle } from "@/composition/article";

export default defineComponent({
  name: "CreateArticle",
  components: { RegForm, RegButton, RegInput, LanguageSelector },
  props: {
    lang: { type: String, required: true },
  },
  setup() {
    const i18n = useI18n();
    const state = reactive({
      loading: false,
    });
    const { form, fields } = createForm();
    const Article = useArticle();
    return {
      i18n,
      state,
      form,
      fields,
      Article,
    };
  },
  mounted() {
    this.i18n.changeLocale(this.lang);
  },
  computed: {
    availableLanguages(): string[] {
      const lang = Object.keys(this.i18n.messages);
      return lang.filter((l) => l !== this.lang);
    },
  },
  methods: {
    changeLocale(locale: string) {
      this.$router.push({ name: "CreateArticle", params: { lang: locale } });
    },
    async createArticle() {
      this.state.loading = true;
      if ((await this.form.validate()).valid) {
        const article = await this.Article.create(
          this.lang,
          this.fields.article.value
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
      this.state.loading = false;
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
