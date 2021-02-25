<template>
  <reg-card class="flex aic dir-col">
    <div class="login-header">{{ $t("views.login.header") }}</div>
    <div class="login-subheader">{{ $t("views.login.subheader") }}</div>
    <reg-form @commit="loginUser">
      <reg-input
        label="Username"
        v-model="form.username.value"
        type="text"
        :error="form.username.error"
      />
      <reg-input
        label="Password"
        v-model="form.password.value"
        type="password"
        :error="form.password.error"
      />
      <ul>
        <li v-for="error in state.errors" :key="error">{{ error }}</li>
      </ul>
      <reg-btn icon="sign-in-alt" :loading="state.loading">
        {{ $t("views.login.btn") }}
      </reg-btn>
    </reg-form>
  </reg-card>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import { login } from "@/composition/user";
import { FetchError } from "@/core/requests";

interface LoginState {
  errors: string[];
  loading: boolean;
}

type FormField = { value: string; error: string | null };
interface LoginForm {
  username: FormField;
  password: FormField;
}

export default defineComponent({
  name: "Login",
  setup() {
    const state = reactive<LoginState>({
      errors: [],
      loading: false,
    });
    const form = reactive<LoginForm>({
      username: {
        value: "",
        error: null,
      },
      password: {
        value: "",
        error: null,
      },
    });
    const validateInputs = (): boolean => {
      let ok = true;
      if (!form.username.value) {
        ok = false;
        form.username.error = "required";
      }
      if (!form.password.value) {
        ok = false;
        form.password.error = "required";
      }
      return ok;
    };
    const loginUser = async () => {
      try {
        state.errors = [];
        state.loading = true;
        if (validateInputs())
          await login(form.username.value, form.password.value);
      } catch (err) {
        if (err instanceof FetchError) state.errors = err.errors;
      }
      state.loading = false;
    };
    return {
      state,
      form,
      loginUser,
    };
  },
});
</script>

<style lang="scss" scoped>
.login-header {
  font-weight: bold;
  font-size: 3rem;
}
.login-subheader {
  font-size: 1.5rem;
  margin: 10px 0 30px 0;
}
</style>
