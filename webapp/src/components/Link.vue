<template>
  <router-link :to="to" class="in-link">
    <slot />
  </router-link>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "InLink",
  props: {
    to: {
      type: Object,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
.in-link {
  color: blue;
}
</style>
