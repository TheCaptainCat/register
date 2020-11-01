<template>
  <div class="home">Welcome {{ userState.user.username }}</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import userStore from "@/composition/user/store";

export default defineComponent({
  name: "Home",
  setup() {
    return {
      userState: userStore.state
    };
  }
});
</script>
