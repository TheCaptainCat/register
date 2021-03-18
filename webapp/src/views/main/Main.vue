<template>
  <header><reg-nav-bar /></header>
  <main>
    <reg-container>
      <router-view />
    </reg-container>
  </main>
  <footer><reg-footer /></footer>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { RegFooter, RegNavBar } from "@/components/layout";
import RegContainer from "@/components/containers/Container.vue";

export default defineComponent({
  name: "Main",
  components: { RegContainer, RegNavBar, RegFooter },
});
</script>

<style lang="scss" scoped></style>
