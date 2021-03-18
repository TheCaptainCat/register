<template>
  <reg-card class="app-loading-container">
    <div class="app-loading flex dir-col aic">
      <div class="flex aic">
        <icon name="loading" spin :size="3" />
        <div class="text">
          {{ i18n.t("components.loader.text") }}
        </div>
      </div>
      <div class="subtext">
        {{ i18n.t("components.loader.subtext") }}
      </div>
    </div>
  </reg-card>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Icon } from "@/components";
import { useI18n } from "@/plugins/i18n";
import RegCard from "@/components/containers/Card.vue";

export default defineComponent({
  name: "Loading",
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
.app-loading-container {
  .mdi {
    margin-right: 15px;
  }

  .app-loading {
    .text {
      font-size: 3rem;
      font-weight: bolder;
    }

    .subtext {
      font-size: 1.5rem;
      font-weight: bold;
    }
  }
}
</style>
