<template>
  <div class="nav">
    <div>
      Register
    </div>
    <div class="spacer" />
    <div v-if="userState.user">
      <button @click="logout">Logout</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import userStore from "@/composition/user/store";
import useUserFunctions from "@/composition/user/functions";

export default defineComponent({
  name: "Navigation",
  setup() {
    const { logout } = useUserFunctions();

    return {
      userState: userStore.state,
      logout
    };
  }
});
</script>

<style lang="scss" scoped>
.nav {
  border: red solid thin;
  display: flex;
  flex-direction: row;

  .spacer {
    flex-grow: 1;
  }
}
</style>
