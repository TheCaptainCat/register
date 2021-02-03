<template>
  <div v-if="userStore.loading">Loading</div>
  <div v-else-if="!userStore.user">
    <login />
  </div>
  <div class="container" v-else>
    <main-part />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { getUserInfo } from "@/composition/user/functions";
import userStore from "@/composition/user/store";
import Login from "@/views/Login.vue";
import MainPart from "@/views/Main.vue";

export default defineComponent({
  name: "App",
  components: {
    Login,
    MainPart,
  },
  setup() {
    return {
      userStore: userStore.state,
      getUserInfo,
    };
  },
  async mounted() {
    await this.getUserInfo();
  },
});
</script>

<style lang="scss">
html {
  height: 100%;

  body {
    margin: 0;
    height: 100%;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    height: 100%;

    .container {
      height: 100%;
      display: flex;
      flex-direction: column;

      main {
        flex-grow: 1;
      }
    }
  }
}
</style>
