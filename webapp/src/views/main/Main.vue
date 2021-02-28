<template>
  <header><nav-bar /></header>
  <main>
    <reg-container>
      <router-view />
    </reg-container>
  </main>
  <footer><reg-footer /></footer>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import NavBar from "@/components/NavBar.vue";
import RegFooter from "@/components/Footer.vue";
import RegContainer from "@/components/containers/Container.vue";

export default defineComponent({
  name: "Main",
  components: { RegContainer, NavBar, RegFooter },
});
</script>

<style lang="scss" scoped></style>
