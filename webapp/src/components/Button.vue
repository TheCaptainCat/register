<template>
  <div>
    <button
      :class="['reg-btn', size, light ? 'light' : '', loading ? 'loading' : '']"
      :disabled="loading"
    >
      <slot />
      <fa-icon v-if="icon" :icon="icon" />
      <div v-if="loading" class="loading-label">
        <fa-icon icon="spinner" spin />
      </div>
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";

export default defineComponent({
  name: "Button",
  props: {
    size: {
      type: String,
      default: "md",
    },
    icon: String,
    light: {
      type: Boolean,
      default: false,
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
  setup() {
    const state = reactive({});
    return {
      state,
    };
  },
});
</script>
