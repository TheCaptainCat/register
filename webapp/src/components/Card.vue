<template>
  <div :class="['reg-card', outline ? 'outline' : '']">
    <slot />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Card",
  props: {
    outline: {
      type: Boolean,
      default: true,
    },
  },
});
</script>
