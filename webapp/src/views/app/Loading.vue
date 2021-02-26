<template>
  <reg-card class="app-loading-container">
    <div class="app-loading flex dir-col aic">
      <div class="flex aic">
        <icon name="loading" spin :size="3" />
        <div class="text">
          {{ $t("components.loader.text") }}
        </div>
      </div>
      <div class="subtext">
        {{ $t("components.loader.subtext") }}
      </div>
    </div>
  </reg-card>
</template>

<script lang="ts">
import { Icon } from "@/components";
import { defineComponent } from "vue";
import { RegCard } from "@/components/containers";

export default defineComponent({
  name: "Loading",
  components: {
    Icon,
    RegCard,
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
