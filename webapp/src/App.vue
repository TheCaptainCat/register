<template>
  <div v-if="userState.loading">
    Loading
  </div>
  <div class="container" v-else>
    <header>
      <navigation />
    </header>
    <main>
      <div v-if="userState.user">
        <router-view />
      </div>
      <div v-else>
        <login />
      </div>
    </main>
    <footer>
      <bottom />
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Navigation from "@/components/Navigation.vue";
import Bottom from "@/components/Bottom.vue";
import useUserFunctions from "@/composition/user/functions";
import userStore from "@/composition/user/store";
import Login from "@/views/Login.vue";

export default defineComponent({
  name: "App",
  components: {
    Bottom,
    Navigation,
    Login
  },
  setup() {
    const { getUserInfo } = useUserFunctions();
    return {
      userState: userStore.state,
      getUserInfo
    };
  },
  async mounted() {
    userStore.setState({ loading: true });
    try {
      const user = await this.getUserInfo();
      userStore.setState({ user, loading: false });
    } catch (e) {
      userStore.setState({ user: undefined, loading: false });
    }
  }
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
