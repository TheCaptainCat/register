<template>
  <div :id="`reg-form-${uid}`" class="reg-form-container">
    <slot />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "RegForm",
  mounted() {
    const elem = document.getElementById(`reg-form-${this.uid}`);
    if (elem) elem.addEventListener("keyup", this.submit);
  },
  beforeUnmount() {
    const elem = document.getElementById(`reg-form-${this.uid}`);
    if (elem) elem.removeEventListener("keyup", this.submit);
  },
  setup(props, context) {
    let uid = Math.random().toString(36).substring(7);
    const submit = (e: KeyboardEvent) => {
      if (e.code === "Enter") context.emit("submit");
    };
    return {
      submit,
      uid,
    };
  },
});
</script>
