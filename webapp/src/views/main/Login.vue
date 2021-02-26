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
      />
      <reg-input
        name="password"
        :label="i18n.t('views.login.password')"
        type="password"
        v-model="fields.password.value"
        :error="fields.password.error"
      />
      <reg-button icon="login" :loading="state.loading" @click="loginUser">
        {{ i18n.t("views.login.btn") }}
      </reg-button>
    </reg-form>
  </reg-card>
</template>

<script lang="ts">
import { useField, useForm } from "vee-validate";
import * as yup from "yup";
import { defineComponent, reactive } from "vue";
import { useI18n } from "@/plugins/i18n";
import { login } from "@/composition/user";
import { FetchError } from "@/core/requests";
import { RegForm, RegButton, RegInput } from "@/components/forms";
import { RegCard } from "@/components/containers";

interface LoginState {
  errors: string[];
  loading: boolean;
}

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

export default defineComponent({
  name: "Login",
  components: {
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
.error-wrapper {
  list-style: none;
  padding: 5px 10px;
  border: red solid 1px;
  color: red;
  border-radius: $border-radius;
}
</style>
