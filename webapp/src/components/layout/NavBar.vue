<template>
  <nav class="reg-nav flex aic">
    <div class="reg-nav-inner flex max-width aic">
      <div class="nav-title">
        <router-link :to="{ name: 'Home' }">
          {{ i18n.t("app.title") }}
        </router-link>
      </div>
      <div class="flex-grow-1" />
      <div>
        <reg-button
          size="mini"
          :loading="state.loggingOut"
          @click="logoutUser"
          icon="logout"
        >
          {{ i18n.t("components.nav.logout") }}
        </reg-button>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import { useI18n } from "@/plugins/i18n";
import RegButton from "@/components/forms/Button.vue";
import { useUser } from "@/composition/user";

interface NavBarState {
  loggingOut: boolean;
}

export default defineComponent({
  name: "NavBar",
  components: { RegButton },
  setup() {
    const state = reactive<NavBarState>({ loggingOut: false });
    const i18n = useI18n();
    const { logout } = useUser();
    const logoutUser = async () => {
      state.loggingOut = true;
      await logout();
      state.loggingOut = false;
    };
    return {
      i18n,
      state,
      logoutUser,
    };
  },
});
</script>

<style lang="scss" scoped>
@import "../../styles/variables";

.reg-nav {
  background-color: $grey-lighter;
  height: 50px;
  position: sticky;
  top: 0;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.75);

  .reg-nav-inner {
    padding: 0 15px;

    .nav-title {
      font-weight: bolder;
      font-size: 1.5rem;
    }

    > div:not(:last-child) {
      margin-right: 15px;
    }
  }
}
</style>
