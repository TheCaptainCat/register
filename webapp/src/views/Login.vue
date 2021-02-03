<template>
  <form @submit.prevent="login">
    <label>
      Username
      <input name="username" v-model="state.username" />
    </label>
    <label>
      Password
      <input name="password" v-model="state.password" type="password" />
    </label>
    <button type="submit">Login</button>
  </form>
  <div v-if="state.errors.length">
    <ul>
      <li v-for="error in state.errors" :key="error">
        {{ error }}
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import { login } from "@/composition/user/functions";
import { FetchError } from "@/core/requests";

interface State {
  username: string;
  password: string;
  errors: string[];
}

export default defineComponent({
  name: "Login",
  setup() {
    const state = reactive<State>({
      username: "",
      password: "",
      errors: [],
    });

    const loginFunc = async function () {
      try {
        await login(state.username, state.password);
      } catch (e) {
        if (e instanceof FetchError) state.errors = e.errors;
      }
    };

    return {
      state,
      login: loginFunc,
    };
  },
});
</script>

<style lang="scss" scoped></style>
