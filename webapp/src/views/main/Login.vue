<template>
  <reg-card class="flex aic dir-col">
    <div class="login-header">{{ i18n.t("views.login.header") }}</div>
    <div class="login-subheader">{{ i18n.t("views.login.subheader") }}</div>
    <reg-form @submit="loginUser">
      <reg-input
        name="username"
        :label="i18n.t('views.login.username')"
        v-model="fields.username.value"
        :error="fields.username.error"
        fluid
      />
      <reg-input
        name="password"
        :label="i18n.t('views.login.password')"
        type="password"
        v-model="fields.password.value"
        :error="fields.password.error"
        fluid
      />
      <reg-button icon="login" :loading="state.loading" @click="loginUser">
        {{ i18n.t("views.login.btn") }}
      </reg-button>
    </reg-form>
    <LanguageSelector
      class="language-selector"
      @updated:locale="(locale) => i18n.changeLocale(locale)"
    />
  </reg-card>
</template>

<script lang="ts">
import { useField, useForm } from "vee-validate";
import * as yup from "yup";
import { defineComponent, reactive } from "vue";
import { useI18n } from "@/plugins/i18n";
import { useUser } from "@/composition/user";
import { FetchError } from "@/core/requests";
import RegCard from "@/components/containers/Card.vue";
import { LanguageSelector } from "@/components";
import RegForm from "@/components/forms/Form.vue";
import RegInput from "@/components/forms/Input.vue";
import RegButton from "@/components/forms/Button.vue";

interface LoginState {
  errors: string[];
  loading: boolean;
}

export default defineComponent({
  name: "Login",
  components: {
    LanguageSelector,
    RegForm,
    RegButton,
    RegInput,
    RegCard,
  },
  setup() {
    const i18n = useI18n();
    const state = reactive<LoginState>({
      errors: [],
      loading: false,
    });
    const { form, fields } = createForm();
    const { login } = useUser();
    const loginUser = async () => {
      try {
        state.errors = [];
        state.loading = true;
        if ((await form.validate()).valid) {
          await login(fields.username.value, fields.password.value);
        }
      } catch (err) {
        if (err instanceof FetchError) state.errors = err.errors;
      }
      state.loading = false;
    };
    return {
      i18n,
      state,
      fields,
      loginUser,
    };
  },
});

const createForm = () => {
  const form = useForm({
    validationSchema: yup.object({
      username: yup.string().required().min(4),
      password: yup.string().required().min(4),
    }),
  });
  const { value: username, errorMessage: usernameError } = useField<string>(
    "username"
  );
  const { value: password, errorMessage: passwordError } = useField<string>(
    "password"
  );
  return {
    form,
    fields: reactive({
      username: {
        value: username,
        error: usernameError,
      },
      password: {
        value: password,
        error: passwordError,
      },
    }),
  };
};
</script>

<style lang="scss" scoped>
@import "../../styles/variables";

.login-header {
  font-weight: bold;
  font-size: 3rem;
}
.login-subheader {
  font-size: 1.5rem;
  margin: 10px 0 30px 0;
}
.language-selector {
  margin-top: 15px;
}
</style>
