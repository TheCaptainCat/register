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
  <main-part v-else />
</template>

<script lang="ts">
import { defineComponent, reactive, computed } from "vue";
import { provideI18n, buildI18nStrings } from "@/plugins/i18n";
import { useUser, userStore } from "@/composition/user";
import { FetchError } from "@/core/requests";
import fr from "@/i18n/fr";
import en from "@/i18n/en";

import Login from "@/views/main/Login.vue";
import Loading from "@/views/main/Loading.vue";
import Error from "@/views/main/Error.vue";
import Main from "@/views/main/Main.vue";

interface AppState {
  loading: boolean;
  error: boolean;
}

const fetchInitData = async (state: AppState) => {
  try {
    await useUser().fetchUserInfo();
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
  components: { Loading, Login, Error, MainPart: Main },
  setup() {
    provideI18n("en", buildI18nStrings({ en, fr }));
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
