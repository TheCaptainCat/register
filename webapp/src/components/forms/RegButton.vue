<template>
  <div>
    <button
      :class="['reg-btn', size, light ? 'light' : '', loading ? 'loading' : '']"
      :disabled="loading"
    >
      <span class="reg-btn-inner">
        <slot />
        <icon v-if="icon" :name="icon" :size="1.5" />
      </span>
      <span v-if="loading" class="loading-label">
        <icon name="loading" spin :size="1.5" />
      </span>
    </button>
  </div>
</template>

<script lang="ts">
import { Icon } from "@/components";
import { defineComponent, reactive } from "vue";

export default defineComponent({
  name: "RegButton",
  components: {
    Icon,
  },
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
