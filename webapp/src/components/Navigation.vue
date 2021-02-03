<template>
  <div class="nav">
    <div>
      <router-link :to="{ name: 'Home' }">Register</router-link>
    </div>
    <div class="spacer" />
    <div v-if="isAdmin">
      <router-link :to="{ name: 'Admin' }">Admin page</router-link>
    </div>
    <div v-if="userStore.user">
      <button @click="logout">Logout</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import userStore from "@/composition/user/store";
import { logout } from "@/composition/user/functions";
import { checkPermissions } from "@/composition/role/functions";
import { AppRoles } from "@/composition/role/model";

export default defineComponent({
  name: "Navigation",
  setup() {
    const userState = userStore.state;
    const isAdmin = computed(
      () =>
        userState.user && checkPermissions(AppRoles.admin, userState.user.roles)
    );

    return {
      userStore: userStore.state,
      logout,
      isAdmin,
    };
  },
});
</script>

<style lang="scss" scoped>
.nav {
  background-color: rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 20px;

  > div {
    margin: 10px;
  }

  .spacer {
    flex-grow: 1;
  }

  .lang-selector {
    display: flex;

    .lang {
      padding-left: 5px;

      &:not(:last-child)::after {
        padding-left: 5px;
        content: "/";
      }

      &:last-child {
        padding-right: 5px;
      }

      a {
        color: blue;
        text-decoration: underline;
        cursor: pointer;
      }
    }
  }
}
</style>
