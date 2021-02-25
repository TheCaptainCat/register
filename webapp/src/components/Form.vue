<template>
  <form class="reg-form" @submit.prevent="submit">
    <slot />
  </form>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Form",
  setup(props, context) {
    const submit = () => context.emit("commit");
    return {
      submit,
    };
  },
});
</script>
