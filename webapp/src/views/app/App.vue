<template>
  <div v-if="state.loading" class="flex aic jcc max-height">
    <loading />
  </div>
  <div
    v-else-if="state.error"
    class="app-loading-container flex aic jcc max-height"
  >
    <Error />
  </div>
  <div v-else-if="!authenticated" class="flex aic jcc max-height">
    <Login />
  </div>
  <div v-else>
    <h1>Register</h1>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, computed } from "vue";
import { provideI18n } from "@/plugins/i18n";
import { fetchUserInfo, userStore } from "@/composition/user";
import { FetchError } from "@/core/requests";
import Login from "@/views/Login.vue";
import Loading from "@/views/app/Loading.vue";
import Error from "@/views/app/Error.vue";
import fr from "@/i18n/fr";
import en from "@/i18n/en";

interface AppState {
  loading: boolean;
  error: boolean;
}

const fetchInitData = async (state: AppState) => {
  try {
    await fetchUserInfo();
  } catch (err) {
    if (!(err instanceof FetchError && err.code === 401)) {
      state.error = true;
    }
  } finally {
    state.loading = false;
  }
};

export default defineComponent({
  name: "App",
  components: { Loading, Login, Error },
  setup() {
    provideI18n({ fr, en }, "en");
    const state = reactive<AppState>({
      loading: true,
      error: false,
    });
    const authenticated = computed(() => userStore.state.authenticated);
    fetchInitData(state);
    return {
      state,
      authenticated,
    };
  },
});
</script>
