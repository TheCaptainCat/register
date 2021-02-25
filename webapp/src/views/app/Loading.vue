<template>
  <reg-card class="app-loading-container">
    <div class="app-loading flex dir-col aic">
      <div class="flex aic">
        <fa-icon icon="spinner" spin size="3x" />
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
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { defineComponent, reactive } from "vue";
import { RegCard } from "@/components/containers";

export default defineComponent({
  name: "Loading",
  components: {
    FaIcon: FontAwesomeIcon,
    RegCard,
  },
  setup() {
    const state = reactive({});
    return {
      state,
    };
  },
});
</script>

<style lang="scss" scoped>
.app-loading-container {
  svg {
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
