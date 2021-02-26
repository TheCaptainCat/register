<template>
  <header>nav</header>
  <main>
    <router-view />
  </main>
  <footer>footer</footer>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Main",
});
</script>

<style lang="scss" scoped></style>
