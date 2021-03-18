<template>
  <div class="outer-reg-container">
    <div class="reg-container">
      <div class="reg-inner-container">
        <slot />
      </div>
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

.outer-reg-container {
  display: flex;
  justify-content: center;
  height: 100%;

  .reg-container {
    background-color: $bg-light;
    height: 100%;
    width: 100%;
    margin: 0;

    @media screen and (min-width: $md-breakpoint) {
      width: $md-breakpoint;
    }

    .reg-inner-container {
      padding: 30px 50px;
    }
  }
}
</style>
