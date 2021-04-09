<template>
  <section
    class="reg-section"
    :style="{ borderColor: color, backgroundColor: background }"
  >
    <div
      class="section-heading"
      :style="{ borderColor: color, backgroundColor: background }"
    >
      {{ title }}
    </div>
    <div class="section-inner">
      <slot />
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "RegSection",
  props: {
    title: {
      type: String,
      required: true,
    },
    color: String,
    background: String,
  },
});
</script>

<style lang="scss" scoped>
@import "../../styles/variables";

.reg-section {
  position: relative;
  border: $grey-md solid 1px;
  border-radius: $border-radius;
  margin-top: 30px;

  .section-heading {
    position: absolute;
    top: -1rem;
    left: 7px;
    font-weight: bolder;
    font-size: 1.25rem;
    border: $grey-md solid 1px;
    background-color: $bg-light;
    border-radius: $border-radius;
    padding: 2px 8px;
  }

  .section-inner {
    margin: 25px 15px 15px 15px;
    display: flex;
  }
}
</style>
