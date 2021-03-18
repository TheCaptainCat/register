<template>
  <reg-card class="app-error-container flex dir-col aic">
    <div class="flex aic">
      <icon name="exclamation-circle" size="3x" />
      <div class="text">
        {{ i18n.t("views.app.error.text") }}
      </div>
    </div>
    <div class="subtext">
      {{ i18n.t("views.app.error.subtext") }}
    </div>
  </reg-card>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import RegCard from "@/components/containers/Card.vue";
import { Icon } from "@/components";
import { useI18n } from "@/plugins/i18n";

export default defineComponent({
  name: "Error",
  components: {
    Icon,
    RegCard,
  },
  setup() {
    const i18n = useI18n();
    return {
      i18n,
    };
  },
});
</script>

<style lang="scss" scoped>
.app-error-container {
  svg {
    margin-right: 15px;
  }
  .text {
    font-size: 3rem;
    font-weight: bolder;
  }

  .subtext {
    font-size: 1.5rem;
    font-weight: bold;
  }
}
</style>
