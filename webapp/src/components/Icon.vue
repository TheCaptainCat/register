<template>
  <span
    :style="{ fontSize: `${size}rem` }"
    :class="classes"
    :aria-hidden="ariaHidden"
  />
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";

export default defineComponent({
  name: "Icon",
  props: {
    name: { type: String, required: true },
    rotate: {
      type: Number,
      validator: (value: number) => {
        return [45, 90, 135, 180, 225, 270, 315].includes(value);
      },
    },
    flip: {
      type: String,
      validator: (value: string) => {
        return ["h", "v"].includes(value);
      },
    },
    spin: { type: Boolean, default: false },
    ariaHidden: { type: Boolean, default: false },
    size: { type: Number, default: 1 },
  },
  setup(props) {
    const state = reactive({});
    const classes = ["mdi", "mdi-" + props.name];
    if (props.rotate) classes.push("mdi-rotate-" + props.rotate);
    if (props.flip) classes.push("mdi-flip-" + props.flip);
    if (props.spin) classes.push("mdi-spin");
    return {
      state,
      classes,
    };
  },
});
</script>

<style lang="scss" scoped></style>
