<template>
  <div :class="['reg-card', outline ? 'outline' : '']">
    <slot />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "RegCard",
  props: {
    outline: {
      type: Boolean,
      default: true,
    },
  },
});
</script>
