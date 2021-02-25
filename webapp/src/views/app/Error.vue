<template>
  <reg-card class="app-error-container flex dir-col aic">
    <div class="flex aic">
      <fa-icon icon="exclamation-circle" size="3x" />
      <div class="text">
        {{ $t("views.app.error.text") }}
      </div>
    </div>
    <div class="subtext">
      {{ $t("views.app.error.subtext") }}
    </div>
  </reg-card>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";

export default defineComponent({
  name: "Error",
  setup() {
    const state = reactive({});

    return {
      state,
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
