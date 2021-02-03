<template>
  <header>
    <navigation />
  </header>
  <main>
    <router-view />
  </main>
  <footer>
    <bottom />
  </footer>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import Bottom from "@/components/Bottom.vue";
import Navigation from "@/components/Navigation.vue";

export default defineComponent({
  name: "Main",
  components: {
    Bottom,
    Navigation,
  },
  setup() {
    const state = reactive({});

    return {
      state,
    };
  },
});
</script>

<style lang="scss" scoped></style>
