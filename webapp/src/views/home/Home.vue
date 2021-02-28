<template>
  <div class="home-page">
    <h1>{{ i18n.t("views.home.welcome") }}</h1>
    <h2>{{ i18n.t("views.home.private") }}</h2>
    <reg-section
      v-if="hasRole('admin')"
      :title="i18n.t('views.home.admin')"
      color="red"
      background="white"
    >
      Manage users
    </reg-section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useI18n } from "@/plugins/i18n";
import RegSection from "@/components/containers/Section.vue";
import { hasRole } from "@/composition/user";

export default defineComponent({
  name: "Home",
  components: { RegSection },
  setup() {
    const i18n = useI18n();
    return {
      i18n,
      hasRole,
    };
  },
});
</script>

<style lang="scss" scoped>
@import "../../styles/variables";

.home-page {
  h1 {
    font-size: 1.75rem;
  }
  h2 {
    font-size: 1.25rem;
    opacity: 0.75;
  }

  section {
    margin-top: 30px;
  }
}
</style>
