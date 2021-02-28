<template>
  <nav class="reg-nav flex aic">
    <div class="reg-nav-inner flex max-width">
      <div class="nav-title">
        {{ i18n.t("app.title") }}
      </div>
      <div class="flex-grow-1" />
      <div>
        <language-selector />
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useI18n } from "@/plugins/i18n";
import LanguageSelector from "@/components/LanguageSelector.vue";

export default defineComponent({
  name: "NavBar",
  components: { LanguageSelector },
  setup() {
    const i18n = useI18n();
    return {
      i18n,
    };
  },
});
</script>

<style lang="scss" scoped>
@import "../styles/variables";

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
  }
}
</style>
