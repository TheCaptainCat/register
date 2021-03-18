<template>
  <div>
    <button
      :class="['reg-btn', size, light ? 'light' : '', loading ? 'loading' : '']"
      :disabled="disabled || loading"
    >
      <span class="reg-btn-inner">
        <slot />
        <icon v-if="icon" :name="icon" :size="iconSize" />
      </span>
      <span v-if="loading" class="loading-label">
        <icon name="loading" spin :size="iconSize" />
      </span>
    </button>
  </div>
</template>

<script lang="ts">
import { Icon } from "@/components";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "RegButton",
  components: {
    Icon,
  },
  props: {
    size: {
      type: String as PropType<"sm" | "md" | "lg">,
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
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      iconSizes: {
        sm: 1,
        md: 2,
        lg: 3,
      },
    };
  },
  computed: {
    iconSize(): number {
      return this.iconSizes[this.size];
    },
  },
});
</script>
