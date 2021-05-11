<template>
  <router-link v-if="to" :to="to" class="in-link">
    <slot />
  </router-link>
  <a disabled v-else class="in-link error">
    <slot />
  </a>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "InLink",
  props: {
    to: {
      type: Object,
      required: false,
    },
  },
});
</script>

<style lang="scss" scoped>
.in-link {
  color: blue;
  &.error {
    color: red;
  }
}
</style>
