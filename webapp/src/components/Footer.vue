<template>
  <div class="reg-footer flex aic">
    <div class="flex-grow-1" />
    <div class="credits">&copy; 2021 - Pierre Chat</div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Footer",
});
</script>

<style lang="scss" scoped>
@import "../styles/variables";

.reg-footer {
  background-color: $grey-lighter;
  height: 25px;

  .credits {
    margin-right: 15px;
  }
}
</style>
