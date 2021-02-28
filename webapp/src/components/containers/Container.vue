<template>
  <div class="reg-container">
    <div class="reg-inner-container">
      <slot />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "RegContainer",
});
</script>

<style lang="scss" scoped>
@import "../../styles/variables";

.reg-container {
  background-color: $bg-light;
  height: 100%;

  @media screen and (min-width: 1000px) {
    width: 1000px;
    margin-left: calc((100vw - 1000px) / 2);
  }

  @media screen and (max-width: 1000px) {
    width: 100%;
    margin: 0;
  }

  .reg-inner-container {
    padding: 30px 50px;
  }
}
</style>
